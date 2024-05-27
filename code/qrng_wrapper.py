import requests
import math


#This is a wrapper class that we created to facilitate the interaction with aQRNG

class QRNGwrapper:
  
  qci_url = "https://api.qci-next.com"
  access_token = f""

  def __init__(self):
    #basic credentials
    f = open("qci_access_token.token", "r")
    access_token = f"{f.read()}"

    #auth
    json_data = {
    "access_token": f"{access_token}",
    }
    headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    }
    response=requests.post(
    f"{self.qci_url}/authorize",
    headers=headers,
    json=json_data)
    response_json = response.json()
    self.access_token = response.json().get("access_token")


  def custom_pdf_sample(self, pdf: list, nb_samples) -> list:
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {self.access_token}",
    "Content-Type": "application/json",
    }
    json_data = {
    "distribution": "custom",
    "output_type": "decimal",
    "n_samples": nb_samples,
    "pdf": pdf
    }
    response = requests.post(
    f"{self.qci_url}/qrng/random_numbers",
    headers=headers,
    json=json_data)
    json_list = response.json()
    return list([json_list[i] for i in range(len(json_list))])
  
  def guassian_sample(self, nb_samples: int, mu: int, sigma: int):
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {self.access_token}",
    "Content-Type": "application/json",
    }
    json_data={
    "distribution" : "gaussian",
    "n_samples" : nb_samples,
    "mu" : mu,
    "sigma" : sigma}
    response = requests.post(
    f"{self.qci_url}/qrng/random_numbers",
    headers=headers,
    json=json_data)
    
    response = requests.post(
    f"{self.qci_url}/qrng/random_numbers",
    headers=headers,
    json=json_data)
    json_list = response.json()
    #print(json_list)
    return list([json_list[i] for i in range(len(json_list))])
  
  def binomial_sample(self, nb_samples: int, n: int, p: float):
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {self.access_token}",
    "Content-Type": "application/json",
    }
    json_data={
    "distribution" : "bernoulli",
    "n_samples" : n*nb_samples,
    "prob": p}
    response = requests.post(
    f"{self.qci_url}/qrng/random_numbers",
    headers=headers,
    json=json_data)
  
    response = requests.post(
    f"{self.qci_url}/qrng/random_numbers",
    headers=headers,
    json=json_data)
    json_list = response.json()
    bernoulli_samples = list([json_list[i] for i in range(len(json_list))])
    binomial_samples = [sum(bernoulli_samples[i: i+n]) for i in range(0, n*nb_samples, n)]
    return binomial_samples
    
  """
    This function retrun a list of @nb_samples random integers of size @nb_bits according to discrete uniform distribution  
  """
  def randint_qrng(self, nb_bits:int, nb_samples: int) -> list:
    #nb_bits is aribtrary
    nb_bits_from_api = 8
    nb_samples_from_api = math.ceil((nb_samples * nb_bits) / nb_bits_from_api)
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {self.access_token}",
    "Content-Type": "application/json",
    }
    json_data = {
    "distribution": "uniform_discrete",
    "output_type": "binary",
    "n_samples": nb_samples_from_api,
    "n_bits": nb_bits_from_api
    }
    response = requests.post(
    f"{self.qci_url}/qrng/random_numbers",
    headers=headers,
    json=json_data)
    json_list = response.json()
    stream_of_bits = ''.join(json_list)
    samples_bin = [stream_of_bits[i:i+nb_bits] for i in range(0, len(stream_of_bits), nb_bits)]
    return list([int(samples_bin[i], 2) for i in range(len(samples_bin))])

wrapper = QRNGwrapper()