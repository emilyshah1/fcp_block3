import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np

N = 1000
S = N-1
I = 1
R = 0

def diff_sir(sir, t, beta, gamma):
    '''
    calculates the gradient for an SIR model of disease spread
    Inputs:
        sir: state of the system, with sir[0] = number susceptible
                                                                sir[1] = number infected
                                                                sir[2] = number recovered
        t: current time - not used her, but odeint expects to pass this argument so we must include it
        beta: the rate at which the virus spreads
        gamma: the rate at which people are removed due to the virus
    Outputs:
        the gradient of the SIR model
    '''
    dsdt = (-beta*sir[0] * sir[1])/N
    didt = (beta*sir[0]*sir[1])/N - (gamma * sir[1])
    drdt = gamma * sir[1]

    grad = [dsdt, didt, drdt]

    return grad

def solve_sir(sir0, t_max, beta, gamma):
    '''
    Solves an SIR model using odeint
    '''
    
    t = np.linspace(0, t_max)
    sir = odeint(diff_sir, sir0, t, (beta, gamma))

    return sir, t

def plot_sir(t, data):

    fig = plt.figure()
    ax1 = fig.add_subplot(311)
    ax1.plot(t, data[:, 0], label='S(t)')
    ax2 = fig.add_subplot(312)
    ax2.plot(t, data[:, 1], label='I(t)')
    ax3 = fig.add_subplot(313)
    ax3.plot(t, data[:, 2], label='R(t)')
    plt.show()

    return t, data

def main():

    beta = 0.4
    gamma = 0.2
    t_max = 100

    sir0 = (S, I, R)
    sir, t = solve_sir(sir0, t_max, beta, gamma)
    plot_sir(t, sir)

if __name__ == "__main__":
    main()