## First thoughts
This problem appears to be a set covering problem. For instance, the problem asks how many dominos need to be knocked over, and we're given a list of pairs of numbers showing which domino each domino can in turn knock over. If there are any gaps in that series of numbers, we need to knock down an additional domino ourselves.

## inputs:
total # of test cases (always occurs only once)
test case description (can occur multiple times, once per test case)
  - contains two numbers, n and m, both <= 100000
  - n is the total number of dominos
  - m is the number of lines of domino number pairs
domino number pairs (can occur multiple times per test case)
  - numbers are x and y, indicating that if domino x falls, it causes y to fall

# output:
integer k representing the number of dominos needing to be knocked over by hand

## additional thoughts
A first approach will be to see if the domino number pairs cover the entire range of dominos. We need at least one knock to get the series started, and an additional knock for any domino not covered in the pair. We could initialize k with the first value giving the total number of test cases.

It's possible that the relationship between n and m could be enough to get k. This example input has n = 3 and m = 2, with k = 2:
### test case inputs with k = 2:
1
4 2
1 2
3 4
