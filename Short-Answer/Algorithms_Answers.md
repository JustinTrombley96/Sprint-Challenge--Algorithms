#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
Constant


b) Logarithmic(n log n)


c) O(n)

## Exercise II

Binary Search is the algorithm that I would propose for this problem. We have to find floor f, which is the floor highest floor that the egg can be dropped off without breaking. N is the argument that represents the amount of floors in the building.

I would create an above and below variable for the floors above and below f which is our target. I would set below = 0 and above to the length of n - 1.

First I would set a while the bottom floors is less than or equal to the above floors. Inside of that loop I would create a mid floor which would be bottom plus top divided by 2.

Still inside of that while loop I would have if n[mid] is equal to f then return mid

if n[mid] was less than f then bottom equals mid + 1.

I would then have an else that would have the above floors - 1

Then outside of the while loop if we didn't find the element I would return -1.

This has a runtime of O(log n).