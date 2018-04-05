
sum_of_squares = lambda nums: sum(map(lambda x: x ** 2, nums))
square_of_sums = lambda nums: sum(nums) ** 2

diff = lambda f, g, high: f(xrange(1, high + 1)) - g(xrange(1, high + 1))

HIGH = 100
print diff(square_of_sums, sum_of_squares, HIGH)
