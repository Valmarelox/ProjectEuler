#Constants
START_X, START_Y = 10, 10
END_X, END_Y = 100, 100
TARGET = 2 * (10 ** 6)


def count_rectangle(x,y):
    return (TOTAL_X - (x - 1)) * (TOTAL_Y - (y - 1))

closest_solution = 0
closest_x, closest_y = 0,0
for TOTAL_X in xrange(START_X, END_X):
    for TOTAL_Y in xrange(START_Y, END_Y):
        counter = 0
        for x in xrange(1, TOTAL_X + 1):
            for y in xrange(1, TOTAL_Y + 1):
                counter += count_rectangle(x,y)
        if abs(TARGET - counter) < abs(TARGET - closest_solution):
            closest_solution = counter
            closest_x, closest_y = TOTAL_X, TOTAL_Y
            print "closest: {sol}; {x} * {y} = {area}" \
                .format(sol=closest_solution, x=closest_x, \
                    y=closest_y, area=closest_x * closest_y)

