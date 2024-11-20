# Exercício 6 (Taha 2008 8ed pag 9)

from mip import Model, xsum, maximize

# Dados de entrada
T = ['C', 'B']  # Conjunto dos tipos de peças de alumínio produzidas (C = chapa, B = barra)
Lt = {'C': 40, 'B': 35}  # Lucros unitários por produto
Ct = {'C': 800, 'B': 600}  # Capacidade máxima de produção do tipo t ∈ T por dia
Dt = {'C': 550, 'B': 580} # Demanda máxima diária do tipo t ∈ T

# Modelo
model = Model("Maximizar Lucro")

# Variáveis de decisão: xt → Quantidade produzida diariamente do produto i
# var_type="I" --> indica que as variáveis são valores inteiros
# lb=0 --> indica que as variáveis não podem ser negativas
x = {t: model.add_var(name=f"x_{t}", var_type="I", lb=0) for t in T}

# Função objetivo: Maximizar o lucro com a venda dos produtos
model.objective = maximize(xsum(Lt[t] * x[t] for t in T))

# Restrição: Demanda máxima diária
for t in T:
    model += x[t] <= Dt[t], f"Demanda_Max_{t}"

model += (x['C'] / 800) + (x['B'] / 600) <= 1, "Restricao_Relacionada"  # Restrição do uso total

# Resolver o modelo
model.optimize()

# Exibir os resultados
print("\n\nStatus:", model.status)
print("Lucro Máximo:", model.objective_value)
for t in T:
    print(f"Quantidade produzida de {t}: {x[t].x}")
