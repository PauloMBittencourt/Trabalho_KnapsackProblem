import random
import numpy
from deap import creator, base, tools, algorithms

#Definindo variaveis de peso, numero total de itens e numero de gerações
Peso_Max = 40
Numero_Itens = 20
NGEN = 50
#Print do peso max da mochila
print("Esse é o peso maximo da mochila:")
print(Peso_Max)
print("-" * 500)

#Criando a função para gerar itens aleatorios
def createItens(Numero_Itens):
  itens = []
  for x in range(Numero_Itens):
    itens.append({"Peso": random.randint(1, 10), "Valor": random.uniform(1, 100)})
  return itens

#Chamando a função para gerar os itens e coloca-los dentro de uma lista
itens = createItens(20)
print("Itens que foram criados:\n")
for item in items:
    print(item)
print("-" * 500)

#Definindo a Fitness
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

#Definindo o individuo
creator.create("Individuo",list, fitness = creator.FitnessMax)

#Inicializando a toolbox
toolbox = base.Toolbox()

#Criando um atributo booleano aleatorio
toolbox.register("attr", random.random)

#Criando um Individuo 
toolbox.register("individuo", tools.initRepeat, 
                 creator.Individuo, toolbox.attr, n = 5)

#Criando uma população
toolbox.register("populacao", tools.initRepeat, list, toolbox.individuo)

#Criando a função que recebe um indivíduo e retorna uma tupla
def evalIten(individuo):
  weight = 0.0
  value = 0.0
  for item in range(len(individuo)):
    if individuo[item] > 0.5:
      weight += itens[item]["Peso"]
      value += itens[item]["Valor"]
    if weight > Peso_Max:
      return 10000, 0
    return weight, value

#Criando a função para pegar itens 
def getItens(individuo):
  pegarItem = []
  for x in range(len(individuo)):
    if individuo[x] > 0.5:
      pegarItem.append((x, itens[x]))
  return pegarItem


#Registrando a função de fitness
toolbox.register("evaluate", evalIten)

#Criando os operadoes do crossover e mutação
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb = 0.05)

#Criando o método do select
toolbox.register("select", tools.selNSGA2)

#Criando o tamanho da população
population = toolbox.populacao(n=300)

#Criando e inicializando o processo de evolução
for gen in range(NGEN):

  offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

  fits = toolbox.map(toolbox.evaluate, offspring)

  for fit, ind in zip(fits, offspring):
        ind.fitness.values = [fit[1]]

  population = toolbox.select(offspring, k=len(population)) 

#Criandp uma variavel que pega os 10 melhores da ultima posição
top10 = tools.selBest(population, k=10)

#Prints 
print("Esse é o melhor Individuo da ultima posição:\n")
print(top10[0])
print("-" * 500)

itemPegar = getItens(top10[0])
print("Itens listados por Peso e Valor")
for item in itemPegar:
    print(item)