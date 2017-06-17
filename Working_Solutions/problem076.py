
def ways_to_ctor_with(TARGET, values):

    ways = [0 for _ in xrange(0, TARGET + 1)]

    ways[0] = 1
    for value in values:
        for x, _ in enumerate(ways):
            if x < value:
                continue
            ways[x] += ways[x - value]

    return ways[-1]


if __name__ == '__main__':
    import sys
    TARGET = int(sys.argv[1])
    values = range(1, TARGET)
    print ways_to_ctor_with(TARGET, values)
