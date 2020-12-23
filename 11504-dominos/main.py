# not yet passing
import sys


def count_knocks(n, m, pairs):
    count = 0
    domino_list = [False for _ in range(n)]

    for pair in pairs:
        x, y = map(int, pair.split(' '))
        domino_list[y - 1] = True

    for domino in domino_list:
        if domino is False:
            count += 1
    return count


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('input.txt') as f:
#     inputs = [line.strip() for line in f]

num_test_cases = int(inputs[0])
inputs = inputs[1:]
for case in range(num_test_cases):
    n, m = map(int, inputs[0].split(' '))
    domino_pairs = inputs[1:m+1]
    inputs = inputs[m+1:]
    print(count_knocks(n, m, domino_pairs))
exit(0)
