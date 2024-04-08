import saga                      # import the test suite

#saga.test_basesampler(0, 14)

mu = -0.920619
sigma = 1.711864
data = [-1, 2, -4, 0, -2, 1, -2, -3, -1, 1, -1, 0, 0, 1, -4, -1, -2, -2, -1, 0, 1, -1, 2, -3, 2, 0, -1, -2, 0, -3, -1, -2, -1, 1, -5, -1, -2, -2, -1, 0, 2, 1, 0, 0, 1, -1, -2, -2, -1, 0, 2, -2, -1, -3, 0, 0, 0, -2, 0, 0, 0, -3, -4, 0, 1, -1, 0, -1, 1, -3, 0, 0, -3, 0, -4, -1, -2, 0, 0, -2, -2, -1, 1, -1, 0, -2, -2, -2, 0, -1, -4, -2, 0, -2, -2, 1, -1, 0, -3, -1]

res = saga.UnivariateSamples(mu, sigma, data)
print(res)