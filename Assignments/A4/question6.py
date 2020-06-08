# These are the six most informative unit tests I can think of:

# 1. lines = ([0.0, 0.0], [1.0, 1.0]], [[1.0, 1.0], [2.0, 2.0]])
# This produces a unit test for two lines that share the same point.
# We will find out if there'll be a point of intersection at that point or not. It could bug out.

# 2. lines = ([[0.0, 0.0], [5.0, 5.0]], [[0.0, 5.0], [5.0, 0.0]])
# This produces a valid test that has one regular intersection.

# 3. lines = ([[0.0, 0.0], [1.0, 1.0]], [[0.0, 3.0], [2.0, 2.0]])
# This produces a non-intersection test.

# 4. lines = ([[1.0, 1.0], [1.0, 1.0], [[0.0, 0.0], [3.0, 3.0]])
# One line shares the same point.

# 5. lines = (["cat", "cat"], ["dog", "bird"])
# This test involves strings.

# 6. lines = ([[-1.0, -1.0], [1.0, 1.0]], [[[-3.0, 3.0], [3.0, -3.0]]
# This test includes negative values.