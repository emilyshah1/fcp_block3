import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

X = 50
Y = 50

def diff_lv(xy, t, alpha, beta, delta, gamma):
    dxdt = (alpha * xy[0]) - (beta * xy[0] * xy[1])
    dydt = (delta * xy[0] * xy[1]) - (gamma * xy[1])
    return [dxdt, dydt]

def solve_lv(xy0, t_max, alpha, beta, delta, gamma):
    t = np.linspace(0, t_max)
    xy = odeint(diff_lv, xy0, t, args=(alpha, beta, delta, gamma))
    return xy, t

def plot_lv(t, data):
    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(t, data[:, 0], label='X(t)')
    ax2 = fig.add_subplot(212)
    ax2.plot(t, data[:, 1], label='Y(t)')
    ax1.legend()
    ax2.legend()

    plt.show()

def main():
    alpha = 0.4
    beta = 0.1
    delta = 0.2
    gamma = 0.3

    t_max = 100

    xy0 = (X, Y)
    xy, t = solve_lv(xy0, t_max, alpha, beta, delta, gamma)

    plot_lv(t, xy)

if __name__ == "__main__":
    main()



