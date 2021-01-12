import sys
from math import sqrt, floor

def calculate_troop_rows(num_troops):
    return floor(-0.5 + sqrt(0.25 + 2 * num_troops))


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('input.txt') as f:
#     inputs = [line.strip() for line in f]

num_cases = inputs[0]
inputs = inputs[1:]

for line in inputs:
    num_troops = int(line)
    print(calculate_troop_rows(num_troops))
exit(0)
