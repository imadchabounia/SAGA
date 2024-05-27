import qrng_wrapper
import math
import saga
from decimal import *

mu = -0.920619
sigma = 1.711864

def gaussian(mu: float, sigma: float, x: int):
  """
    Gaussian function of center mu and "standard deviation" sigma.
  """
  return Decimal(math.exp(-((Decimal(x) - Decimal(mu))**2)/(Decimal(2*sigma*sigma))))
  
def make_discrete_gaussian_pdt(mu: float, sigma: float):
  """
    Make the probability distribution table (PDT) of a discrete Gaussian.
    The output is a dictionary.
  """
  c = 0
  tau = 14
  zmax = math.ceil(tau * sigma)
  for i in range(int(math.floor(mu)) - zmax, int(math.ceil(mu)) + zmax):
    c = Decimal(c) + Decimal(gaussian(mu, sigma, i))
  pdt_table = []

  for i in range(int(math.floor(mu)) - zmax, int(math.ceil(mu)) + zmax):
    rho_de_i = gaussian(mu, sigma, i)
    pdt_table.append([i, rho_de_i/c])
  
  return pdt_table

pdt = make_discrete_gaussian_pdt(mu, sigma)

nb_samples = 100

n_tests = 15
passed_cnt = 0
print("[+] Running 15 tests :")
for i in range(n_tests):
  qrng_samples = qrng_wrapper.wrapper.custom_pdf_sample(pdt, nb_samples)
  res = saga.UnivariateSamples(mu, sigma, qrng_samples)
  #print(res)
  if res.is_valid:
    print("Test #" + str(i+1) + " Passed ...")
    passed_cnt = passed_cnt + 1
  else:
    print("Test #" + str(i+1) + " Failed ...")

print(str(passed_cnt) + "/" + str(n_tests) + " Passed")
