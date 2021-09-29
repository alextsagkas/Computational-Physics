import numpy as np

# Random Number Generator - Uniform Distribution
def U():
        return np.random.rand()

# Integrated Function
def f(x):
    return np.exp(x)

if __name__ == "__main__":
    # Number of Random Numbers
    N = 10000

    # Limits of Integration
    a, b = 0 ,10

    # It is not actually mandatory to be the exact max{f(x)}
    f_max = f(b)

    # "Volume" of Integration
    V = (b-a) * f_max

    Hits = 0

    for i in range(N):
        x = (b-a)/2 * U() + (b-a)/2
        y = f_max * U()

        if y <= f(x):
            Hits += 1

    # Probalitiy to Hit
    p = Hits/N

    # Integral Computed with Hit-or-Miss Method
    I = V * p

    # Integral Error
    δI = V/np.sqrt(N) * np.sqrt(p-p**2)

    print(f'Ι ± δI = {I:.2f} ± {δI:.2f}')