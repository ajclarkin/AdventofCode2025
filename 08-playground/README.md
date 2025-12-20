# Playground

This is the first one that stumped me for a while. In retrospect I probably wasn't stumped, I just thought there should be a more elegant way to solve it.

The input is a series of x,y,z coordinates describing points in space. We need to connect the pairs in order, moving from the points closest together to further apart. I read the points in to a list of tuples and then created a dictionary of the format `dict[distance] = ((point1), (point2))`. For distance I used the squared distance for efficiency (I didn't take the square root of the squares of the distances).


## Part 1

Build a dictionary of the required number of shortest pairs.

First consider each possible pairing of points:
  - if we don't have the required number of pairs saved (we only need the first 1000) then save it (add to shortest)
  - otherwise replace the pair with longest distance in dict if this is shorter
  - dict shortest is of format: sortest[distance] = (point1, point2)

Now make a list of circuits, each stored as a set.
Try every combination of sets to see if they should be joined: if so then remove the two circuits and add the joined
circuits instead.
Process stops when the list of circuits doesn't get shorter - that is, there are no more unions to make.

I use `isdisjoint()` method here. `set1.isdijoint(set2)` will be false if they share a common element and true if they don't.

Once I have merged all the circuits that can be merged I sort by size, take the first 3, and multiply.


## Part 2

This was actually straightforward after getting through part 1.

Instead of building a dictionary of the 1000 shortest pairs I just make a dict of every pair and the distance. I make a list of the keys (distances) and sort it. I sort in reverse because popping from the end is more efficient.

Then I repeatedly pop a pair off to create a circuit and check to see if it would merge with other circuits as before. Once that set is minimised I pop the next point off. I keep going until all points have been used (using a set to keep track) and until it all merges down to one circuit. At that point I look at the coordinates of the most recently popped pair.

