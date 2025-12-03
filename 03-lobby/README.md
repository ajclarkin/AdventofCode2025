# Lobby

There was a step up in difficulty with part 2 today. Classic AoC - there was an easy (and elegant) solution that worked but did not scale up because of the maths.

The input is a long number, one per line. We have to build numbers out of the component digits. I hadx to do a bit of conversion back and forth to strings and then join them together to make the bigger numbers.


## Part 1

Find the biggest digit in each row. I did this by converting the number into a list of digits, sorting them descending, and taking the first. If the first digit is in the final position then we know the next largest number will come first. Otherwise find the largest number in the digits to the right of the position of the already-found digit. Then join them together and cast to int (reversing if required based on final position of the first).


## Part 2

Using the same large numbers find the biggest 12 digit number that can be formed from the digits in the input number while keeping the digits in order.

I initially used `itertools.combinations` to create every possible 12 character combination then joining them, casting to int, and selecting the maximum. This worked nicely for the example. However, it did not work for the main input and caused python to quit. It ran out of memory at the combination stage.

The next attempt was more brute-force. Start by finding the largest digit up to the last 11 characters (which will be required to complete the 12 digit number). Then find the biggest number between that position and last 10 characterss. And so on, until all 12 characters are selected. Then join and cast to int as before.
