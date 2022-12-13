#%%
# +---------------+
# | Comments Rule |
# +---------------+
### e.g. 1
# Set the person name (x?v?)
person_name = 'ted'
# Set the person name (x?v?)
pn = 'ted'

### e.g. 2
# Let the person_age equal to 100 (x)
person_age = 100

### e.g. 3
#[1] Print the name and age to the screen (x)
#[2] Let the user check their info. (v)
#[3] <do not write any comment> (v)
print_str = "[info] %s is %d years old..." %(person_name)
print(print_str)

### e.g. 4
# Function Definition Part (v)
def input_user_info():
  """Let the user (re)input their info."""
  pass #TODO

kk = 1
h = 0
#%%
import sys
import math
# +---------------------+
# | Variable Names Rule |
# +---------------------+
### e.g. 1
total_fail_times = 10 #(v)
tft = 10 #(x)
total_fail_numbers = 10 #(x?v?)

### e.g. 2
if_the_total_fail_time_more_that_10_then_this_var_turn_to_true = False #(x)
too_many_fails = False # If more than 10, then turn this var to True. (v)
tmf = False #(x)

# If too many fails, then exit the program
if too_many_fails:
  sys.exit()

### e.g. 3
# The following variables agree with the notes in: https://www.somesome.com/notes.pdf
i = 1
phi = 30 # unit in degree
theta_i = calc_theta(phi, i) # unit in pi
H_ij = S_j * math.sin(theta_i)

#%% 
# +----------------------+
# | Function Define Rule |
# +----------------------+
# See the Slides...
