# Exercício 10 (Taha 2008 8ed pag 10)

from mip import Model, xsum, maximize

# Dados de entrada
E = 60 # Espaço total de prateleira (pés2)
C  = ['G', 'W'] # Conjunto dos itens de cereal
Oc = {'G': 0.2, 'W': 0.4} # Espaço ocupado por uma caixa do item c ∈ C (pés2)
Dc = {'G': 200, 'W': 120} # Demanda diária máxima do item c ∈ C (caixas)
Lc = {'G': 1, 'W': 1.35} # Lucro líquido por caixa do item c ∈ C (reais)

# Modelo
model = Model("Maximizar o lucro com as vendas dos cereais")

# Variáveis de decisão: xc → Unidades disponibilizadas diariamente do item c ∈ C
# var_type="I" --> indica que as variáveis são valores inteiros
# lb=0 --> indica que as variáveis não podem ser negativas
x = {c: model.add_var(name=f"x_{c}", var_type="I", lb=0) for c in C}

# Função objetivo: Maximizar o lucro com as vendas dos cereais
model.objective = maximize(xsum(Lc[c] * x[c] for c in C))

# Restrição: Espaço das prateleiras
model += xsum(x[c] * Oc[c] for c in C) <= E

# Restrição: Demanda diária
for c in C:
    model += x[c] <= Dc[c]

# Resolver o modelo
model.optimize()

# Exibir os resultados
print("\n\nStatus:", model.status)
print("Lucro Máximo:", model.objective_value)
for c in C:
    print(f"Unidades disponibilizadas diariamente do cereal {c}: {x[c].x}")
