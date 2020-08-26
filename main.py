# Dependências

import random 
import time

# Métodos utilitários

def gerarBooleanRandomico():
  return bool(random.getrandbits(1))

def gerarIntRandomico(inicio, fim):
  return random.randint(inicio,fim)

# Constantes

NUMERO_MAXIMO_DE_CHAMADAS = 3
NUMERO_INICIAL_DE_CHAMADAS = 0
PRESENCA = False

# Classe que irá representar o objeto Aluno

class Aluno:

    def __init__(self, nome):
        self.nome = nome
        self.jaRespondeuAChamada = PRESENCA
        self.numeroDeVezesQueFoiChamado = NUMERO_INICIAL_DE_CHAMADAS

    def getNome(self):
        return self.nome

    def verificaSeEstaPresente(self):
        return self.jaRespondeuAChamada
    
    def atualizarChamada(self, respostaDaChamada):
        self.jaRespondeuAChamada = respostaDaChamada

    def quantasVezesFoiChamado(self):
        return self.numeroDeVezesQueFoiChamado
    
    def atualizarNumeroDeChamadas(self):
        self.numeroDeVezesQueFoiChamado += 1

def getAlunos():
  listaDeAlunos = []

  arquivo = open('alunos.txt', 'r')
  for nomeAluno in arquivo:
      nomeAlunoSemEspaco = nomeAluno.strip()
      listaDeAlunos.append(Aluno(nomeAlunoSemEspaco))
  arquivo.close()
  
  return listaDeAlunos

def getAluno(listaDeAlunos):
  indice = gerarIntRandomico(0, len(listaDeAlunos) - 1)
  aluno = listaDeAlunos[indice]
  return aluno

def getHorario(numAlunos, quantidadeChamada, duracaoAula):
  horario = duracaoAula / numAlunos
  horario = horario / quantidadeChamada
  return horario

listaDeAlunos = getAlunos()

numAlunos = len(listaDeAlunos)
quantidadeChamada = NUMERO_MAXIMO_DE_CHAMADAS
duracaoAula = 10

horario = getHorario(numAlunos, quantidadeChamada, duracaoAula)

while duracaoAula > 0:
 aluno = getAluno(listaDeAlunos)
 if(aluno.verificaSeEstaPresente() == False and aluno.quantasVezesFoiChamado() < NUMERO_MAXIMO_DE_CHAMADAS):
   duracaoAula = duracaoAula - horario

   aluno.atualizarNumeroDeChamadas()
   aluno.atualizarChamada(gerarBooleanRandomico())
   
   print(aluno.getNome(), "Respondeu a chamada: ", (aluno.verificaSeEstaPresente() and "Sim" or "Não"))
   
   time.sleep(horario)
