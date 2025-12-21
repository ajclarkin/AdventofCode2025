# Movie Theater

We're given a set of x,y coordinates. I read them into a list of tuples.


## Part 1

Find the biggest rectangle made from two of the points as opposite corners. The distances measured
are inclusive: 2,1 to 7,2 would be 6 wide and 2 high.

Nice and easy. Consider all the combinations of points and calculate the area as `abs(x2-x1) + 1 *
abs(y2-y1) + 1`

Note that I could have made it more efficient:

```python

combos = list(combinations(points, 2))
areas = [CalcArea(*c) for c in combos]

# could be rewritten as


areas = [CalcArea(*c) for c in combinations(points, 2)]

```
