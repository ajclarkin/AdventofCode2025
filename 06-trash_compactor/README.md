# Trash Compactor

This is a challenge about reading the input in a column-wise manner. Again I think there is probably a better way to do this. I think I could have rotated a numpy array but decided to keep to base python.

I use `pop()` to remove the final element from the rows when they are lists and `string[-1]` when strings. Because I can access the operations row
directly it doesn't get reversed the way that these methods work so I `reverse()` this list.


## Part 1
In part one I pop the ends of each row (treating them as words which can then be cast to int) and then pass to `sum()` or `math.prod()`.


## Part 2
This time it's each character column that needs to be concatenated. Therefore I handle the rows as strings rather than the lists of numbers (as words). So, sequentially take the -1 character and add to a list, then remove the blanks, join, and cast to int.
