import sys
import functools


def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

        outer = []
        inner = []
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                outer.append(inner)
                inner = []
                continue
            inner.append(int(line))
        if len(inner) > 0:
            outer.append(inner)
        return outer


def sum_elves(data):
    return [functools.reduce(lambda a, b: a + b, e) for e in data]

def run(file_name):
    data = read_file(file_name)
    elves = sum_elves(data)
    elves.sort()
    top_elves = elves[-3:]
    print(top_elves)
    print(functools.reduce(lambda a, b: a + b, top_elves))

if __name__ == '__main__':
    run(sys.argv[1])
