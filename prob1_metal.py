# Problema 1 - Problema da Produção de Ligas Metálicas

from mip import Model, xsum, maximize, BINARY

# Dados de entrada
M = ['Cobre','Zinco','Chumbo'] # Conjunto de materiais
L = ['Alta resistência', 'Baixa resistência'] # Conjunto de ligas especiais
Dm = {'Cobre': 16, 'Zinco': 11, 'Chumbo': 15}  # Disponibilidade do material m ∈ M (toneladas)
Pl = {'Alta resistência': 5000, 'Baixa resistência': 3000}  # Preço por tonelada da liga especial l ∈ L (reais)
Qml = {  # Quantidade do material m ∈ M na composição da liga especial  l ∈ L
    ('Cobre', 'Alta resistência'): 0.2,
    ('Cobre', 'Baixa resistência'): 0.5,
    ('Zinco', 'Alta resistência'): 0.3,
    ('Zinco', 'Baixa resistência'): 0.25,
    ('Chumbo', 'Alta resistência'): 0.5,
    ('Chumbo', 'Baixa resistência'): 0.25
}

# Modelo
model = Model("Maximizar a receita bruta das ligas especiais produzidas")

# Variáveis de decisão: xl → toneladas produzidas da liga especial l
x = {l: model.add_var(name=f"x_{l}", var_type="C", lb=0) for l in L}

# Função objetiva: Maximizar receita bruta das ligas produzidas
model.objective = maximize(xsum(Pl[l] * x[l] for l in L))

# Restrições: Disponibilidade de materiais
for m in M:
    model += xsum(x[l] * Qml.get((m, l), 0) for l in L) <= Dm[m], f"Disponibilidade_{m}"

# Resolver o modelo
model.optimize()

# Exibir os resultados
print("\n\nStatus:", model.status)
print("Receita Bruta Máxima:", model.objective_value)
for l in L:
    print(f"Toneladas produzidas da {l}: {x[l].x}")