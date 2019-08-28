from time import sleep
from redis import Redis, StrictRedis
import numpy
from rq import Queue
from redis_modules import cria_matriz, multiplica_linha_coluna

if __name__ == "__main__":
  linhas, colunas = 2, 2

  matrizA = cria_matriz(linhas, colunas)
  matrizB = cria_matriz(colunas, linhas)
  # matrizA = [[2, 3], [4, 5]]
  # matrizB = [[6, 7], [8, 9]]
  matrizA = numpy.array(matrizA)
  matrizB = numpy.array(matrizB)
  matrizC = numpy.zeros(shape=(linhas, colunas))

  redis_conn = Redis(host='127.0.0.1',port=6379)
  queue_jobs = Queue('my_queue', connection=redis_conn)
  jobs = []

  for i in range(len(matrizA)):
    jobLocal = []
    for j in range(len(matrizA[0])):
      job = queue_jobs.enqueue(multiplica_linha_coluna, matrizA[i], matrizB[:, j])
      jobLocal.append(job)
    jobs.append(jobLocal)

  for i in range(len(matrizA)):
    for j in range(len(matrizA[0])):
      while jobs[i][j].result is None:
        sleep(2)
      matrizC[i][j] = jobs[i][j].result

  print matrizC

