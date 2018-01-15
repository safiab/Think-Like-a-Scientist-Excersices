# Start the Python interpreter and use it as a calculator. Python's syntax
# for math operations is almost the same as standard mathematical notation.
# For example, the symbols +, - and / denote addition, subtraction and
# division, as you would expect. The symbol for multiplication is '*'.
#
# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your average time
# per mile? What is your average speed in miles per hour? (Hint: there are
# 1.61 kilometers in a mile).

# conevert distance to distance in miles

distanceKM = 10
distanceMile = distanceKM / 1.61

# convert rice time  to seconds
timePerSeconds = (43 * 60) + 30

# print average time per mile
print(timePerSeconds / distanceMile, 'seconds per mile')

# convert rice time  to hours
timePerHours = 43.5 / 60

# average speed in miles per hour
print(distanceMile / timePerHours, 'miles per hour')
