# algorithm_py
algorithm learning
|作者|兰军|
|---|---|
|author|Lanujun|
****
Sort problems  
排序问题  

Common sorting algorithm  
常见排序算法  

* Sorting lowest 3 methods  最差的三个排序  
    * bubble sort  冒泡排序  
    * select sort  选择排序
    * insert sort  插入排序
* Sorting highest 3 methods  最厉害的三个排序
    * quick sort  快速排序
    * heap sort  堆排序
    * merge sort  归并排序
* Other sorting
    * shell sort  希尔排序
    * count sort  计数排序
    * cardinality sort 基数排序  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.20.jpg)  

bubble sorting  
If front is bigger than back in each two nearby numbers of list, exchanging them.  
列表每两个相邻数，如果前面比后面大，则交换。  
The number of disorder region is reduced in each sorting, while the number of order region is increased.  

Let's see a list.  
看一个列表。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.21.jpg)  
If the element pointed by arrow is bigger than back one, exchanging them.    
如果指针指向的元素大于后面的元素，交换。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.22.jpg)  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.23.jpg)  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.24.jpg)  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.25.jpg)  
7 is smaller than 8, not exchanging.  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.26.jpg)  
8 is bigger than 2, exchanging.  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.27.jpg)  
8 is smaller than 9, not exchanging  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.28.jpg)  
9 is bigger than 1, exchanging  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.29.jpg)  
Now the biggest is in the end of list. This is one sorting.    
最大的数在列表的最后。这是一趟排序。  
The Element's color is orange, which is in order region. The white is in disorder region.    
橙色在有序区，白色在无序区。  
The second sorting is in disorder.  
对无序区第二次排序。  
The number of order region is increased by second sorting.  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.30.jpg)  
Finally, the list is sorted.  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.31.jpg)  
The count of sorting is n-1. Because the number of order list is n-1, it means the whole list is order.  
排序n-1趟，因为有序列表数是n-1个，意味着整个列表都是有序的。  
The key of this algorithm is the count of sorting and order region.    
There is not element of order region in the beginning of this algorithm.  
算法的关键是趟数和无序区的范围，算法开始有序区没有元素。  
For example, when there are two element in order region and 7 elements in disorder region.  
The arrow can't point at 6 index, this is only pointed 5 index.   
So the count of comparing is smaller than the number of disorder region in each sorting.  
无序区有7个元素，但是只比较6次就可以。      
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.32.jpg)  






