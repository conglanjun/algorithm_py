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


    
    
    
    
    





