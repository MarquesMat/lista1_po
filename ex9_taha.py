# Exercício 9 (Taha 2008 8ed pag 10)

from mip import Model, xsum, maximize

# Dados de entrada
M = ['I', 'II'] # Conjunto dos tipos de matérias-primas
P = ['A', 'B'] # Conjunto dos produtos de limpeza
Dm = {'I': 150, 'II': 145} # Disponibilidade diária de m ∈ M 
Cpm = {  # Quanto uma unidade do produto p ∈ P consome da matéria-prima m ∈ M (unidades)
    ('A', 'I'): 0.5,
    ('A', 'II'): 0.6,
    ('B', 'I'): 0.5,
    ('B', 'II'): 0.4
}
Lp = {'A': 8, 'B': 10} # Lucro de venda da unidade do produto p ∈ P (reais)
LIDp = {'A': 30, 'B': 40} # Limite inferior da demanda diária do produto p ∈ P (unidades)
LSDp = {'A': 150, 'B': 200} # Limite superior da demanda diária do produto p ∈ P (unidades)

# Modelo
model = Model("Maximizar o lucro com as vendas dos produtos")

# Variáveis de decisão: xi → quantidade do capital investido em i ∈ I (em reais)
# var_type="I" --> indica que as variáveis são valores inteiros
# lb=0 --> indica que as variáveis não podem ser negativas
x = {p: model.add_var(name=f"x_{p}", var_type="I", lb=0) for p in P}

# Função objetivo: Maximizar o ganho com os investimentos
model.objective = maximize(xsum(Lp[p] * x[p] for p in P))

# Restrição: Disponibilidade de matéria-prima
for m in M:
    model += xsum(x[p] * Cpm[(p,m)] for p in P) <= Dm[m], f"disponibilidade_materia_{m}"

# Restrição: Limite inferior
for p in P:
    model += x[p] >= LIDp[p], f"lim_inf_{LIDp[p]}_para_{x[p]}"

# Restrição: Limite superior
for p in P:
    model += x[p] <= LSDp[p], f"lim_sup_{LSDp[p]}_para_{x[p]}"

# Resolver o modelo
model.optimize()

# Exibir os resultados
print("\n\nStatus:", model.status)
print("Lucro Máximo:", model.objective_value)
for p in P:
    print(f"Unidades produzidas diariamente do produto {p}: {x[p].x}")
