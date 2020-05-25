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

### bubble sorting  
`Time complexity: O(n2)`  
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

Bubble sorting does not exchange in one sorting, it means list is already sorted and it is order.  
冒泡排序在一趟排序中没有交还，意味着已经排好序了。  

Add a flag, which is exchange = False.  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.33.jpg)  
When the original list is order, the sorting only needs one loop. While version 1 bubble sorting needs n-1 loops.  
当数组有序，只需要排一次。版本1冒泡排序需要排n-1次。  

### select sort  
`Time complexity: O(n2)`  
1. simple select sort  
    Each loop find the min val of list, and put it into a new list.  
    每次循环找最小值放到新列表中。  
    ![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.34.jpg)  
    The shortage is:  
        a.It needs a new space to save sorted list.  
          需要新空间存放列表。  
        b.Outer layer loop is O(n), the min is O(n),  
          li.remove is O(n) because of finding the element to remove and the following elements need to be filled forward.  
          外层循环O(n)，最小值O(n)，删除O(n)因为要找到元素并且后续元素往前补位。  
2. select sort  
    Exchange selected element into the first place in the list.  
    把找到的元素与第一个位置交换。  
    The first place is order region, while the elements behind is disorder region.  
    第一个位置就是有序区，后面的元素是无序区。  
    Each loop we will put the min value into the order region. After n-1 loops, there are n-1 elements in the order region.  
    There is one element in the disorder region, but it's the biggest one. So we need n-1 loops to sort list.  
    每次循环会把最小值放到有序区，n-1次循环后，有序区n-1个元素，无序区有一个元素，但已经是最大的，因此排序列表需要循环n-1次。  
    ![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.35.jpg)  
    ![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.36.jpg)  
### insert sort  
`Time complexity: O(n2)`  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.37.jpg)  
For example, the color is orange, it means order region(cards in hand), it is 5.  
The first card is 7 in the disorder region. 7 is bigger than 5, so insert 7 into the right of 5.  
手中牌是橙色5，要摸的牌是白色。摸到7比5大，插入到5的右边。  
When the first card is 4 in disorder region, we move 7 and 5 to right.  
摸到4，向右移动7和5。  
Next it is 6, it is inserted between 5 and 7.  
摸到6插入5和7之间。  
Nest it is 3, it is inserted the first place, and following numbers are moved to right space place.  
摸到3，有序区都向右移动，3插入到第一个位置。  
Nest it's 1, it's inserted the first place, and following numbers are moved to right space place.  
摸到1插入第一个位置，右边元素往右移动。  
Nest it's 2, it's inserted between 1 and 3, and right elements are moved to right space place.  
摸到2插入到1和3之间，右边元素往右边移动。  
Nest it's 9, it's bigger than order region, so it's inserted the last place.  
摸到9，比有序区都大，插入到最后的位置。  
Nest it's 8, it's inserted 7 and 9, moving 9 to right.  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/alg_insert_sort.gif)  
We touch n-1 cards, white region is touched by us. After touching a card, we compare it with the biggest one of order region.  
我们会摸到n-1张牌，白色区域是要摸的牌，摸到一张后，比较手里牌最大的。  
If the biggest one is bigger than the card, moving the biggest one to right space place.  
如果最大的大于手里的牌，向右移动最大牌到空位。  
We compare the second biggest one of order region. When the one of order region is smaller than the card or reaching the first place.  
Stopping to find place, inserting the card.  
比较第二大的牌，当手里牌小于或者已经到手里牌最左边的位置(也就是手里牌都比摸的牌大)，停止比较，插入牌。  

![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.39.jpg)  
Explain the code, for example, touching card is 6, it's smaller than 7 and index j points it, so 7 is moved to right.  
And j is moved left, it points 5 index. Now 6 is bigger than 5, so 6 is inserted j+1 index.  
说明下代码，摸到6，小于7并且j指向它，7向右移动。j索引左移指向了5，6大于5，所以插入j+1的位置。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.38.jpg)  
When touching card is 3, it's smaller than 7,6,5,4. They are moved to right and j -= 1.  
当摸到3时，比7,6,5,4都小，把他们右移，那么j向左移动。  
Finally, j = -1, so while loop is over. Insert 3 into j+1 index.  
最后j=-1，while循环结束，插入到j+1的位置。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.40.jpg)  
****
Sorting lowest 3 methods is over! They are in-place sort.  
`Time complexity: O(n2)`  

### quick sort
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.41.jpg)  
For example, get first value 5, and find some values are smaller than 5.  
Find them in the right of list and put them to left.  
获取第一个5，在列表指针右边找比5小的放到左边。  
8 is bigger than 5, moving arrow to left. 9 is bigger than 5, moving arrow to left.  
8，9比5大，往左边移动。  
2 is smaller than 5, moving 2 to left arrow. Now begin to find the number is bigger than 5.  
2小于5放到左边箭头，现在开始找比5大的。  
2 is smaller than 5, 7 is bigger than 5, moving 7 to right arrow.  
2小于5，7大于5，移动7到右箭头。  
Now left has space place, find the smaller than 5 in right.  
左边找到空位了，去右边找比5小的空位。  
7 is bigger than 5, 1 is smaller than 5, moving 1 to left arrow.  
7大于5，1小于5，移动1到左边箭头。  
Now find in left. 1 and 4 are smaller than 5. 6 is bigger than 5, moving 6 to right arrow.  
在左边找，1和4小于5，6大于5，移动6到右边。  
Now find in right. 6 is bigger than 5, 3 is smaller than 5, moving 3 to left arrow.  
在右边找，6比5大，3比5小，移动3到左边箭头。  
Now finding the bigger number is than 5 in left, 3 is smaller than 5, moving left arrow to right.  
Now left and right are coincidence.  
在左边找比5大的数，3比5小，左箭头右移，现在左右箭头重合。  
Moving 5 to this place. This process is the partition of code.  
把5移动到这里。这就是代码中partition的过程。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/alg_quick_sort.gif)  
    
Explain code.  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.42.jpg)  
Partition code. Variant tmp sorts the first value of li. Left points the begin of the list, while right points the end of list.  
When left < right, we find right arrow element is smaller than tmp value, the arrow will be moved to left one step.  
Until we find right arrow points element which is smaller than tmp. Move right element to left point.  
Now we find left arrow element is bigger than tmp value, the arrow will be moved to right,  
until we find left arrow points element which is bigger than tmp. Move left element to right point.  
Until left and right arrows are coincidence. Put tmp value into left arrow.  
Now list is separated left elements are smaller than tmp value, right elements are bigger than tmp value.  
Quick sort code. Involve partition function return mid index. Left list is put into quick_sort function.  
Right list is put into quick_sort function. Recursion implement.  
Partition 代码。tmp存li第一个变量，左指针指向list第一个位置，右指针指向末尾，左指针小于右指针时进行list的元素查找。  
右指针会向左边移动直到找到比tmp小的值，把它移动到左边的位置。左指针会向右边移动直到找到比tmp大的值，把它移动到右边位置。  
直到左右指针重合，把tmp值放到指针位置。  
现在list被切分成左右两部分，右边元素比tmp大，左边元素比tmp小。
Quick sort代码。调用partition函数得到中间切分索引mid。左半部分调用quick_sort函数，右边也是。递归实现。  
`Time complexity: O(nlogn)`  
Because each loop cut the list to left half and right half. So the program runs logn counts of partition.  
And all parts run n count in one layer. So nlogn time complexity.  
因为每次循环切分列表为左右两部分，因此程序运行logn次partition函数，并且一层所有部分要运行n次。因此时间复杂度是nlogn。  
Let's see the worst. The list is reversed order.  
看下最坏情况，倒序列表。  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/alg_quick_sort1.gif)  
In the worst condition, partition function get the worst result, which only has right part.  
That means one loop only cuts one element.  
最坏的情况，partition函数只获取右边部分。左边部分没有。也就是一次只切分掉一个元素。  
So the program runs n counts partition, the time complexity is O(n2) in the worst condition.  
程序要运行n次partition函数，最坏情况时间复杂度是O(n2)。  
If you want to test the worst condition, it maybe throw Recursion Error. So `sys.setrecursionlimit(1000)`
测试最坏情况，递归栈可能会溢出，设置递归参数  `sys.setrecursionlimit(1000)`  
We can solve the problem with random finding the tmp value from list. Exchange first value and the finding value。  
通过随机tmp值来解决这个问题。交换第一个数和随机找的数。  
If you get tmp value is the biggest value, you'll meet the worst condition. But the probability is small.  
如果你找到tmp值是最大值，你会遇到最坏的情况。但是概率很小。  

### quick sort
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.43.jpg)  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.44.jpg)  
![image](https://github.com/conglanjun/algorithm_py/blob/master/image/1.45.jpg)  


    





