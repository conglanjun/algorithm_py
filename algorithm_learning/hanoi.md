# algorithm_py
algorithm learning
|作者|兰军|
|---|---|
|author|Lanujun|
****
Hanoi problem
汉诺塔问题  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.1.png)  
Move 3 plate from a to b.
把三个盘子从a移动到b。  
Step 1, small plate is moved to b.  
第一步把小盘移动到b。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.2.png)  
Step 2, middle plate is moved to c.  
第二步中间圆盘移动到c。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.3.png)  
Step 3, small plate is moved to c.  
第三步，小盘移动到c。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.4.jpg)  
Step 4, big plate is moved to b.  
第四步，大盘移动到b。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.5.png)  
Step 5, small plate is moved to a.  
第五步，小盘移动到a。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.6.jpg)  
Step 6, middle plate is moved to b.  
第六步，中间盘移动到b。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.7.jpg)  
Step 7, small plate is moved to b.  
第七步，小盘移动到b。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.8.jpg)  
****
Can we move n plates from a to c?  
怎么把n个盘子从a移动到c呢？  
* n plates:
    * 1. Move n-1 plates from a to b with c.(把n-1个盘子从a经过c移动到b)  
    ![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.9.jpg)
    * 2. Move the biggest plate from a to c.(把最大的盘子从a移动到c)  
    ![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.10.jpg)  
    * 3. Move n-1 plates from b to c.(把n-1个盘子从b移动到c)  
    ![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.11.jpg)  
Step 2 is that moving a plate.  
第二步是移动一个盘子的。  
Although it's impossible to move n-1 plates in one step, it's 1 smaller than the original problem.  
虽然不能一步移动n-1个盘子，但是比原问题规模小1。  
Implement with recursion. Code in [hanoi](https://github.com/conglanjun/algorithm_py/blob/master/algorithm_learning/hanoi.py)  
用递归实现。  

