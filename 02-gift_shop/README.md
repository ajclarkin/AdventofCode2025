## Gift Shop

There was a slight step up in difficulty today but not too much. The input is a set of numeric ranges such as `12-55,95-119` and we have to search all the numbers in the ranges for patterns.

I approached this by iterating through each range, converting the current number to a string, and then slicing the string to look for the patterns. I had considered a vectorised solution but it wasn't required.


### Part 1

Find all the numbers in the range made up of a sequence repeated, that is, the first half is the same as the second half of the number. So, 11 and 22 would be present in 12-55.

I did this by excluding the numbers with an odd number of characters, then slicing into first and second half and checking for equality.


### Part 2

This time we're looking for all the numbers made of a repeating sequence. So, 11 and 22 are still valid but 111, 446446, and 828282 would all be valid.

This time I start at 1 character and see if it repeated for the length of the string is equal to the string. Then try 2 characters repeated length/2 times, and so on until all the possibilties up to half the length of the string are considered. I initially had the wrong solution and when checking the found values I discovered some single digits which did not meet the day's criteria.

