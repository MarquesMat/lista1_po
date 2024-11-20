# Exercício 7 (Taha 2008 8ed pag 9)

from mip import Model, xsum, maximize

# Dados de entrada
C = 5000 # Capital disponível para investimentos (reais)
I = ['A', 'B'] # Conjunto de investimentos
Ri = {'A': 0.05, 'B': 0.08} # Rendimento do investimento i ∈ I (em porcentagem)
LIi = {'A': 0.25, 'B': 0} # Limite inferior do investimento i ∈ I (em porcentagem)
LSi = {'A': 1, 'B': 0.5} # Limite superior do investimento i ∈ I (em porcentagem)

# Modelo
model = Model("Maximizar o ganho com os investimentos")

# Variáveis de decisão: xi → quantidade do capital investido em i ∈ I (em reais)
# var_type="C" --> indica que as variáveis são valores contínuos
# lb=0 --> indica que as variáveis não podem ser negativas
x = {i: model.add_var(name=f"x_{i}", var_type="C", lb=0) for i in I}

# Função objetivo: Maximizar o ganho com os investimentos
model.objective = maximize(xsum(Ri[i] * x[i] for i in I))

# Restrição: Capital disponível
model += xsum(x[i] for i in I) <= C

# Restrição: Limite inferior
for i in I:
    model += x[i] >= LIi[i]*C, f"lim_inf_{LIi[i]}"

# Restrição: Limite superior
for i in I:
    model += x[i] <= LSi[i]*C, f"lim_sup_{LIi[i]}"

# Resolver o modelo
model.optimize()

# Exibir os resultados
print("\n\nStatus:", model.status)
print("Lucro Máximo:", model.objective_value)
for i in I:
    print(f"Quantia investida em {i}: {x[i].x}")
