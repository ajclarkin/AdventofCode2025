# Printing Department

This is the first of the two dimensional maps this year. Here we have a grid of `.` and occasional `@` which represent rolls of paper. We have to find all the rolls which can be moved, the criteria for which is that they touch fewer that 4 other rolls out of possible 8. A roll on the boundary has fewer possible contacts but doesn't need to be handled differently.

I considered storing the whole grid for this (`grid[(r, c)]: char`) but actually don't need that. What I actully did was store a list of the positions of the rolls of paper, and another list of the dc and dr needed to check the other positions. Bounds handling is not required.


## Part 1

For each roll of paper (position stored in list_rolls) count the adjacent rolls. If fewer than 4 then increment a counter.


## Part 2

I anticipated this. This time after the identified rolls have been removed (in the manner of part 1), look again to see what rolls can be removed and do so. Repeat until no more rolls can be removed.

I wrapped the part 1 solution in a loop which repeated if the previous loop was successful in removing a roll.

The one thing that I needed to remember was not to edit a list while iterating through it. Remember to use a copy.

