# Exercício 11 (Taha 2008 8ed pag 10)

from mip import Model, xsum, maximize

# Dados de entrada
A  = ['E', 'D'] # Conjunto de atividades
T = 10 # Tempo disponível no dia (horas)
LSa = {'E': T, 'D': 4} # Limite superior da atividade a ∈ A (horas)

# Modelo
model = Model("Maximizar o tempo destinado a se divertir")

# Variáveis de decisão: xa → Tempo diário destinado à atividade a ∈ A (horas)
# var_type="I" --> indica que as variáveis são valores inteiros
# lb=0 --> indica que as variáveis não podem ser negativas
x = {a: model.add_var(name=f"x_{a}", var_type="C", lb=0) for a in A}

# Função objetivo: Maximizar o tempo destinado a se divertir
model.objective = maximize(xsum(x[a] for a in A))

# Restrição: Total de horas disponíveis no dia
model += xsum(x[a] for a in A) <= T

# Restrição: Limite superior
for a in A:
    model += x[a] <= LSa[a]

# Restrição: Estudar pelo menos o mesmo tempo que se dedica à diversão
model += x['E'] >= x['D']

# Resolver o modelo
model.optimize()

# Exibir os resultados
print("\n\nStatus:", model.status)
for a in A:
    print(f"Horas destinadas à atividade {a}: {x[a].x}")
