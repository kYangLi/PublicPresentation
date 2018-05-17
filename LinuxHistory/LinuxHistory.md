# 计算物理讨论班---第一次. 
# Linux系统的安装和使用

## Linux系统的历史
### 1969年之前, Multics
早期计算机编程使用纸带和打卡机完成, 编程周期极长且由于计算机一次只能跑一个程序,所以计算机资源十分有限. 大部分时间都花在排队等待上.   

CTSS横空出世, 兼容分时系统, 给人以"计算机可以同时跑多个程序的错觉".("终端"概念出现)  

但此时, 即使是有了终端的概念, 计算资源也十分有限, 因为即使是当时最先进的计算机, 能带的动的终端上限也就是不到30个.

为了进一步发掘计算资源, 1965年(文革), Bell实验室,MIT,  奇异公司(GE, 或称为美国通用电气公司)一起发起了名为"Multics"计划. 该计划的目标是让一台主机又能力支持300个以上的终端. 但是, 由于各种原因, 1969年Bell实验室不堪重负, 退出计划.

后来,虽然Multics成功研制出来, 但是该项目也并没有引起社会的太多关注, 倒是在该计划中培养出了一大批优秀的计算机人才.

### 1969年, Ken Thompson 的 file server system
虽然认定了Multics计划不可能成功的Bell实验室退后该计划, 但原本参与计划的大佬"Ken Thompson"却从Multics计划中获得了一些灵感.

此时Thompson正沉迷于一款名为<太空旅游>的游戏. 但该游戏无法再他的机器上--- DEC公司开发的PDP-7上运行.又正赶上他的妻子去美西探亲, 于是, Thompson有了一个月的单身时间. 

因此, 这一个月内, 他起早贪黑, 不断奋斗, 最终以汇编语言Assembler写出了一组核心程序, 以及一些核心工具程序,和一个小小的文件系统.(玩没玩上<太空旅游>?你说呢...) 

这个小小的文件系统被他的同事们戏称 Unics, 因为他更像是一个微缩版简化版的Multics系统.

这个被同事们称为"Unics"的文件系统由两个特点:

* 所有的程序和系统都是文件, 驱动硬件也是!
* 不管建构编辑器还是附属文件, 所写每个程序只有唯一的目的, 且要有效的完成目标.

这两点深深的影响到了后来的Linux系统.

### 1973年(文革结束,快了)

Thompson写的程序太好用了!导致其在Bell 实验室 风靡一时. 唯一的缺点是它是由汇编语言写成的, 而汇编语言具有专一性, 也就是对于不同构架的计算机, 所使用的汇编语言语法是完全不同的! 也就是说, 你兴高采烈的买回来一个最新款的服务器, 却发现用不了最好用的系统. 只能自己动手按照源码重构语言....

因此, Thompson与Ritchie合作想将Unics用高级语言写出来. 这样就可以极大地提高程序的兼容性.

然而...当时现成的语言只有B语言, 但是用B语言编出来的Unics性能很差, 不再像以前那么好用了....

因此, 大佬Ritchie一气之下将B语言改造为C语言, 再用C语言编译Unics核心. 这个版本的Unics不在叫Unics了, 而改名为"UNIX".  

于是, 到此为止, 传奇的Unix系统和C语言就这样诞生了.

Bell实验室是隶属于AT&T的.AT&T的毕竟是一个商业公司, 以商业活动为主. 自己旗下的Bell实验室一群工程师搞了个什么Unix系统, 据说起源还是一个什么 太空旅游 的游戏, 好好的B语言不用, 还弄了个什么C语言. 感觉也没啥意思, 但同底下其他工程师反映,这貌似确实干的是正事, 也没对公司有什么负面影响. 所以AT&T对Unix系统诞生也不排斥也不鼓励. 意思就是这个所谓的Unix我们也不管了,爱咋咋地, 自生自灭. 有了好处, 都是公司的, 闯了祸就你们自己担着.

而对于一般吃瓜群众呢? Bell实验室都是计算机大佬, 一群大佬张牙舞爪地声称他们搞出了一个很好用的程系统, 还是用一种自己完全没有见过的, 所谓的C语言编写的. 这正常人一听头就大了, 因此一时间,很多人都不接受这个系统.

但是对于学术界, Unix真可谓是 研究人员的一波福利! 因为这段程序是开放的, 可以任意改写并做学术之用. 直接汲取C语言创始人的智慧, 这是多么珍贵的一段代码!

伯克利大学的Bill Joy 在取得了Unix源码之后, 对其进行一系列改造,最终形成了Unix系统的一个重要分支系统 Berkeley Software Distribution (BSD)

AT&A也发展了自己的Unix系统 system V

此时所有的 Unix均只支持服务器和大型工作站.

### 197AT&T的版权宣告(改革开放&对越自卫反击战)
Uinx出现后, 以一种迅速的态势发展, 也来越火爆.AT&T公司一见如此态势. 立刻推出system V 7.0 将个人计算机上装入Unix系统, 并特别声明了该版本的Unix系统"不得对学生提供源码!"

### 1984年 Minix

AT&T公司的版权宣言可苦了正在修相关课程的老师和学生. 自己听说有一个很强的系统, 想来学一学. 可是课程上到一半突然说不能提供源码了! 这咋办(盗版? 美帝的版权意识个法律可是相当健全和完善的...) 没事!是所谓的Unix不也是某个大佬搞的么...我们学校没有个能赶上那个大佬的更强大佬?

有的!

谭宁帮教授为了解决学生的上课问题, 自己完全独立的(也就是不看Unix源码, 从零开始)编写了一个名为Minix的系统, 用了两年时间, 终于完成!

然而...   

这个由于Unix有版权声明而做出来的Minix并不是免费的...虽然还是很便宜的...

另外值得一提的是...

这个程序的源码是装在磁带中的...

而且, 由于Minix只是做学术学习只用, 很多地方都是点到为止. 实用性并不是很大.

### 还是1984年 GNU计划

还是一个大佬 Stallman. 18岁就进入著名的人工智能实验AI LAB.
后来人工智能实验室解体, 斯托曼的雄心壮志并未结束.
斯托曼认为, 写程序的最大乐趣在于自己编写的有软件能够给大家由良好的使用体验.既然程序是分享给大家使用的, 但每个人的计算机有可能不同, 所以程序的源码应该与程序一同发布!
也就是说, 你写程序不仅仅是分享用程序的快乐, 还要分享你编程序是后的喜怒哀乐.
这就是自由软件(FreeSoftware)运动(注意不是免费软件哦!)

而且, 如果你释出源码, 加上你的软件很好用,那么就会有更多的人来帮你修改, 你的软件会越来越强, 流芳百世也不是没有可能.

1986年 斯托曼开始自己的GUN计划.  
GUN计划很简单: 建一个开放自由的Unix操作系统.  
也就是和Minix性质差不多, 但是这个更专业.  
但是一个人想反对整个世界!谈何容易.  
于是, 斯托曼采用了曲线救国的策略.  

他先是编写了一个Unix上相当给力的编辑软件Emacs(即使是现在也是这样). 大获成功! 一个小软件还是难不倒一个计算机大师的. Emacs实在是太好用了! 很多人都直接联系斯托曼索要Emacs软件, 并提供了一笔可观的购买款. 斯托曼借着出售Emacs的磁带大赚了一笔, 并有更多时间和精力去实现自己的GNU计划了.

期间, 斯托曼又完成了另一壮举, 1990年左右, 他成功写出了GCC这一c语言编译软件.
至此, GNU的名声大噪

### 1991年 Linux!
Linus Torvalds
芬兰大学的 托瓦兹 同学在校内BBS上发表了一篇公告
说他抱着用Minix在386机器上玩一玩的心态编写了一个操作系统, 并不是像GNU那样伟大计划.但希望有大神的话可以带他一起玩.

由于托瓦兹存放在网站上存放文件的位置叫 Linux   
所以, 以后的大家就都把这个小小的操作系统叫做Linux了!

后来, Linux就像滚雪球一样,越来越大, 参与修改的人员越来越多. 核心也越来越健全.

而另一方面, GNU的创始人斯托曼也注意到了这个小小的荷兰学生托瓦兹所写的Linux. 这让他眼前一亮!因为GNU计划就是缺一个核心程序!

之后GNU的大多数软件都以Linux为平台制作开发. 有了GNU强大名声的支持, Linux的名望也越来越大

后来一些公司直接将Linux核心加那些支持Linux的软件打包做成成套的安装系统. 成为完全安装套件.这些套件大都是以卖服务盈利为主.

Ubuntu就是其中之一.

## Linux VS Windows
1. Windows下系统崩了,你要骂微软; Linux下系统崩了你只能骂自己

2. 是免费的
 "可以用盗版windows啊!不一样么...我们都是为了学术啊!"  
 "这 话 你 留 着 跟 法 官 去 说!"

3. 自定义极高   
 嘿嘿, 哪天不高兴可以试一试, 嘿嘿嘿
```shell
su rm -rf /
```
4. 完全不用担心病毒什么的

5. 删除程序文件 真的只用 删除程序文件  
***萌新三连:残余文件呢?注册表呢?历史记录呢?(ﾟДﾟ≡ﾟдﾟ)!?***  
***大佬三连:没有!不存在的!已经删啦!（￣▽￣）***  
***蠢萌三连:怎么回事,怎么搞的,我要学._(:3」∠)_***  

6. 不用担心内存泄漏.  
"老夫的电脑, 连续开机两月不卡"

7. 用apt-get安装大多数软件(Mac使用homebrew)    
"windows上的latex怎么安啊!看教程好麻烦啊....官网在哪....用迅雷下载安装包么   
.....镜像怎么打开, 哪个是安装程序啊! .bat么?什么"_lt"啊?啊!!!!要崩溃了!"    
"关上windows, 打开Ubuntu, 打开终端......对打开! 然后复制这个输进这个, 输进去!
```
sudo apt-get install texlive-full
```
你只管输进去就行了, 按回车, 按下去.   
再问...那啥!"   
"哇, 程序安好了耶!"

8. 不能玩大多数游戏  
 "你不是说要戒游戏吗?给你机会!"

9. 从来不用磁盘整理,垃圾清理之类的    

"什么?怎么清理垃圾?微软和360共同训练出来的强迫症吧..."

10. 编程效率极高  
"说了咋还不信呢...不信自己写一段C程序用gcc编译编译跑一跑"

11. 说吧, 还用不用谷歌学术了, Youtube清单里的视频还看不看了

12. 有很大几率能体验到成就感   
"大家都来登录我刚写的网站啦!支持文献整理分享和WolframAlpha啦!"

13. 不适合行政办公和娱乐  
"什么? 怎么打开这个flv视频文件? 这位同学,我们现在讨论的是学术问题!"

**!!!特别注意!!!**  
14. 有一定几率会让你吃上官司! 如果你一开始学Linux的时候就满脑子想着搭站做网页这样的大新闻, 而自己又不是老司机又没有老司机指导...     
"什么?我的服务器被警告了! 原因是蓄意攻击索尼在东京的R4服务器, 什么鬼..."

## Linux 的文件系统
```
   /bin 二进制可执行命令
   /boot 存放系统启动所必须的文件
　　/dev 设备特殊文件
　　/etc 系统管理和配置文件
　　/etc/rc.d 启动的配置文件和脚本
　　/home 用户主目录的基点，比如用户user的主目录就是/home/user，可以用~user表示
　　/lib 标准程序设计库，又叫动态链接共享库，作用类似windows里的.dll文件
　　/sbin 系统管理命令，这里存放的是系统管理员使用的管理程序
　　/tmp 公用的临时文件存储点
　　/root 系统管理员的主目录（呵呵，特权阶级）
　　/mnt 系统提供这个目录是让用户临时挂载其他的文件系统。
　　/lost+found 这个目录平时是空的，系统非正常关机而留下“无家可归”的文件（windows下叫什么.chk）就在这里
　　/proc 虚拟的目录，是系统内存的映射。可直接访问这个目录来获取系统信息。
　　/var 某些大文件的溢出区，比方说各种服务的日志文件
　　/usr 最庞大的目录，要用到的应用程序和文件几乎都在这个目录。其中包含：
　　/usr/X11R6 存放X window的目录
　　/usr/bin 众多的应用程序
　　/usr/sbin 超级用户的一些管理程序
　　/usr/doc linux文档
　　/usr/include linux下开发和编译应用程序所需要的头文件
　　/usr/lib 常用的动态链接库和软件包的配置文件
　　/usr/man 帮助文档
　　/usr/src 源代码，linux内核的源代码就放在/usr/src/linux里
　　/usr/local/bin 本地增加的命令
　　/usr/local/lib 本地增加的库
```
SWAP分区: 虚拟内存  
绝对路径和相对路径  
隐藏文件

## Linux的安装
1. 准备好一个USB安装镜像  
  (软碟通)
2. 分出一块磁盘空间  
  (PE或是其他更正规的方法)
3. 关机开机F2安装  

## Linux 的使用

1. 几个基本的命令
```
cd
cd ../../../../../
ls 
ls -all
ll
rm 
rm -r 
mv 
cp
mkdir

alias

vim
cat
tail
./    
echo $PATH

sudo 
apt_get
wget
chmod +x

pwd
top
htop

sl
cowsay
cowthink
fortune

ssh
scp
ping

man
info

gcc
python
gnuplot
xelatex

mount
unmount

....and more...
```
会用"TAB"键...

## 如何正确使用Man 
***
 ***有困难? 多找Man!***

***
### man page 边角的数字的意义
|代号|代表内容|
|----|----|
|1|用户在SHELL环境中可以操作的指令或可执行文件|
|2|系统核心可呼叫的函数与工具|
|3|一些常用的函数和依赖包, 多为C语言的依赖包|
|4|硬件文件的说明, ,通常是在/dev下的文件|
|5|配置文件或者是某些文件的格式|
|6|游戏|
|7|惯例与协议|
|8|系统管理员可执行的管理指令|
|9|和系统核心有关的文件|

### man page 的基本结构
|名称|内容说明|
|----|----|
|NAME|十分精简的指令和数据名称的说明|
|SYNOPSIS|简短的语法介绍|
|DESCRIPTION|完整的说明|
|OPTIONS|针对SYNOPSIS部分中[OPTIONS...]选项的说明和列举|
|COMMANDS|在这个程序中可以调用的指令|
|FILES|这个程序或者参考位于哪个文件中|
|SEE ALSO|可以参考的, 其他与此指令有关的指令|
|EXAMPLE|一些例子|
|BUGS|此程序的BUG|
|AUTHORS|此程序的作者|
|COPYRIGHT|此程序的版权信息|

对于一个给定的指令的man page 并不是一定包含上述的所有结构

### 几个编辑器的讲解

vim  
vscode  
emacs  

### 讨论班的工具

1. 服务器
2. GitHub
3. GoogleGroups


# Latex初步

## Word的糟糕体验

不知道在座的有没有尝试过用word插入图片 (°∀°)ﾉ

又或者是用word插入表格（#-_-)┯━┯

或者是公式(╯°口°)╯(┴—┴

当然还有....(￣ε(#￣) Σ

## 游戏的来历

1. 高纳德 Tex《计算机程序设计艺术》 "泰赫"
2. LaTeX "拉泰赫" 或 "雷泰赫"

目前我们使用的是LaTeX

## 优缺点

### 优点

1. 使你的作品更像排版专家的手笔
2. 强大的数学公式编辑能力
3. 只需掌握极为基本的语法就可以满足一般要求
4. 强大的扩展性, usepackage
5. 能敦促和帮助您的写出结构清晰的文档
6. 开源免费的FreeSoftWare

### 缺点 

1. 易学难精
2. Debug, 程序员的阴影
3. 很难写出格式自定义很强的文章
4. 您需要不停地编译来查看文章的效果.

## 名词的解释

tex, latex, xetex, xelatex, texlive, ctex, pdftex, pdflatex
到底都是什么东西?

再解释这些名词之前, 先要再引入几个名词:

* 引擎: 俗称编译器, 意为把用户写的语言转化为计算机可以识别并执行的程序, 不同的引擎实用性工作原理都略有不同

* 格式/宏集: 也就是一组指令集, 因为TeX本身只有300个命令, 有时候打一个特殊字符都需要若干命令的组合, 因此, 直接将这些命令打包, 做一个宏集是十分必要的.   

* 命令: 上述两个东西的组合体, 之所以叫"命令", 是因为这就是在终端直接调用的东西

* 宏包: 依赖包, 之所以区别于格式, 是因为宏包只是辅助作用, 它本身并不成体系.

* 发行版: 打包完善的应用程序

目前, 格式主要有两种: plain TeX, LaTeX
引擎主要有三种: TeX, pdfTeX, XeTeX

其相互组合, 可生成6种命令:

||plainTex格式|LaTeX格式|
|---|----|-----|
|TeX引擎|tex|N/A|
|pdfTeX引擎|etex|latex|
||pdftex|pdflatex|
|XeTeX引擎|xetex|xelatex| 


较为常用的宏包: xeCJK, enumerate, mathams...  
较为流行的发行版: 
* TeXLive: 支持Linux, MacOS, Windows 
* MiKiTeX: 支持Windows
* CTeX: 基于MiKiTeX, 对中文的支持做了更好的封装.

## 命令的使用

### latex

使用latex命令: 
```
latex demo.tex
```
会生成一个`demo.dvi`的文件  
在Linux下您可以使用`xdvi`命令将其打开, 即
```
xdvi demo.dvi
```

Windows下latex软件包大多数都预装了yap软件, 直接双击就可以打开`.dvi`文件  
要进一步生成的当前流行的PDF格式文件, 还需要将`.dvi`文件转换为`.pdf`文件  
```
dvipdfmx demo.dvi
```

然后您就可以查看您的PDF文档了!

* 不难发现, 如此编辑pdf文件真的是要多麻烦有多麻烦...

### pdflatex 和 xelatex

上述两个命令可以略过生成`.dvi`文件的过程, 直接生成`.pdf`文件.

尤其是xelatex, 对中文支持及其优秀, 推荐大家食用!!

## latex中的文件类型及其意义

### 用到的文件
|后缀|意义|
|---|---|
| .sty| 宏包文件, 宏包名称即为去掉.sty后的文件名|
| .cls| 文档类文件, 命名规则与宏包相同|
| .bib| 参考文献的数据库文件|
| .bst| 用到的参考文献的格式的模板|

### 生成的文件
|后缀|意义|
|---|---|
|.log |日志文件, 记录编译过程, 供排错使用|
|.aux |主要的辅助文件, 用于记录目录, 交叉引用, 参考文献引用等|
|.toc |目录文件|
|.lof |图片目录记录文件|
|.lot |表格目录记录文件|
|.idx |供makeindex处理的索引记录文件|
|.ind |makeindex处理.idx后生成的格式化索引记录文件|
|.out |hyperref宏包生成的PDF书签记录文件|
|.blg |bibtex的日志文件|
|.bbl |bibtex的参考文献记录文件|

注:
很多长篇科技著作在正文之后都附有词汇索引, 以便读者查阅所关心部分的论述.
makeindex是可生成索引的标准 LaTeX 宏包，它能将指定的词汇以及出现在正文中的页码，按字母顺序列于指定位置. 源文件在第一次编译时，自动生成一个索引条目和页码信息文件*.idx，然后运行工具程序 `makeindex` 对其编译，再自动生成一个与源文件同名的排序索引文件*.ind，当再次编译源文件时， \printindex 命令将被这个文件的内容所取代.

## LaTeX文件编辑格式

### 程序语言的声明
* 使用`\`表明之后跟的不是普通字符, 而是一个程序语言

### 文档类和宏包

#### 文档类
在.tex编辑的第一行, 一般都是这样的形式
```latex
\documentclass[<option1>,<option2>,...]{class-name}
```
这就是传说中的文档类  
其中, class-name是文档类的名称
其主要有一下几种
|class-name|具体意义|
|---|---|
|article|用于写论文或短篇说明文档|
|report|用于写长篇报告,长篇论文, 简单的书籍等, 有章节结构|
|book|用于书写书籍, 文档结构复杂且严密, 有前言, 正文, 后记等结构|
|proc|基于article的简单学术文档模板|
|slides|用于制作幻灯片, 使用无衬线字体|
|minimal|极其精简的文档类, 一般用于测试代码|

\<option1>, \<option2>, ... 被称为可选参数,   
他可以指定纸张的大小, 字号, 
|\<options>|意义|
|---|---|
|12pt|指定文档的基本字号为12pt, 默认为10pt|
|a4paper|指定打印纸张为A4纸|
|fleqn|行间公式右对齐, 默认为居中|
|leqno|公式编号放在左边, 默认右边|
|twocolumn|双栏排版, 默认为单栏|
|twoside|纸张双面印刷排版, article和report默认为单面, book默认为双面|
|landscape|横向排版, 默认为纵向|

#### 宏包
紧接着下一行, 您一般会看到一下命令
```
\usepackage[<option1>, <option2>, ...]{package-name}
```

或更常见的写作:
```latex
\usepackage[<option1>, 
            <option2>, 
            ...]{package-name}
```

不同的宏包一般提供了不同的功能, 您可以通过
```
texdoc package-name
```
命令来查看该宏包的具体说明文档

常用的宏包:
|package-name|说明|
|---|---|
|xeCJK|用于支持中文, 要用xelatex编译|
|hyperref|用于自定义引用脚注等的格式和样式|
|enumerate|list常用的宏包|
|geometry|用于设置页面的更具体的属性|
|amsmath|用于编辑公式|
|graphicx|图片的插入环境|
|float|浮动图片的支持|

### 设置标题和其他内容
在声明了调用宏包之后, 在开始正式码字之前, 可能您还需要一些其他的设置, 比如:
* 设置文章的题目,作者和文章日期信息. 文章的题目是文章的一个重要部分, 如果只是在正文中用加大字号和加粗字体的方法来表明这就是题目, 未免太不正式了!
* 设置简单的宏指令, 或者简化指令
* 设置文档的整体布局
* 修改某些指令的默认参数, 比如 将图片标签默认显示的'Fig.1'改成'图1'
* ...

其中题目, 作者, 日期的设置:
```
\title{article-title}
\author{your-name}
\date{date}
```
而后在正文中使用命令
```
\maketitle
```
就可以显示文章的题目, 作者和日期了.

值得注意的是, 如果您不设置日期, 其会默认显示当前日期, 如果您不想显示日期, 只需将日期设置为空即可!  
也即
```
\date{}
```

### 文章主体
文章主体需要一个声明, 要理解这个声明, 首先要理解一个名为'环境'的东西.

环境可以理解成一个图层, 特殊的内容只有在特殊的图层上才可以被理解.图层可以摞在一起!  声明环境的语句十分简单
```
\begin{env-name}
  ...
\end{env-name}
```
中间...部分即为受该环境支持的部分.

如果您要开始编辑文本了, 那么首先需要使用`document`环境!  
也即
```
\begin{document}

\end{document}
```
还有其他几个常用的环境:
|env-name|作用|
|---|---|
|document|文章环境, 可以往上码字的地方|
|figure|图片环境|
|equation|公式环境, 需要masmath宏包的支持|
|tabular|表格环境|
|verbatim|代码环境|

### 导言区
 从`\documentclass[a4paper]{article}`到`\begin{document}`
 之间的部分被称为'导言区'!

### 大文档的格式
大文档的编辑一般用`\include`指令, 即, 将要编辑的内容分别储存在若干个子文件里,
在主文件中使用
```
\include{<filename>}
```
 指令就可以将子文件中的内容加载到主文件中进行编译.

您还可以在导言区中加入
这样一来, 不但问价结构清晰, 而且排错和修改内容也会变得极为方便.  
```
\includeonly{<filename1, filename2, ...>}
```
来限制在正文中`\include`的文件的范围.

## PDF文章的结构控制

### 标题

在导言区使用
```
\title{...}
\author{...}
\date{}
```
在文章主体中使用
```
\maketitle
```
即可完成标题的编辑

### 摘要
一般摘要应紧跟在标题后
摘要环境只适用于`article`与`report`

```
\begin{abstract}
...
\end{abstract}
```


### 章节

```
\part{<title>}
```
将文章书籍等分成若干大的部分(如, 上下册)

```
\section{<title>}
\subsection{<title>}
\subsubsection{<title>}
\paragraph{<title>}
\subparagraph{<title>}
```
不同层次的章节分层命令, 高层可嵌套低层, 例如
```
\section{水果}
  \subsection{橙子}
    \subsubsection{美国甜橙}
      .....
    \subsubsection{中国甘橙}
      .....
  \subsection{梨}
    ....
\section{肉类}
  \subsection{牛肉}
    ....
  \subsection{鱼肉}
    ....
```

### 目录
```
\tableofcontents
```

### 脚注

```
\footnote{.....}
```

### 交叉引用

```
....
\label{label-name}
....
....
....
\ref{label-name}
....
```

## 书写文本的基本语法

### 正常文字内容

正常在`document`环境中书写即可.但有一下几点需要注意!

* 要书写中文最好使用xelatex编译, 并需在导言区声明:
```
\usepackage{xeCJK}
```
* 一个空格和多个空格的效果一样
* .tex中单个换行只会产生一个空格, 多个换行会产生一个空行
* 文章强制换行使用`\\`, 此换行不产生缩进
* 使用`{}`隔开程序语言与普通文字
```
Sh\"o{}rdinger
```
* 使用`\par`产生新的段落

### 注释

```
% 这是一个注释
```

### 列表

使用`enumerate`环境产生一个列表  
次环境需要`enumerate`宏包的支持  

具体用法:
```
\begin{enumerate}[1.]
  \item you have lost
  \item you win
  \item finally, we find this staff!
\end{enumerate}
```

列表环境可嵌套使用!

### 引用

使用 `quote`环境

```
He said:
\begin{quote}
  I am your Father!
\end{quote}
```

### 代码

```
\begin{verbatim}
#include<stdio.h>

int main(void){
  printf("Hello!\n");

  return 0;
}
\end{verbatim}

```

行内代码引用可以使用:
```
\verb|printf|
```
需要注意的是, `\verb|..|`命令一般不可以包含在其他命令内部

### 表格 

表格需要使用`tabular`环境
```
\begin{tabular}{r|c|l|...} 
  ⟨item1⟩ & ⟨item2⟩ & ... \\
  \hline
  ⟨item1⟩ & ⟨item2⟩ & ... \\ 
\end{tabular}
```
更多内容参考[一份不太简短的LaTeX2e介绍](https://mirrors.tuna.tsinghua.edu.cn/CTAN/info/lshort/chinese/)

### 图片

图片需要调用`graphicx`的支持. 

在调用了`graphicx`宏包后, 直接使用语句
```
\includegraphics[<options>]{file-path-name}
```
就可以调用图片了!

对于不同版本tex, 该命令一般支持的图片格式不同.  
以xelatex为例,  
其支持的图片格式有:
* .pdf
* .eps 
* .jpg
* .png
* .bmp

`\includegraphics`命令的options有如下几个:

|选项|含义|
|---|---|
|width=2cm|图片宽度, 2cm|
|height=3cm|图片高度, 3cm|
|scale=1.0|图片缩放比例, 1倍|
|angle=90|图片旋转角度, 90度|
 
### 浮动体
内容丰富的文章或者书籍往往包含丰富的图片和表格等内容。这些内容的尺寸往往太大，导 致分页困难。LaTeX为此引入了浮动体的机制，令大块的内容可以脱离上下文，放置在合适位置.  

浮动体主要有`figure`和`table`两种环境  

习惯上 figure 里放图片，table 里放 表格，但并没有严格限制，可以在任何一个浮动体里放置表格.

两种环境的用法完全一样, 以`table`为例:
```
\begin{table}[<options>]
\end{table}
```

|选项|含义|
|---|---|
|h/H|允许/只能在当前位置插入|
|t|允许在顶部|
|b|允许在底部|
|p|单独成页|

如:
```
\begin{table}[hpb]
  \centering
  ...
  ...
  ...
  \caption{...}
\end{table}
```

更多内容参见: [一份不太简短的LaTeX2e介绍](https://mirrors.tuna.tsinghua.edu.cn/CTAN/info/lshort/chinese/)

## 公式的书写

AMS宏集, 基本上可以满足所有的数学需要.


### 公式环境
行间公式:
```
\begin{equation}

\end{equation}
```

行内公式:
```
$\hbar\omega = E_n - E_m$
```

$\hbar\omega = E_n - E_m$

### 公式中的普通文本
### 巨算符
### 字符附加符
### 特殊符号和字母/字符控制
### 公式编号
### 多行公式
### 大括号, 分段函数
### 矩阵和数组
### 证明环境

## 字体样式设计
详见: [一份不太简短的LaTeX2e介绍](https://mirrors.tuna.tsinghua.edu.cn/CTAN/info/lshort/chinese/)

## 参考文献的引用

### 一般latex小白的做法
```
\documentclass{article}

\begin{document}

  \section{Introduction}
    Partl~\cite{pa} has proposed that \ldots

  \begin{thebibliography}{99}
    \bibitem{pa} H.~Partl: \emph{German \TeX}, TUGboat Volume~9,Issue~1 (1988)
  \end{thebibliography}

\end{document}
```

### 真正的科研工作者的做法
  
  bibtex + xelatex

  为了使用高级的引用参考文献的方法, 你需要学习两个文件的写法:
  * .bst 定义了参考文献引用的格式
  * .bib 参考文件数据库

 下面是一则`liyangbook.bib`文件示例
  ```
  @book{Lamport1994,
  title = {{\LaTeX}: A Document Preparation System},
  author = {Lamport, L.},
  publisher = {Addison-Wesley},
  address = {Reading, Massachusetts},
  year = {1994},
  edition = {2nd}
}
@book{Mittelbach2004,
  title = {The {\LaTeX} Companion},
  author = {Mittelbach, F. and Goossens, M. and
  Braams, J. and Carlisle, D. and Rowley, C.},
  publisher = {Addison-Wesley},
  address = {Reading, Massachusetts},
  year = {2004},
  edition = {2nd}
}
```
下面为实际引用的在`demo.tex`中的形式!
```
\documentclass{article}

\bibliographystyle{plain}

\begin{document}
  \section{Some words}
    Some excellent books, for example, \cite{Lamport1994}
    and \cite{Mittelbach2004} \ldots

  \bibliography{liyangbooks}
\end{document}
```
注意: `\bibliographystyle` 和 `\bibliography` 命令缺一不可  
`\bibliography`实际上是替换了原先的`thebibliography`
将demo.tex编译为demo.pdf步骤
1. 首先使用 pdflatex 或 xelatex 等命令编译 LATEX 源代码 demo.tex;
2. 接下来用 bibtex 命令处理 demo.aux 文件记录的参考文献格式、引用条目等信息。bibtex 命令处理完毕后会生成 demo.bbl 文件，内容就是一个 thebibliography 环境;
3. 再使用 pdflatex 或 xelatex 等命令把源代码 demo.tex 编译两遍，读入参考文献并正确 生成引用。

实际执行过程中
```
pdflatex demo
bibtex demo
pdflatex demo
pdflatex demo
```

## 其他扩展功能

### makeindex
### `\color`
### hyperref 宏包
### tikz 宏包画图(非主流用法)

## 自定义LaTeX

### 自定义命令
命令的形式
```
\newcommand{\⟨name⟩}[⟨num⟩]{⟨definition⟩}
```
具体的使用方法
```
\newcommand{\txsit}[1]
 {This is the \emph{#1} Short
      Introduction to \LaTeXe}
% in the document body:
\begin{itemize}
\item \txsit{not so}
\item \txsit{very}
\end{itemize}
```

### 自定义环境
命令的形式
```
\newenvironment{⟨name⟩}[⟨num⟩]{⟨before⟩}{⟨after⟩}
```
具体使用方法
```
\newenvironment{king}
{\rule{1ex}{1ex}%
     \hspace{\stretch{1}}}
{\hspace{\stretch{1}}%
     \rule{1ex}{1ex}}
\begin{king}
My humble subjects \ldots
\end{king}
```
在 ⟨before⟩ 中的内容将在此环境包含 的文本之前处理，而在 ⟨after⟩ 中的内容将在遇到 \end{⟨name⟩} 命令时处理。

### 自定义宏包

`⟨package name⟩.sty`文件  
在文件第一行  需要有
```
\ProvidesPackage{⟨package name⟩}
```
如果在自己定义的宏包中要调用其他宏包:
```
\RequirePackage[⟨options⟩]{⟨package name⟩}
```
### 编写自己的文档类
不会, 大家自己学习

### 计数器等其他很不常用的内容...


# MarkDown的编写

MarkDown是一款html向的文本编辑组件

其最大的优势在于对html的完全兼容性

下面将实际介绍如何优雅的使用MarkDown

## 标题系统

## 换行

## 重点标记

## 列表

## 超链接

## 图片

## 表格

## 分割线

## 代码

## 转义字符

## 公式??

## 和HTML完全兼容

# vscode, vim 和 Emacs

## vscode
vscode的设置

## Vim
Vim文件操作模式的转化

## Emacs
???

实际操作体验
