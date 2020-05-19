# algorithm_py
algorithm learning
|作者|兰军|
|---|---|
|author|Lanujun|
****
Search problem  
查找问题  

Using two variables to control the candidate region. Initialize variable left by 0, right by n-1.  
用两个变量控制候选区，初始化变量left=0， right=n-1  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.12.jpg)  

Finding the middle value. (left + right) / 2 = mid.  
找到中间元素  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.13.jpg)  

Judge the middle value 5 is larger than 3. It means candidates is in the left of mid.    
比较中间值5大于3。说明候选区域在左边。  
Moving `right` to 4. `right=mid-1`  
移动`right`到4的位置。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.14.jpg)  

Calculating new mid. `(0+3)/2=1`  
计算新mid值。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.15.jpg)  

