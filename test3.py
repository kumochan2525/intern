from turtle import *
from math import atan2

def lorenz(sigma, beta, rho):
    dt = 0.01
    scale = 10
    x, y, z = (1, 1, 1)
    dx, dy = (0, 0)
    while True:
        setpos(x*scale, y*scale)
        setheading(atan2(dy, dx))
        
        dx = (sigma*(y-x)) * dt
        dy = (x*(rho-z)-y) * dt

        x += dx
        y += dy
        z += (x*y - beta*z) * dt


if __name__ == '__main__':
    tracer(10000,0)
    lorenz(10, 8/3, 28)