# Secret Entrance

This was a nice start to the year. There's a dial on the safe and we have to turn it so many times. In part 1 it's how many times does it land on 0, and in part 2 it's how many times does it pass 0.

## Part 1

Use a direction indicator to move left or right (multiply by -1 if left). At the end of each move we take the position mod 100 to correct for any rotations.

```python

# Example

>>> 5 % 10
5
>>> 15 % 10
5
>>> -3 % 10
7

```

## Part 2

Keep track of previous position and new position after a move. Use floor division (//) to count how many rotations have been added or subtracted. Take the absolute value to account for changes in direction.

```python

# One rotation: this illustrates the need for abs()
>>> 50//100 - 150//100
-1
>>> 50// - -88//100
0
>>> 50//100 - -88//100
1
>>> 50//100 - 350//100
-3
```

Nice.
