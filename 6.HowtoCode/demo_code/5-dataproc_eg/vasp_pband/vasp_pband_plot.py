#!/usr/bin/python3
# Author: liyang@cmt.tsinghua
# Date: 2020.09.02
# Descripution: This script is designed for plot the projection band
#                 of VASP calculation.
import json
import os
import sys
import re
import argparse
import math
import numpy as np
print("[do] Loading the matplotlib.pyplot...")
import matplotlib.pyplot as plt
plt.switch_backend('agg') # For GUI less server


def check_python_version():
  """Check the python version"""
  curr_python_version = sys.version
  if curr_python_version[0] != '3':
    print('[error] Please use the python3 run this script...')
    sys.exit()
  return 0


def get_command_line_input():
  """Read in the command line parameters"""
  parser = argparse.ArgumentParser("Basic VASP band plot parameters")
  parser.add_argument('-l', '--xmin-i', dest='min_kp_index', 
                      default=-1, type=int,
                      help='Band minimal kpoints index (begin from 1).')
  parser.add_argument('-r', '--xmax-i', dest='max_kp_index', 
                      default=-1, type=int,
                      help='Band maximal kpoints index (begin from 1).')
  parser.add_argument('-d', '--ymin', dest='min_plot_energy', 
                      default=-3, type=float,
                      help='Minimal plot energy windows.')
  parser.add_argument('-u', '--ymax', dest='max_plot_energy', 
                      default=3, type=float,
                      help='Maximal plot energy windows.')
  parser.add_argument('-f', '--format', dest='plot_format', 
                      default='pdf', type=str, choices=['png', 'eps', 'pdf'],
                      help='Plot format.')
  parser.add_argument('-i', '--dpi', dest='plot_dpi', 
                      default=400, type=int,
                      help='Plot resolution (dpi).')
  parser.add_argument('-s', '--point-size', dest='plot_point_size', 
                      default=1.0, type=float,
                      help='Plot resolution (dpi).')
  parser.add_argument('-o', '--output', dest='plot_filename', 
                      default='band', type=str,
                      help='Output file name.')
  parser.add_argument('-p', '--project', dest='project_atoms', 
                      default='1', type=str,
                      help='The projected atoms.')
  parser.add_argument('-b', '--orbit', dest='project_orbit',
                      default='dxy,dz2', type=str,
                      help='The plot projected orbitals, please check the PROCAR to get the label of each orbital. Split the orbital by comma(",") without blank(" ").')
  parser.add_argument('-x', '--no-plot', dest='no_plot', action='store_const',
                      const=True, default=False,
                      help='Do not plot the band.')
  args = parser.parse_args()
  plot_args = {"min_kp_index"    : args.min_kp_index - 1,
               "max_kp_index"    : args.max_kp_index - 1,
               "min_plot_energy" : args.min_plot_energy,
               "max_plot_energy" : args.max_plot_energy,
               "plot_format"     : args.plot_format,
               "plot_dpi"        : args.plot_dpi,
               "plot_point_size" : args.plot_point_size,
               "plot_filename"   : args.plot_filename,
               "project_atoms"   : args.project_atoms,
               "project_orbit"   : args.project_orbit,
               "no_plot"         : args.no_plot}
  return plot_args


def cal_k_distance(local_rlv, start_kpoint_frac, end_kpoint_frac):
  """ Calculate the distance of two different kpoints in k-space"""
  # Reciprocal lattice vector but localy uesd :: local_rlv
  # Start kpoints in frac k-cooridnate :: start_kpoint
  # End kpoints in frac k-cooridnate :: end_kpoint

  # Calcualte the k-cooridnate in Cartesian indicator
  start_kpoints_cart = np.array([0.0, 0.0, 0.0])
  end_kpoints_cart = np.array([0.0, 0.0, 0.0])
  #
  # k_cart = k_frac * rlv
  #                               __              __
  #                               | b_1x b_1y b_1z |
  #        = (kf_1, kf_2, kf_3) * | b_2x b_2y b_2z |
  #                               | b_3x b_3y b_3z |
  #                               --              --
  #        = (kc_x, kc_y, kc_z)
  #
  for xyz in range(3):
    start_kpoints_cart[xyz] = 0.0
    for b_index in range(3):
      start_kpoints_cart[xyz] += start_kpoint_frac[b_index] * \
                                 local_rlv[b_index, xyz]
      end_kpoints_cart[xyz] += end_kpoint_frac[b_index] * \
                               local_rlv[b_index, xyz]
  # Calculate the k distance of the two kpoints
  k_distance = math.sqrt(sum((start_kpoints_cart - end_kpoints_cart) ** 2))
  return k_distance


def read_kpath_info(plot_args):
  """Read in the kpath, fermi level, and spin number informations"""
  ## Check the existance of the OUTCAR.
  if not os.path.isfile('OUTCAR'):
    print("[error] OUTCAR not found!!!")
    sys.exit(0)
  ## Spin Number, Recp. Lattice Vec.(rlv) & Fermi Energy
  # Reciprocal lattice vector :: rlv
  # Each row of the 'rlv' matrix is a basis vector
  spin_num = -1
  rlv = np.zeros((3, 3))
  writing_rlv = False
  fermi_energy = 9999999999.00
  with open("OUTCAR") as frp:
    for line in frp:
      if 'ISPIN' in line:
        spin_num = int(line.split()[2])
      if writing_rlv:
        rlv_index += 1
        if rlv_index > 2:
          writing_rlv = False
          continue
        line = line.replace('\n','')
        rlv[rlv_index, 0] = float(line[43:58])
        rlv[rlv_index, 1] = float(line[58:71])
        rlv[rlv_index, 2] = float(line[71:84])
      elif 'reciprocal lattice vectors' in line:
        writing_rlv = True
        rlv_index = -1
        continue
      if 'E-fermi' in line:
        fermi_energy = float(line.split()[2])
      if 'ICHARG' in line:
        icharge = line.split()[2]
        if icharge == '11':
          print("[warning] You are using the OUTCAR of the BAND step, ")
          print("            which fermi energy may not correct...")
      if 'LNONCOLLINEAR' in line:
        if 'T' == line.split()[2]:
          is_cl = False
        else:
          is_cl = True
  # Check the validation of spin_num
  if spin_num not in [1, 2]:
    print('[error] Spin Number Must be 1 or 2!!!')
    sys.exit(0)
  ## Kpoints Quantity Each Kpath, K Path Quantity, K Points Quantity
  ##   K Path Vec. & K Path Symbol
  # Read in the kpoints file
  kts_is_line_mode = False
  khi_is_line_mode = False
  if os.path.isfile('KPOINTS'):
    with open("KPOINTS") as frp:
      kts_lines = frp.readlines()
      kts_is_line_mode = 'line' in kts_lines[2].lower()
  if os.path.isfile('KPATH.in'):
    with open("KPATH.in") as frp:
      khi_lines = frp.readlines()
      khi_is_line_mode = 'line' in khi_lines[2].lower()
  if kts_is_line_mode:
    lines = kts_lines
  elif khi_is_line_mode:
    print("[info] KPOINTS is not in line mode, using KPATH.in...")
    lines = khi_lines
  else:
    print('[error] No line mode KPOINTS or KPATH.in was found...')
    sys.exit(1)
  # Read kpoints number
  kpoints_quantity_each_kpath = int(lines[1].split()[0])
  hsk_quantity = 0 # High Symmetic Kpoint quantity
  for line in lines[1:]:
    line = line.replace('#', ' ').replace('!',' ').replace('\n','')
    curr_line_ele_num = len(line.split())
    if re.search('[0-9]', line) and \
       (curr_line_ele_num == 3 or curr_line_ele_num == 4):
      hsk_quantity += 1
  kpath_quantity = hsk_quantity // 2
  plot_kpoints_quantity = kpoints_quantity_each_kpath * kpath_quantity
  kpath_symbol_list = [['#', '#'] for path in range(kpath_quantity)]
  kpath_vector_list = [[[], []] for path in range(kpath_quantity)]
  hsk_index = -1 # High Symmetic Kpoint index
  if kpath_quantity == 0:
    print('[error] Kpath Numbre = 0, pls check the KPOINTS file...')
    sys.exit(1)
  for line in lines:
    line = line.replace('#', ' ').replace('!',' ').replace('\n','')
    curr_line_ele_num = len(line.split())
    if re.search('[0-9]', line) and \
       (curr_line_ele_num == 3 or curr_line_ele_num == 4):
      line = line.split()
      hsk_index += 1
      hsk_pair_index = hsk_index % 2
      kpath_index = hsk_index // 2
      kpath_vector_list[kpath_index][hsk_pair_index] = \
        [float(line[0]), float(line[1]), float(line[2])]
      if len(line) == 4:
        kpath_symbol_list[kpath_index][hsk_pair_index] = line[3]
  ## Plot kpath symbol
  # Prepare the symbol of k-axis (xtics)
  hsk_symbol_list = ['' for kpath_index in range(kpath_quantity+1)]
  hsk_symbol_list[0] = kpath_symbol_list[0][0]
  for kpath_index in range(1, kpath_quantity):
    if kpath_symbol_list[kpath_index][0] == kpath_symbol_list[kpath_index-1][1]:
      hsk_symbol_list[kpath_index] = kpath_symbol_list[kpath_index][0]
    else:
      hsk_symbol_list[kpath_index] = kpath_symbol_list[kpath_index-1][1] + \
                                     '|' + kpath_symbol_list[kpath_index][0]
  hsk_symbol_list[kpath_quantity] = kpath_symbol_list[-1][1]
  plot_hsk_symbol_list = []
  for symbol in hsk_symbol_list:
    symbol = symbol.replace("\\", "")
    symbol = symbol.replace('GAMMA',u"\u0393") 
    symbol = symbol.replace('Gamma',u"\u0393")
    symbol = symbol.replace('gamma',u"\u0393")
    symbol = symbol.replace('G',u"\u0393")
    symbol = symbol.replace('g',u"\u0393")
    plot_hsk_symbol_list.append(symbol)
  # Kpoints index
  
  ## Pack the parameters
  kp_data = {"spin_num"                    : spin_num,
             "rlv"                         : rlv,
             "fermi_energy"                : fermi_energy,
             "hsk_quantity"                : hsk_quantity,
             "kpath_quantity"              : kpath_quantity,
             "plot_kpoints_quantity"       : plot_kpoints_quantity,
             "kpoints_quantity_each_kpath" : kpoints_quantity_each_kpath,
             "kpath_symbol_list"           : kpath_symbol_list,
             "plot_hsk_symbol_list"        : plot_hsk_symbol_list,
             "kpath_vector_list"           : kpath_vector_list,
             "is_cl"                       : is_cl}
  return kp_data


def get_kpoints_coors(kp_data, kpoints_vector_list):
  """Calculate cooridinate of kpotions using rlv and fractional k points."""
  kpath_quantity = kp_data['kpath_quantity']
  rlv = kp_data['rlv']
  kpath_vector_list = kp_data['kpath_vector_list']
  kpoints_quantity = kp_data['kpoints_quantity']
  kpoints_quantity_each_kpath = kp_data['kpoints_quantity_each_kpath']
  beg_ki = kp_data["beg_ki"]
  # Get the length of each k-path in k-space
  hsk_distance_list = [0.0 for kpath_index in range(kpath_quantity)]
  sum_hsk_distance_list = [0.0 for kpath_index in range(kpath_quantity)]
  for kpath_index in range(kpath_quantity):
    start_hsk = kpath_vector_list[kpath_index][0]
    end_hsk = kpath_vector_list[kpath_index][1]
    hsk_distance_list[kpath_index] = cal_k_distance(rlv, start_hsk, end_hsk)
    sum_hsk_distance_list[kpath_index] = sum(hsk_distance_list[0:kpath_index+1])
  hsk_corrdinate_list = [0.0] + sum_hsk_distance_list # add gamma point
  hsk_corrdinate_list = np.array(hsk_corrdinate_list)
  # Get the distance in k-space about a k-points on the k-path
  kpoints_corrdinate_list = np.zeros(kpoints_quantity)
  kpoints_index = beg_ki - 1
  for kpath_index in range(kpath_quantity):
    # Count the Previous kpath distance
    pre_path_distance = hsk_corrdinate_list[kpath_index]
    # Calculate the kpoints' distance in current kpath
    for _ in range(kpoints_quantity_each_kpath):
      kpoints_index += 1
      start_hsk = kpath_vector_list[kpath_index][0]
      end_hsk = kpoints_vector_list[kpoints_index]
      # The total distance equals to (pre_path_dis + curr_dis)
      kpoints_corrdinate_list[kpoints_index] = \
        pre_path_distance + cal_k_distance(rlv, start_hsk, end_hsk)
  return hsk_corrdinate_list, kpoints_corrdinate_list


def read_tband(plot_args, kp_data):
  """Read the total band data"""
  ## Check the EIGENVAL file
  if not os.path.isfile('EIGENVAL'):
    print("[error] EIGENVAL not found!!!")
    sys.exit(0)
  ## Initial the kpath data
  plot_kpoints_quantity = kp_data["plot_kpoints_quantity"]
  spin_num = kp_data["spin_num"]
  fermi_energy = kp_data['fermi_energy']
  ## Kpoints Quantity, Band Quantity & Band Data
  with open ("EIGENVAL") as frp:
    lines = frp.readlines()
  kpoints_quantity = int(lines[5].split()[1])
  # Read the plot kpoints index
  min_kp_index = plot_args["min_kp_index"]
  max_kp_index = plot_args["max_kp_index"]
  beg_ki = 0
  end_ki = kpoints_quantity - 1
  if min_kp_index >= 0:
    beg_ki = min_kp_index
  if max_kp_index > 0:
    end_ki = max_kp_index
  if plot_kpoints_quantity != (end_ki - beg_ki + 1):
    print('[error] EIGENVAL kpoints quantity do not match with KPOINTS!!!')
    sys.exit(1)
  kp_data["kpoints_quantity"] = kpoints_quantity
  kp_data["beg_ki"] = beg_ki
  kp_data["end_ki"] = end_ki
  # Read band quantity
  band_quantity = int(lines[5].split()[2])
  # Read band data
  # Init. the band data matrix using numpy array
  spin_up_band = np.zeros((band_quantity, kpoints_quantity))
  spin_dn_band = np.array([])
  if spin_num == 2:
    spin_dn_band = np.zeros((band_quantity, kpoints_quantity))
  kpoints_vector_list = [[] for kpoints in range(kpoints_quantity)]
  # Set the band data block info
  data_start_line_index = 7
  # Read the band data from EIGENVAL
  read_line_index = data_start_line_index
  for kpoints_index in range(kpoints_quantity):
    line = lines[read_line_index].split()
    kpoints_vector_list[kpoints_index] = [float(line[0]), 
                                          float(line[1]), 
                                          float(line[2])]
    read_line_index += 1
    for band_index in range(band_quantity):
      line = lines[read_line_index].split()
      spin_up_band[band_index, kpoints_index] = float(line[1]) - fermi_energy
      if spin_num == 2: 
        spin_dn_band[band_index, kpoints_index] = float(line[2]) - fermi_energy
      read_line_index += 1 # Read next band line
    read_line_index += 1 # Skip the blank line
  # Combine the band
  band_data = [spin_up_band, spin_dn_band]
  # Get the kpoints coors
  hsk_corrdinate_list, kpoints_corrdinate_list = \
    get_kpoints_coors(kp_data, kpoints_vector_list)
  # Cut the kp list
  kpoints_corrdinate_list = kpoints_corrdinate_list[beg_ki:end_ki+1]
  # Cut the kpoints band
  band_data[0] = band_data[0][:, beg_ki:end_ki+1]
  if spin_num == 2:
    band_data[1] = band_data[1][:, beg_ki:end_ki+1]
  # Packup the data
  kp_data["hsk_corrdinate_list"] = hsk_corrdinate_list
  kp_data["kpoints_corrdinate_list"] = kpoints_corrdinate_list
  tband_data = {"band_quantity" : band_quantity,
                "energys"       : band_data}
  return kp_data, tband_data



def check_poscar():
  """Check POSCAR and report the elements"""
  element_table = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
  'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 
  'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 
  'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Tu', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 
  'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 
  'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 
  'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 
  'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 
  'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 
  'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
  if not os.path.isfile('POSCAR'):
    print("[error] POSCAR not found...")
    sys.exit(1)
  with open('POSCAR') as frp:
    lines = frp.readlines()
  poscar_elements = lines[5].replace('\n','').split()
  poscar_elements_num = lines[6].replace('\n','').split()
  poscar_elements_num = [int(val) for val in poscar_elements_num]
  for element in poscar_elements:
    if element not in element_table:
      print("[error] POSCAR element list error...")
      print("[error] Please make sure the 6th line is the element list...")
      sys.exit(1)
  return poscar_elements, poscar_elements_num


def check_project_input(project_str):
  """Refromal the projection strings"""
  poscar_elements, poscar_elements_num = check_poscar()
  project_str = project_str.replace('\n', '')
  project_str = project_str.replace(',', ' ')
  project_str = project_str.split()
  project_atoms = []
  for index in range(len(poscar_elements)):
    element = poscar_elements[index]
    if element in project_str:
      while element in project_str:
        project_str.remove(element)
      beg_index = sum(poscar_elements_num[:index])
      end_index = sum(poscar_elements_num[:(index+1)])
      for atom_index in range(beg_index, end_index):
        project_atoms.append(atom_index+1)
  if project_str != []:
    try:
      remain_atoms = [int(val) for val in project_str]
    except TypeError:
      print("[error] Please check the project atoms string...")
      sys.exit()
    project_atoms += remain_atoms
  project_atoms = list(set(project_atoms))
  project_atoms.sort()
  return project_atoms


def read_pband_data(plot_args, kp_data, project_atoms):
  """Read the projection band data"""
  project_orbit_str = plot_args["project_orbit"]
  ## Check the PROCAR file
  if not os.path.isfile('PROCAR'):
    print("[error] PROCAR not found!!!")
    sys.exit(0)
  with open('PROCAR') as frp:
    lines = frp.readlines()
  # Determin the data block size
  kpoints_quantity = int(lines[1].split()[3])
  band_quantity = int(lines[1].split()[7])
  ions_quantity = int(lines[1].split()[11])
  spin_num = kp_data['spin_num']
  k_init_block_size = 3
  k_band_block_size =  ions_quantity + 1
  if kp_data["is_cl"]:
    dirc_num = 1
  else:
    dirc_num = 4
  total_kbb_size = 3 + k_band_block_size * dirc_num + 1
  k_block_size = k_init_block_size + band_quantity * total_kbb_size
  spin_block_size = k_block_size * kpoints_quantity + 1
  file_size = spin_block_size * spin_num + 1
  if len(lines) != file_size:
    print('[error] PROCAR format error...')
    sys.exit()
  # Read the project orbits
  orbits = lines[7].replace('\n','').split()
  project_orbit_indexs = []
  project_orbits = []
  for index in range(1, len(orbits)-1):
    orbit = orbits[index]
    if (orbit in project_orbit_str) or \
       ('all' in project_orbit_str):
      project_orbit_indexs.append(index)
      project_orbits.append(orbits[index])
  # Read the band weight
  spin_up_pband_data = [\
    [{} for j in range(kpoints_quantity)] \
    for i in range(band_quantity)]
  spin_dn_pband_data = []
  for band_index in range(band_quantity):
    for kpoint_index in range(kpoints_quantity):
      total_weight = 0
      for proj_index in project_orbit_indexs:
        orb_weight = 0
        for atom_order in project_atoms:
          line_index = 1 + kpoint_index * k_block_size + k_init_block_size + \
                       total_kbb_size * band_index + 3 + atom_order
          line = lines[line_index].replace('\n','').split()
          orb_weight += float(line[proj_index])
        orbit = orbits[proj_index]
        spin_up_pband_data[band_index][kpoint_index][orbit] = orb_weight
        total_weight += orb_weight
      spin_up_pband_data[band_index][kpoint_index]['total'] = total_weight
  if spin_num == 2:
    spin_dn_pband_data = [\
      [{} for j in range(kpoints_quantity)] \
      for i in range(band_quantity)]
    for band_index in range(band_quantity):
      for kpoint_index in range(kpoints_quantity):
        total_weight = 0
        for proj_index in project_orbit_indexs:
          orb_weight = 0
          for atom_order in project_atoms: 
            line_index = spin_block_size + \
                         1 + kpoint_index * k_block_size + k_init_block_size + \
                         total_kbb_size * band_index + 3 + atom_order
            line = lines[line_index].replace('\n','').split()
            orb_weight += float(line[proj_index])
          orbit = orbits[proj_index]
          spin_dn_pband_data[band_index][kpoint_index][orbit] = orb_weight
          total_weight += orb_weight 
        spin_dn_pband_data[band_index][kpoint_index]['total'] = total_weight
  # Cut the kpoints
  beg_ki = kp_data["beg_ki"]
  end_ki = kp_data["end_ki"]
  spin_up_pband_data = \
    [spin_up_pband_data[i][beg_ki:end_ki+1] \
      for i in range(len(spin_up_pband_data))]
  if spin_num == 2:
    spin_dn_pband_data = \
      [spin_dn_pband_data[i][beg_ki:end_ki+1] \
        for i in range(len(spin_dn_pband_data))]
  pband_data = {"project_atoms" : project_atoms,
                "project_orbit" : project_orbits,
                "weight"        : [spin_up_pband_data, spin_dn_pband_data]}
  return pband_data


def store_band(plot_args, kp_data, tband_data, pband_data):
  """Store the band data to file"""
  plot_filename = plot_args["plot_filename"]
  json_filename = plot_filename + '.json'
  txt_filename = plot_filename + '.txt'
  project_atoms = plot_args["project_atoms"]
  data = {"kpath"         : kp_data, 
          "total_band"    : tband_data,
          "project_band"  : pband_data}
  data['kpath']['rlv'] = data['kpath']['rlv'].tolist()
  data['kpath']['hsk_corrdinate_list'] = \
    data['kpath']['hsk_corrdinate_list'].tolist()
  data['kpath']['kpoints_corrdinate_list'] = \
    data['kpath']['kpoints_corrdinate_list'].tolist()
  data['total_band']['energys'][0] = data['total_band']['energys'][0].tolist()
  data['total_band']['energys'][1] = data['total_band']['energys'][1].tolist()
  with open(json_filename, 'w') as jfwp:
    json.dump(data, jfwp, indent=2)
  # Write the txt file 
  hsk_corrdinate_list = kp_data["hsk_corrdinate_list"]
  plot_hsk_symbol_list = kp_data["plot_hsk_symbol_list"]
  kpoints_corrdinate_list = kp_data["kpoints_corrdinate_list"]
  spin_num = kp_data["spin_num"]
  plot_kpoints_quantity = kp_data["plot_kpoints_quantity"]
  band_quantity = tband_data["band_quantity"]
  energys = tband_data["energys"]
  orbits = pband_data["project_orbit"]
  atoms = pband_data["project_atoms"]
  weight = pband_data["weight"]
  txt_strs = ['# HSK COORS  :  %s\n' %str(hsk_corrdinate_list),
              '# HSK SYMBOL :  %s\n' %str(plot_hsk_symbol_list),
              '# PROJ ATOMS :  %s\n' %str(atoms),
              '\n',
              '\n']
  if project_atoms.replace('\n','').replace(' ','') == '':
    if spin_num == 1:
      for band_index in range(band_quantity):
        txt_strs.append('# K-coors        Spin-up(eV)\n')
        for kpoint_index in range(plot_kpoints_quantity):
          txt_strs.append('  %.8f    %.8f\n' \
                          %(kpoints_corrdinate_list[kpoint_index],
                            energys[0][band_index][kpoint_index]))
        txt_strs.append('\n')
    elif spin_num == 2:
      for band_index in range(band_quantity):
        txt_strs.append('# K-coors        Spin-up(eV)     Spin-dn(eV)\n')
        for kpoint_index in range(plot_kpoints_quantity):
          txt_strs.append('  %.8f    %.8f    %.8f\n' \
                          %(kpoints_corrdinate_list[kpoint_index],
                            energys[0][band_index][kpoint_index],
                            energys[1][band_index][kpoint_index]))
        txt_strs.append('\n')
  else:
    if spin_num == 1:
      title = '# K-coors       Spin-up(eV)   '
      for orbit in orbits:
        title += '%8s    ' %orbit
      for band_index in range(band_quantity):
        txt_strs.append(title + '\n')
        for kpoint_index in range(plot_kpoints_quantity):
          line = '  %.8f    %.8f  '%(kpoints_corrdinate_list[kpoint_index],
                                     energys[0][band_index][kpoint_index])
          for orbit in orbits:
            line += '  %.6f  ' %(weight[0][band_index][kpoint_index][orbit])
          txt_strs.append(line + '\n')
        txt_strs.append('\n')
    elif spin_num == 2:
      # Get the title
      title = '# K-coors        Spin-up(eV)  '
      for orbit in orbits:
        title += '%8s    ' %orbit
      title += '   Spin-up(eV)  '
      for orbit in orbits:
        title += '%6s    ' %orbit
      # Get the band contect
      for band_index in range(band_quantity):
        txt_strs.append(title + '\n')
        for kpoint_index in range(plot_kpoints_quantity):
          line = '  %.8f    %.8f  '%(kpoints_corrdinate_list[kpoint_index],
                                     energys[0][band_index][kpoint_index])
          for orbit in orbits:
            line += '  %.6f  ' %(weight[0][band_index][kpoint_index][orbit])
          line += '  %.8f  '%(energys[1][band_index][kpoint_index])
          for orbit in orbits:
            line += '  %.6f  ' %(weight[1][band_index][kpoint_index][orbit])
          txt_strs.append(line + '\n')
        txt_strs.append('\n')
  with open(txt_filename, 'w') as fwp:
    fwp.writelines(txt_strs)
  return 0


def plot_band(plot_args, kp_data, tband_data, pband_data):
  """Plot the band"""
  min_plot_energy = plot_args["min_plot_energy"]
  max_plot_energy = plot_args["max_plot_energy"]
  plot_filename = plot_args['plot_filename']
  plot_dpi = plot_args['plot_dpi']
  plot_format = plot_args['plot_format']
  plot_point_size = plot_args["plot_point_size"]
  hsk_corrdinate_list = kp_data["hsk_corrdinate_list"]
  plot_hsk_symbol_list = kp_data["plot_hsk_symbol_list"]
  kpath_quantity = kp_data["kpath_quantity"]
  plot_kpoints_quantity = kp_data["plot_kpoints_quantity"]
  kpoints_corrdinate_list = kp_data["kpoints_corrdinate_list"]
  spin_num = kp_data["spin_num"]
  band_quantity = tband_data["band_quantity"]
  energys = tband_data["energys"]
  orbits = pband_data["project_orbit"]
  weight = pband_data["weight"]
  ## Design the Figure
  # Set the Fonts
  plt.rcParams.update({'font.size': 14,
                       'font.family': 'STIXGeneral',
                       'mathtext.fontset': 'stix'})
  # Set the spacing between the axis and labels
  plt.rcParams['xtick.major.pad']='6'
  plt.rcParams['ytick.major.pad']='6'
  # Set the ticks 'inside' the axis
  plt.rcParams['xtick.direction'] = 'in'
  plt.rcParams['ytick.direction'] = 'in'
  # Create the figure and axis object
  fig = plt.figure()
  band_plot = fig.add_subplot(1, 1, 1)
  # Set the range of plot
  x_min = 0.0
  x_max = hsk_corrdinate_list[-1]
  y_min = min_plot_energy
  y_max = max_plot_energy
  plt.xlim(x_min, x_max)
  plt.ylim(y_min, y_max)
  # Set the label of x and y axis
  plt.xlabel('')
  plt.ylabel('Energy (eV)')
  # Set the Ticks of x and y axis
  plt.xticks(hsk_corrdinate_list)
  band_plot.set_xticklabels(plot_hsk_symbol_list)
  # Plot the solid lines for High symmetic k-points
  for kpath_index in range(kpath_quantity+1):
    plt.vlines(hsk_corrdinate_list[kpath_index], y_min, y_max, 
                colors="black", linewidth=0.7, zorder=3)
  # Plot the fermi energy surface with a dashed line
  plt.hlines(0.0, x_min, x_max, colors="black",
             linestyles="dashed", linewidth=0.7, zorder=3)
  # Plot the Band Structure
  for band_index in range(band_quantity):
    x = kpoints_corrdinate_list
    y = energys[0][band_index]
    band_plot.plot(x, y, '-', color='red', linewidth=0.6)
  if spin_num == 2:
    for band_index in range(band_quantity):
      x = kpoints_corrdinate_list
      y = energys[1][band_index]
      band_plot.plot(x, y, '-', color='blue', linewidth=0.6)
  if plot_args['project_atoms'] != '':
    for orbit_index in range(len(orbits)):
      orbit = orbits[orbit_index]
      up_color = 0.36 ** ((orbit_index+1) * math.pi)
      up_color = '#' + up_color.hex().split('.')[1][0:6]
      band_plot.scatter([], [], s=10, c=up_color, label='up %s'%orbit)
      if spin_num == 2:
        dn_color = 0.88 ** ((orbit_index+2) * math.pi)
        dn_color = '#' + dn_color.hex().split('.')[1][0:6]
        band_plot.scatter([], [], s=10, c=dn_color, label='dn %s'%orbit)
      for band_index in range(band_quantity):
        x = kpoints_corrdinate_list
        y = energys[0][band_index]
        area = []
        for kpoint_index in range(plot_kpoints_quantity):
          w = weight[0][band_index][kpoint_index][orbit]
          area.append(4 * math.pi * (w**2) * plot_point_size)
        band_plot.scatter(x, y, s=area, c=up_color)
      if spin_num == 2:
        for band_index in range(band_quantity):
          x = kpoints_corrdinate_list
          y = energys[1][band_index]
          area = []
          for kpoint_index in range(plot_kpoints_quantity):
            w = weight[1][band_index][kpoint_index][orbit]
            area.append(4 * math.pi * (w**2) * plot_point_size)
          band_plot.scatter(x, y, s=area, c=dn_color)
    plt.rcParams.update({'legend.handlelength':0.1})
    band_plot.legend(prop = {'size':8})
  # Save the figure
  plot_band_file_name = plot_filename + '.' + plot_format
  plt.savefig(plot_band_file_name, format=plot_format, dpi=plot_dpi)
  return 0


def main():
  """Main function"""
  check_python_version()
  plot_args = get_command_line_input()
  plot_filename = plot_args["plot_filename"]
  plot_format = plot_args["plot_format"]
  print("[do] Reading the kpath info...      <== (KPOINTS, OUTCAR)")
  kp_data = read_kpath_info(plot_args)
  print("[do] Reading the total band...      <== (EIGENVAL)")
  kp_data, tband_data = read_tband(plot_args, kp_data)
  if plot_args['project_atoms'] != '':
    print("[do] Reading the projection band... <== (PROCAR, POSCAR)")
    project_atoms = check_project_input(plot_args['project_atoms'])
    pband_data = read_pband_data(plot_args, kp_data, project_atoms)
  else:
    pband_data = {"project_atoms":[], "project_orbit":[], "weight":[]}
  print("[do] Recording the band data...     ==> (%s.json, %s.txt)" \
        %(plot_filename, plot_filename))
  store_band(plot_args, kp_data, tband_data, pband_data)
  if not plot_args["no_plot"]:
    print("[do] Plotting the band...           ==> (%s.%s)"\
          %(plot_filename, plot_format))
    plot_band(plot_args, kp_data, tband_data, pband_data)
  return 0


if __name__ == "__main__":
  main()
