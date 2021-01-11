import sys


def calculate_displacement(v, t):
    return v * t * 2


if __name__ == '__main__':

    inputs = []
    for line in sys.stdin:
        inputs.append(line)
# with open('input.txt') as f:
#     inputs = [line.strip() for line in f]


for line in inputs:
    values = line.split(' ')
    v = int(values[0])
    t = int(values[1])
    print(calculate_displacement(v, t))
exit(0)
