import numpy as np

# Langrange Polynomial of 3rd Degree
def P(x_data, f_data, pos, x):  # pos is an array with elements the positions of x_data we use

    # n = Degree of the polynomial + 1
    n = len(pos)

    def L(x_data, pos, x):

        L = np.ones(n)

        # Polynomial that goes through x_data[pos[i]]
        for i in range(n):
            for j in range(n):
                if pos[i] != pos[j]:
                    L[i] *= (x - x_data[pos[j]]) / (x_data[pos[i]] - x_data[pos[j]])
        return L

    P = 0.0

    for i in range(n):
            P += f_data[pos[i]] * L(x_data, pos, x)[i]

    return P

if __name__ == "__main__":
    # Some Data
    x_data = [-1.6, -1.0, -0.4, 0.2, 0.8, 1.4]
    f_data = [0.278037, 0.606531, 0.923116, 0.980199, 0.726149, 0.375311]

    print('Compuated with Lagrange Polynomials of 3rd DegreeQ')
    print(f'\tf(0) = {P(x_data, f_data, [1, 2, 3, 4], 0):.6f}')
    print(f'\tf(1) = {P(x_data, f_data, [2, 3, 4, 5], 1):.6f}')
