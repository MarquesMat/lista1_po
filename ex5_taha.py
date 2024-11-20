# Exercício 5 (Taha 2008 8ed pag 9)

from mip import Model, xsum, maximize

# Dados de entrada
P = ['A', 'B']  # Conjunto dos produtos produzidos
LVp = {'A': 100, 'B': float('inf')}  # Limite de vendas do produto p ∈ P por dia (unidades)
M = 240  # Disponibilidade de matéria-prima (em lb)
Qp = {'A': 2, 'B': 4}  # Quantidade de matéria-prima usada por produto (em lb)
Lp = {'A': 20, 'B': 50}  # Lucros unitários (reais)

# Modelo
model = Model("Maximizar Lucro")

# Variáveis de decisão: xp → Quantidade fabricada diariamente do produto p
x = {p: model.add_var(name=f"x_{p}", var_type="I", lb=0) for p in P}

# Função objetivo: Maximizar o lucro com a venda dos produtos
model.objective = maximize(xsum(x[p] * Lp[p] for p in P))

# Restrição: Limite de vendas por produto
for p in P:
    model += x[p] <= LVp[p], f"Limite_de_vendas_{p}"

# Restrição: Consumo total de matéria-prima não pode exceder a disponibilidade
model += xsum(x[p] * Qp[p] for p in P) <= M, "Disponibilidade_de_materia_prima"

# Restrição: As vendas de A devem ser no mínimo 80% das vendas totais
model += x['A'] >= 0.8 * xsum(x[p] for p in P), "Restricao_80_percento_vendas_Produto1"

# Resolver o modelo
model.optimize()

# Exibir os resultados
print("\n\nStatus:", model.status)
print("Lucro Máximo:", model.objective_value)
for p in P:
    print(f"Quantidade fabricada do {p}: {x[p].x}")
