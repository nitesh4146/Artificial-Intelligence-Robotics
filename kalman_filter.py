from math import *


def f(mu, sigma2, x):
    return (1/sqrt(2*pi*sigma2)) * exp(-0.5 * pow(x-mu, 2)/sigma2)

print(f(10, 4, 10))


def update(mean1, var1, mean2, var2):
    new_mean = (mean1*var2 + mean2*var1)/(var1+var2)
    new_var = 1/((1/var1)+(1/var2))
    return [new_mean, new_var]

print(update(10., 4., 12., 4.))


def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

print(predict(10, 4, 12, 4))


measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for i in range(len(measurements)):
    [mu, sig] = update(mu, sig, measurements[i], measurement_sig)
    [mu, sig] = predict(mu, sig, motion[i], motion_sig)

print([mu, sig])
