# slam
## c++基础
### g++
ubuntu等linux系统的c++编译器，把c源码编译为可执行文件
```
g++ helloSLAM.cpp 
./a.out
```
### cmake
在一个 cmake 工程中，我们会用 cmake 命令生成一个 makefile 文件，然后，用 make
命令，根据这个 makefile 文件的内容，编译整个工程。
在 slambook/ch2/中
新建一个 CMakeLists.txt 文件，输入：
```
# 声明要求的 cmake 最低版本
cmake_minimum_required( VERSION 2.8 )
3
4
5
# 声明一个 cmake 工程
project( HelloSLAM )
6
7
8
9
# 添加一个可执行程序
# 语法：add_executable( 程序名 源代码文件 ）
add_executable( helloSLAM helloSLAM.cpp )
```
使用mcake命令生成MakeFile
```
cmake .
```
使用make命令编译
```
make
./helloSLAM
```
现在这个过程中，唯一让我们不满的是，cmake 生成的中间文件还留在我们代码文件
当中。当我们想要发布代码时，并不希望把这些中间文件一同发布出去。这时我们还需把
它们一个个删除，这十分的不便。一种更好的做法是让这些中间文件都放在一个中间目录
中，在编译成功后，把这个中间目录删除即可。所以，更常见的编译 cmake 工程的做法就
是这样：
```
mkdir build
cd build
cmake ..
make
```
## 旋转与变换
### 旋转
#### 旋转矩阵
#### 旋转向量
#### 欧拉角
#### 四元数
