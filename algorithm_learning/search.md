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

The middle value 2 is smaller than 3. It means candidates is in the right of mid.  
中值2小于3，意味着候选区在中值右边。  
Moving `left` to 2. `left=mid+1`  
移动`left`到2的位置。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.16.jpg)  

`left=2` `right=3` `mid=(left+right)/2=2`  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.17.jpg)  

The middle value is equal to 3, which is the number we want to find.  
中值等于3就是我们要找的数。  

If the value of `left` is 4. It means the value should be in the left of the location of `left`.  
如果left位置的值是4，说明要找的值在left的左边。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.18.jpg)  

`right=mid-1=1` If `right` < `left`, there are not value in the candidate region.  
此时候选区没有值了。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.19.jpg)  




