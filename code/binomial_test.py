import qrng_wrapper
import math
import saga
from decimal import *


p = 0.5
n = 100
nb_samples = 100

mu = n*p
sigma = math.sqrt(n*p*(1-p))

binomial_samples = qrng_wrapper.wrapper.binomial_sample(nb_samples, n, p)

test_res = saga.UnivariateSamples(mu, sigma, binomial_samples)
print(test_res)

