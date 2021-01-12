This looks like a problem of calculating the root of a triangle number:
x = n * (n+1) / 2

setting it to a quadratic equation:
0 = (n^2 + n) / 2 - x
0 = 0.5 * n^2 + 0.5 * n - x
a = 0.5, b = 0.5, c = -x

n = (-0.5 +/- sqrt((0.5)^2 - (4 * 0.5 * (-x))) / (2 * 0.5)
  = -0.5 +/- sqrt(0.25 - 2 * (-x))
  = -0.5 + sqrt(0.25 + 2x) -> removing "minus sqrt" because 'n' can't be a negative value

We'll also need to take the floor value of this (ignore decimal values) as we only care about potential complete rows of troops.
