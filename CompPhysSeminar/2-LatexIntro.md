# # 计算物理讨论班[第二次]: LaTeX初步

## Word的糟糕体验

不知道在座的有没有尝试过用word插入图片 (°∀°)ﾉ

又或者是用word插入表格（#-_-)┯━┯

或者是公式(╯°口°)╯(┴—┴

当然还有....(￣ε(#￣) Σ

## LaTeX的来历

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

```bash
latex demo.tex
```

会生成一个`demo.dvi`的文件  
在Linux下您可以使用`xdvi`命令将其打开, 即:

```bash
xdvi demo.dvi
```

Windows下latex软件包大多数都预装了yap软件, 直接双击就可以打开`.dvi`文件  
要进一步生成的当前流行的PDF格式文件, 还需要将`.dvi`文件转换为`.pdf`文件

```bash
dvipdfmx demo.dvi
```

然后您就可以查看您的PDF文档了!

***不难发现, 如此编辑pdf文件真的是要多麻烦有多麻烦...***

### pdflatex 和 xelatex

上述两个命令可以略过生成`.dvi`文件的过程, 直接生成`.pdf`文件.

尤其是xelatex, 对中文支持及其优秀, 推荐大家食用!!

## latex中的文件类型及其意义

### 输入文件

|后缀|意义|
|---|---|
| .sty| 宏包文件, 宏包名称即为去掉.sty后的文件名|
| .cls| 文档类文件, 命名规则与宏包相同|
| .bib| 参考文献的数据库文件|
| .bst| 用到的参考文献的格式的模板|

### 输出文件

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

### Latex关键词的声明

* 使用`\`表明之后跟的不是普通字符, 而是一个Latex关键词.

### 文档类和宏包

#### 文档类

在.tex编辑的第一行, 一般都是这样的形式

```latex
\documentclass[<option1>,<option2>,...]{class-name}
```

这就是传说中的文档类  
其中, class-name是文档类的名称
其主要有一下几种:

|class-name|具体意义|
|-|-|
|article|用于写论文或短篇说明文档|
|report|用于写长篇报告,长篇论文, 简单的书籍等, 有章节结构|
|book|用于书写书籍, 文档结构复杂且严密, 有前言, 正文, 后记等结构|
|proc|基于article的简单学术文档模板|
|slides|用于制作幻灯片, 使用无衬线字体|
|minimal|极其精简的文档类, 一般用于测试代码|

\<option1>, \<option2>, ... 被称为可选参数, 他可以指定纸张的大小, 字号, 等等.

|\<options>|意义|
|-|-|
|12pt|指定文档的基本字号为12pt, 默认为10pt|
|a4paper|指定打印纸张为A4纸|
|fleqn|行间公式右对齐, 默认为居中|
|leqno|公式编号放在左边, 默认右边|
|twocolumn|双栏排版, 默认为单栏|
|twoside|纸张双面印刷排版, article和report默认为单面, book默认为双面|
|landscape|横向排版, 默认为纵向|

#### 宏包

紧接着下一行, 您一般会看到一下命令

```latex
\usepackage[<option1>, <option2>, ...]{package-name}
```

或更常见的写作:

```latex
\usepackage[<option1>, 
            <option2>, 
            ...]{package-name}
```

不同的宏包一般提供了不同的功能, 您可以通过

```bash
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

```latex
\title{article-title}
\author{your-name}
\date{date}
```

而后在正文中使用命令:

```latex
\maketitle
```

就可以显示文章的题目, 作者和日期了.

值得注意的是, 如果您不设置日期, 其会默认显示当前日期, 如果您不想显示日期, 只需将日期设置为空即可!  
也即

```latex
\date{}
```

### 文章主体

文章主体需要一个声明, 要理解这个声明, 首先要理解一个名为'环境'的东西.

环境可以理解成一个图层, 特殊的内容只有在特殊的图层上才可以被理解.图层可以摞在一起! 声明环境的语句十分简单.

```latex
\begin{env-name}
  ...
\end{env-name}
```

中间省略号部分即为受该环境支持的部分.

如果您要开始编辑文本了, 那么首先需要使用`document`环境!  

```latex
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
 之间的部分被称为'导言区'.

### 大文档的格式

大文档的编辑一般用`\include`指令, 即, 将要编辑的内容分别储存在若干个子文件里,
在主文件中使用

```latex
\include{<filename>}
```

指令就可以将子文件中的内容加载到主文件中进行编译.

您还可以在导言区中加入
这样一来, 不但问价结构清晰, 而且排错和修改内容也会变得极为方便.  

```latex
\includeonly{<filename1, filename2, ...>}
```

来限制在正文中`\include`的文件的范围.

## PDF文章的结构控制

### 标题

在导言区使用

```latex
\title{...}
\author{...}
\date{}
```

在文章主体中使用

```latex
\maketitle
```

即可完成标题的编辑

### 摘要

一般摘要应紧跟在标题后
摘要环境只适用于`article`与`report`

```latex
\begin{abstract}
...
\end{abstract}
```

### 章节

```latex
\part{<title>}
```

将文章书籍等分成若干大的部分(如, 上下册)

```latex
\section{<title>}
\subsection{<title>}
\subsubsection{<title>}
\paragraph{<title>}
\subparagraph{<title>}
```

不同层次的章节分层命令, 高层可嵌套低层, 例如:

```latex
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

```latex
\tableofcontents
```

### 脚注

```latex
\footnote{.....}
```

### 交叉引用

```latex
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

```latex
\usepackage{xeCJK}
```

* 一个空格和多个空格的效果一样
* .tex中单个换行只会产生一个空格, 多个换行会产生一个空行
* 文章强制换行使用`\\`, 此换行不产生缩进
* 使用`{}`隔开程序语言与普通文字

```latex
Sh\"o{}rdinger
```

* 使用`\par`产生新的段落

### 注释

```latex
% 这是一个注释
```

### 列表

使用`enumerate`环境产生一个列表  
次环境需要`enumerate`宏包的支持  

具体用法:

```latex
\begin{enumerate}[1.]
  \item you have lost
  \item you win
  \item finally, we find this staff!
\end{enumerate}
```

列表环境可嵌套使用!

### 引用

使用 `quote`环境

```latex
He said:
\begin{quote}
  I am your FATHER!
\end{quote}
```

### 代码

```latex
\begin{verbatim}
#include<stdio.h>

int main(void){
  printf("Hello!\n");

  return 0;
}
\end{verbatim}

```

行内代码引用可以使用:

```latex
\verb|printf|
```

需要注意的是, `\verb|..|`命令一般不可以包含在其他命令内部

### 表格

表格需要使用`tabular`环境

```latex
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

```latex
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

```latex
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

```latex
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

```latex
\begin{equation}

\end{equation}
```

行内公式:

```latex
$\hbar\omega = E_n - E_m$
```

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

```latex
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

  ```latex
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

```latex
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
将demo.tex编译为demo.pdf步骤:

1. 首先使用 pdflatex 或 xelatex 等命令编译 LATEX 源代码 demo.tex;
2. 接下来用 bibtex 命令处理 demo.aux 文件记录的参考文献格式、引用条目等信息。bibtex 命令处理完毕后会生成 demo.bbl 文件，内容就是一个 thebibliography 环境;
3. 再使用 pdflatex 或 xelatex 等命令把源代码 demo.tex 编译两遍,读入参考文献并正确 生成引用.

实际执行过程中

```bash
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
```latex
\newcommand{\⟨name⟩}[⟨num⟩]{⟨definition⟩}
```

具体的使用方法

```latex
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

```latex
\newenvironment{⟨name⟩}[⟨num⟩]{⟨before⟩}{⟨after⟩}
```

具体使用方法

```latex
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
在文件第一行  需要有:

```latex
\ProvidesPackage{⟨package name⟩}
```

如果在自己定义的宏包中要调用其他宏包:

```latex
\RequirePackage[⟨options⟩]{⟨package name⟩}
```

### 编写自己的文档类

不会, 大家自学吧, 学会了教教我 :/

### 计数器等其他很不常用的内容