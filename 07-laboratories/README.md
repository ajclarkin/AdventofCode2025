# Laboratories

This was interesting and again I was tricked by the Maker. It's a series of paths moving downwards and splitting in two so a bit of a binary tree, except that paths can merge again.
In part 1 the question is how many times the path splits - which was quite easy. The second part was to count the number of unique paths.


## Part 1
For this part I start on then top line and look at the positions. I then look for splitters and to see if they split. I save the positions and then move to the next line. At the end I count how many times the line has changed (by splitting).


## Part 2
Find all the unique paths. Easy - depth first search. But no, there are too many paths and it's never going to complete. I eventually had to resort to @hyperneutrino - their explainer on youtube helped immensely. This required `functools.cache` for memoisation, and then I had some difficulty tracking the count. The point is that there are a *huge* number of paths and so caching the results makes it possible.

Recursive algorithm. Use a function to consider one line down from current position:
 - if bottom then return 1
 - if no change then return next iteration of function
 - if splitter then return next iteration left + next iteration right.

