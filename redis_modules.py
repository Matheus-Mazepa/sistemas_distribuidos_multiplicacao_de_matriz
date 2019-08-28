from time import sleep
import random
from redis import Redis

def cria_matriz(linhas, colunas):
  A = []
  for i in range(linhas):
    linha = []
    for j in range(colunas):
      linha = linha + [random.randint(1, 10)]
    A = A + [linha]
  return A

def multiplica_linha_coluna(matrizA, matrizB):
  # redisClient = Redis(host='127.0.0.1', port=6379)
  #
  # print redisClient.hget("matriz", "matrizA")
  valor = 0
  for k in range(len(matrizB)):
    valor = valor + matrizA[k] * matrizB[k]
  return valor