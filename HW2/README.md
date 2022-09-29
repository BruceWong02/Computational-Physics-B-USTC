# 计算物理B第二次作业

PB20511896 王金鑫

## 使用说明

### 文件说明

- main.py : 主程序，在接收用户的输入后执行相关题目的程序并输出结果。可在一次运行中重复使用。
- Question1.py : 解答第一题的程序，包括指数衰减分布事例产生器的定义和动画演示，以及使用重要采样法计算积分 $\int_{0}^{+\infin}x^{\frac{3}{2}}e^{-x}dx$ 的蒙特卡洛估计值。
- Question2.py : 解答第二题的程序，包括Breit-Wigner分布事例产生器的定义和动画演示，以及使用重要采样法计算积分 $\int_{-\infin}^{+\infin}\frac{\sqrt{x}}{1+x^2}dx$ 的蒙特卡洛估计值。
- PlotAnimationOfHist.py : 基于matplotlib.animation.FuncAnimation对直方图更新过程的动画绘制。输出结果可直接窗口展示或者以gif格式保存在figs文件夹中。

### 库说明

- matplotlib.pyplot：用于绘制直方图
- matplotlib.animation：用于绘制动画
- numpy：使用numpy.histogram()函数来计算数据集的直方图，获取每个bar的数值以用来在绘制动画过程中更新直方图。
- random.uniform：用于产生[0, 1]上的均匀随机数。
- math：调用相关数学常数 (例如：math.pi $\rightarrow \pi$) 和初等函数。
- cmath：利用cmath.sqrt()函数来进行复数开根号。

### 函数说明

> 源代码中均有注释，在这里挑选部分进行展示

- ExpDecayCaseGener(lamda) ： 指数衰减分布事例产生器，使用直接抽样法。

  > 指数衰减分布密度函数：$f(x) = \lambda e^{-\lambda x},\quad x\in [0, +\infin)$

- BreitWignerCaseGener(Gamma, x0=0) ： Breit-Wigner分布事例产生器，使用直接抽样法。

  > Breit-Wigner分布密度函数：$f(x) = \frac{\Gamma}{\pi}\frac{1}{(x-x_0)^2 + \Gamma^2}$， 其中 $x_0\in \R， \Gamma > 0$

- PlotAnimation(generator, out, GenerPar, hTitle=None, yTop=None, hrange=None)：绘制直方图更新动画。

  - 参数说明
    - generator：事例产生器的函数
    - out：输出方式。0==out时将动画以gif格式保存在figs文件夹中，否则直接以窗口形式播放
    - GenerPar：产生器的参数
    - hTitle：直方图的标题
    - yTop：直方图纵轴高度的上限
    - hrange：直方图横轴取值的范围
  - 内部函数说明
    - init()：将直方图初始化，动画将从初始化后的状态开始。默认初始化为0
    - animate()：更新每一帧的直方图数据。这里的方法为产生新的500个随机事例后得到一个新的直方图，并将每个bar中的数值对应地赋到图像中的直方图bar中
  - 调用函数说明
    - ax.hist()：在图像中创建直方图对象并将BarContainer(存储每个bar的数值)的句柄赋到bar_container变量中
    - numpy.histogram()：计算新随机数集的直方图，得到每个bar的数值
    - zip()：将两个列表的元素按顺序一一对应打包成元组，将元组组合成列表后返回
    - animation.FuncAnimation()：产生动画。其中参数iterable为迭代次数。其余参数用途可参考函数注释。

### 运行说明

打开main.py，运行，输入1来解答题1，输入2来解答题2，输入其他来退出。

改变Q2.Sub_question2(way)中参数way的值来选择计算方法。0==way时，直接对复数开根号。way==其他值时，先只计算x>0的积分值（为实数），再乘上（1+i）作为最终结果。（由函数对称性可得后一种方法是合理的。

对于分布函数的参数可以在相应题目的程序中修改。

每个小题的第一小问中默认产生的随机事例数为N=10000，可在PlotAnimationOfHist.py中修改。$N=每帧动画更新的随机点数\times迭代次数(iterable)$

每个小题的第二小问可在相应的函数中修改N的值来修改抽样点数，默认为1000000。

### 注意事项

- 直方图更新动画的保存和绘制不能连续进行，因为函数中没有对最终的图像进行数据清理，若在保存了动画后立即绘图展示的话，结果会是在保存的动画的最终结果上进行更新，而不是从0开始重新抽样。且保存的动画和直接展示的动画是两个不同的产生过程。
- 在测试过程中发现对于两个题目的第二小问，即使抽样点数达到百万的量级，最终积分结果仍然在小数点后第二位上有波动，但波动程度明显较几十万数量级的抽样要小。
- 第二题第二小问中，由于事例分布范围为$(-\infin, +\infin)$， 因此默认情况下直方图横轴区间会很大，导致在0附近的事例都被统计在一两个bar当中，使得结果为一条特别高的bar。因此需要将直方图区间加以限制。在这里默认的限制为[-30, 30]。

## 运行结果

| ![ExpDecay](figs\ExpDecay.gif)                               | ![BreitWigner](figs\BreitWignerCaseGener.gif)                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 图1. 指数衰减分布事例产生器                                  | 图2. Breit-Wigner分布事例产生器                              |
| ![I1](figs\I1.jpg)                                           | ![I2_0](figs\I20.jpg)                                        |
| 图3. $\int_{0}^{+\infin}x^{\frac{3}{2}}e^{-x}dx$ 的MC估计值  | 图4. 直接按复数开根号得到的 $\int_{-\infin}^{+\infin}\frac{\sqrt{x}}{1+x^2}dx$ MC估计值 |
| ![I2_1](figs\I21.jpg)                                        |                                                              |
| 图5. 通过求$[0, +\infin)$上的实积分得到的 $\int_{-\infin}^{+\infin}\frac{\sqrt{x}}{1+x^2}dx$ MC估计值 |                                                              |

