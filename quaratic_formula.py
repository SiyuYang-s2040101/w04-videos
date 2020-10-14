# %% md
# We want to find the roots of quadratic function $ax^2 + bx + c = 0$ <br />
# This formula gives us the roots:  <br />
# $x_1, x_2 = \cfrac{-b\pm \sqrt{b^2-4ac} }{2a}$


# %% codecell
import numpy as np


def quad_R_roots(a, b, c):
    D = b**2 - 4*a*c
    x1 = (-b + (D)**0.5)/(2*a)
    x2 = (-b - (D)**0.5)/(2*a)
    return x1, x2

print(quad_R_roots(2, -1, -3))
print(quad_R_roots(1, 2, 5))

def quad_C_roots(aR, bR, cR):
    a = np.complex(aR, 0)
    b = np.complex(bR, 0)
    c = np.complex(cR, 0)
    D = b**2 - 4*a*c
    x1 = (-b + np.sqrt(D))/(2*a)
    x2 = (-b - np.sqrt(D))/(2*a)
    return x1, x2


print(quad_C_roots(2, -1, -3))
print(quad_C_roots(1, 2, 5))

# %%
