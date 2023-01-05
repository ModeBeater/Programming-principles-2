def solve(numheads, numlegs):
    # numheads = x + y
    # numlegs = 4 * x + 2 * y
    # y = numlegs / 2 - 2 * x
    x = (numlegs / 2) - numheads
    y = numheads - x
    ans = "chickens: " + str(y) + " rabbits: " + str(x)
    return ans
print(solve(35,94))