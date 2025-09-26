import numpy as np
import skfuzzy as fuzz
from utils import fuzz_p

""" 
=> Exercício 4 - Assistente de Sono
TODO: alto AND pouco == forçar pausa
TODO: baixo AND adequado == manter alerta
"""

x_cansaco = np.arange(0,11,1)   
x_sono = np.arange(0,13,1)       
x_acao = np.arange(0,11,1)      

# ? Funções de pertinência do cansaço
baixo = fuzz.trimf(x_cansaco, [0,0,4])
medio = fuzz.trimf(x_cansaco, [3,5,7])
alto = fuzz.trimf(x_cansaco, [6,10,10])

# ? Funções de pertinência do sono
pouco = fuzz.trimf(x_sono, [0,0,5])
adequado = fuzz.trimf(x_sono, [4,7,9])
muito = fuzz.trimf(x_sono, [8,12,12])

# ? Funções de pertinência da ação
alerta = fuzz.trimf(x_acao, [0,0,4])
descanso = fuzz.trimf(x_acao, [3,6,8])
pausa = fuzz.trimf(x_acao, [7,10,10])

# * inputs
cansaco = 8   # nível de cansaço
sono = 4      # horas de sono

# TODO: criação das pertinencias

# ? cansaço
p_baixo = fuzz_p(x_cansaco, baixo, cansaco)
p_medio = fuzz_p(x_cansaco, medio, cansaco)
p_alto = fuzz_p(x_cansaco, alto, cansaco)

# ? sono
p_pouco = fuzz_p(x_sono, pouco, sono)
p_adequado = fuzz_p(x_sono, adequado, sono)
p_muito = fuzz_p(x_sono, muito, sono)

# TODO: Aplicação das regras

regra1 = np.fmin(p_alto, p_pouco)     # alto AND pouco == forçar pausa
regra2 = np.fmin(p_baixo, p_adequado) # baixo AND adequado == alerta

# ! ativacao das regras
r1_ativado = np.fmin(regra1, pausa)
r2_ativado = np.fmin(regra2, alerta)

# TODO: agregação das regras
acao = np.fmax(r1_ativado, r2_ativado)

# TODO: defuzzificação

resultado = fuzz.defuzz(x_acao, acao, 'centroid')

print("")
print(f"Grau de pertinência do cansaço baixo: {p_baixo:.2f}")
print(f"Grau de pertinência do cansaço médio: {p_medio:.2f}")
print(f"Grau de pertinência do cansaço alto: {p_alto:.2f}")
print("")
print(f"Grau de pertinência do sono pouco: {p_pouco:.2f}")
print(f"Grau de pertinência do sono adequado: {p_adequado:.2f}")
print(f"Grau de pertinência do sono muito: {p_muito:.2f}")
print("")

if resultado <= 3:
    c = "manter alerta"
elif resultado <= 6:
    c = "descansar"
else:
    c = "forçar pausa"
print(f"Ação sugerida: {resultado:.2f} → {c}")
