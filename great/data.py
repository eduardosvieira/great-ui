
class Turma:
    def __init__(self, id, name, disciplina, ano,vagas):
      self.id = id
      self.name = name
      self.disciplina = disciplina
      self.ano =ano
      self.vagas =vagas


class Disciplina:
    def __init__(self, id, name):
      self.id = id
      self.name = name

class Topico:
    def __init__(self, id, name, disciplina):
      self.id = id
      self.name = name
      self.disciplina = disciplina

class Participante:
    def __init__(self, id, name, ultimo_acesso, pontuacao, desempenho):
      self.id = id
      self.name = name
      self.ultimo_acesso = ultimo_acesso
      self.pontuacao = pontuacao
      self.desempenho = desempenho

class Tarefa:
    def __init__(self, id, name, prazo):
      self.id = id
      self.name = name
      self.prazo = prazo

def create_turmas():
    turmas=[]
    t1 = Turma(1,'FC - T02','FUNDAMENTO DE COMPUTAÇÃO','2017.2',33)
    t2 = Turma(2,'SO - T01','SISTEMAS OPERACIONAIS','2017.2',60)
    t3 = Turma(3,'SO - T02','SISTEMAS OPERACIONAIS','2017.2',60)

    turmas.append(t1)
    turmas.append(t2)
    turmas.append(t3)
    return turmas #render_template("modulos/classroom/index.html",turmas=turmas)


def create_disciplinas():
    disciplinas=[]
    t1 = Disciplina('CCCT0006','FUNDAMENTOS DE COMPUTAÇÃO')
    t2 = Disciplina('CCCT0087','SISTEMAS OPERACIONAIS')

    disciplinas.append(t1)
    disciplinas.append(t2)

    return disciplinas #render_template("modulos/classroom/index.html",turmas=turmas)


def create_tarefas():
    tarefas=[]
    t1 = Tarefa(1,'Exercícios - Entrada / Saída de Dados','May 8, 2018 at 11:55 PM')
    t2 = Tarefa(2,'Exercícios - Estruturas Condicionais', 'May 22, 2018 at 12:00 PM')
    t3 = Tarefa(3,'Exercícios - Estruturas de Repetição','	May 22, 2018 at 12:00 PM')

    tarefas.append(t1)
    tarefas.append(t2)
    tarefas.append(t3)

    return tarefas #render_template("modulos/classroom/index.html",turmas=turmas)


def create_topicos():
    topicos=[]
    topicos.append(Topico('1','HISTÓRICO E EVOLUÇÃO DOS COMPUTADORES','CCCT0006'))
    topicos.append(Topico('2','ARQUITETURA DE COMPUTADORES','CCCT0006'))
    topicos.append(Topico('3','SISTEMA NUMÉRICO','CCCT0006'))
    topicos.append(Topico('4','ARITMÉTICA BINÁRIA','CCCT0006'))
    topicos.append(Topico('5','ÁLGEBRA BOOLEANA','CCCT0006'))
    topicos.append(Topico('6','INTRODUÇÃO À ALGORÍTMOS','CCCT0006'))
    topicos.append(Topico('7','VARIÁVEIS E ATRIBUIÇÃO','CCCT0006'))
    topicos.append(Topico('8','ENTRADA DE DADOS','CCCT0006'))
    topicos.append(Topico('9','ESTRUTURAS CONDICIONAIS','CCCT0006'))
    topicos.append(Topico('10','ESTRUTURAS DE REPETIÇÃO','CCCT0006'))
    topicos.append(Topico('11','OPERAÇÕES SOBRE STRINGS','CCCT0006'))
    topicos.append(Topico('12','OPERAÇÕES SOBRE LISTAS ','CCCT0006'))
    topicos.append(Topico('13','FUNÇÕES: VARIÁVEIS LOCAIS E GLOBAIS, PASSAGEM DE PARÂMETROS','CCCT0006'))

    return topicos #render_template("modulos/classroom/index.html",turmas=turmas)

def create_participantes():
    participantes=[]
    p1 = Participante(1,'ALANA DE ARAUJO OLIVEIRA','2 dias atrás',100, 33)
    p2 = Participante(2,'MARIO ANTONIO MEIRELES TEIXEIRA','35 minutos',200,60)
    p3 = Participante(3,'CARLOS DE SALLES SOARES NETO','nunca acessou',0, 0)

    participantes.append(p1)
    participantes.append(p2)
    participantes.append(p3)
    return participantes
