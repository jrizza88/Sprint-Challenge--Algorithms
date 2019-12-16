#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)  It's a runtime of log(n) or linear time. 

```python
  a = 0 ## o(1)
    while (a < n * n * n): 
      a = a + n * n
```
Example 1 below: 
```
n = 1 (it will only run once)

a = 0
while (0 < 1 * 1 * 1): (total is 1)
1st loop would be: a = 0 + 1 * 1 (this would equal 1)
    break `1 = 1`(you get 1 from the start)
```
Example 2 below: 
```
n = 2 (it will run twice once)
a = 0
while (0 < 2 * 2 * 2):
1st loop would be: a = 0 + 2 * 2 (total is 4)
    continue: 4 < 2 * 2 * 2
2nd loop would be: a = 4 + 2 * 2 (total is 8)
    break `8 = 2 * 2 * 2`
```
This same concept could work for any number of items. Due to the the linear growth of this, this shows a linear increase in run time as the input size grows. 

b) This would be O(log n)

```
  sum = 0 
    for i in range(n):   
      j = 1
      while j < n:
        j *= 2  
        sum += 1 
```

c) This would be O(n)

## Exercise II

This is to break down the points from the summary of exercise II into the general characteristics:
# n story building
# There are a lot of eggs
# floor f -
    # if high than a certain floor, eggs break
    # if lower than a certain floor, eggs do not break

Proposed algorithm - 
Plain english: Binary search would be the proposed algorithm. You would set the midway point of the total number of floors. You would throw the egg off of n-story building and see if it breaks.

** if the egg breaks, then you would only continue searching the n-story of buildings lower than where you dropped the egg from. Coding wise this would use the slice operator to check for only values less than from the n-story of where the egg was dropped.

** otherwise, if the egg does not break, you would then start counting everything higher than the floor you on to continue dropping eggs until you can find the first broken one. This would also use the slice operator. 

The point of the above two instance is to keep halving the midpoint until you reach the midpoint you are seeking. Once the mid point is hit, you would terminate the experiment and return the floor f that the experiment is looking for. 

The run time complexity would be O(log n) because it would keep minimizing/reducing the amount of times that you have to drop the egg. 

Pseudo code version:
``` 


pseudocode: 



This would be a logarithmic log time, also known as O(log n)



