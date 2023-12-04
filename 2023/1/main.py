from collections import deque
import itertools


def part1(fname):
    def parse_line(line: str):
        v = 0
        l = len(line)
        for i in range(l):
            if (c := line[i]).isdigit():
                v += int(c) * 10
                break
        for i in range(l - 1, -1, -1):
            if (c := line[i]).isdigit():
                v += int(c)
                break
        return v

    s = 0
    with open(fname, "r", encoding="utf-8") as f:
        s = sum(parse_line(l) for l in f)
    print(s)

TRANS_TABLE = {
    "one":1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

BACK_TRANS_TABLE = {''.join(reversed(k)): v for k, v in TRANS_TABLE.items()}
POSSIBLE_CHARS = frozenset(itertools.chain.from_iterable(TRANS_TABLE.keys()))


# print('\n'.join(sorted(BACK_TRANS_TABLE.keys())))
# print(POSSIBLE_CHARS)

def forward_pass(line):
    queue = deque(maxlen=5)
    for c in line:
        if c.isdigit():
            return int(c)
        queue.append(c)
        temp = ''.join(queue)
        for k, v in TRANS_TABLE.items():
            if temp.endswith(k):
                return v
    
def backward_pass(line):
    queue = deque(maxlen=5)
    for c in reversed(line):
        if c.isdigit():
            return int(c)
        queue.append(c)
        temp = ''.join(queue)
        for k, v in BACK_TRANS_TABLE.items():
            if temp.endswith(k):
                return v


def part2(fname):
    def parse_line(l):
        return forward_pass(l)*10 + backward_pass(l)
    
    with open(fname, "r", encoding="utf-8") as f:
        t = [parse_line(l) for l in f]
        print(t)
        s = sum(t)
    print(s)


if __name__ == "__main__":
    part2("input")
