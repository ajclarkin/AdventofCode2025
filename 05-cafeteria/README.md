# Cafeteria

This looked more straightforward than I actually found it.

The input is multiple ranges of integers, then a blank line, then multple integers. Part 1 is to count how many of those ints are contained within the ranges (inclusive), and part 2 is to count how many unique ints are within the ranges. Some ranges overlap and some might be completely contained by another. The ranges are inclusive of start and end value so there's a risk of out-by-one error.


## Part 1

Simple approach. Read in the ranges and then iterate through the ints and the ranges looking to see if the value is contained.

I did make heavy weather of parsing the input here and I'm not sure why. That took longer that the problem itself.


## Part 2

And then I made this look difficult. The ranges look like this:

```text
###
     ####
       #####
    ######
              ####
           ###

```

I assume that iterating from beginning to end of each range and adding to a set to deduplicate won't work. The ranges are too big and too high. I didn't test this. But the alternative is to do `high - low`.  In order to do this the ranges will need to be merged to prevent double-counting overlaps.

- My first attempt was nested loops comparing each range to all the others. I got close but it was confusing.
- Then I tried sorting the lists and walking up them but I had the logic wrong.
- I eventually settled on `itertools.combinations()` to produce each 2-range compbination: `AB AC AD BC BD CD` in order to compare each to every other. If a comparison resulted in changing a range the new one was saved and the combinations() function started afresh with the previous comparison pair replaced with the single updated range.

I note from Reddit that if I had sorted the ranges first then I would have just been able to compare adjacent ranges and this would have been more efficient than than the combinations approach.
