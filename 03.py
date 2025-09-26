import numpy as np
import skfuzzy as fuzz
from utils import fuzz_p

""" 
=> Exercício 3 - Controle de Irrigação
TODO: seca AND alta -> intensa
"""

x_umidade = np.arange(0,101,1)     
x_temp = np.arange(0,41,1)         
x_irrigacao = np.arange(0,11,1)    

# ? Funções de pertinência da umidade
seca = fuzz.trimf(x_umidade, [0,0,50])
media = fuzz.trimf(x_umidade, [30,50,70])
umida = fuzz.trimf(x_umidade, [60,100,100])

# ? Funções de pertinência da temperatura
baixa = fuzz.trimf(x_temp, [0,0,15])
media_t = fuzz.trimf(x_temp, [10,20,30])
alta = fuzz.trimf(x_temp, [25,40,40])

# ? Funções de pertinência da irrigação
pouca = fuzz.trimf(x_irrigacao, [0,0,4])
moderada = fuzz.trimf(x_irrigacao, [3,6,8])
intensa = fuzz.trimf(x_irrigacao, [6,10,10])

# * inputs
umidade = 25   
temp = 33      

# TODO: criação das pertinencias

# ? umidade
p_seca = fuzz_p(x_umidade, seca, umidade)
p_media = fuzz_p(x_umidade, media, umidade)
p_umida = fuzz_p(x_umidade, umida, umidade)

# ? temperatura
p_baixa = fuzz_p(x_temp, baixa, temp)
p_media_t = fuzz_p(x_temp, media_t, temp)
p_alta = fuzz_p(x_temp, alta, temp)

# TODO: Aplicação das regras

regra1 = np.fmin(p_seca, p_alta)   # seca AND alta == intensa

# ! ativacao das regras
r1_ativado = np.fmin(regra1, intensa)

# TODO: defusando
irrigacao = r1_ativado  # só uma regra
if np.max(irrigacao) == 0:
    print("Nenhuma regra ativada.")
else:
    resultado = fuzz.defuzz(x_irrigacao, irrigacao, 'centroid')

    print("")
    print(f"Grau de pertinência da umidade seca: {p_seca:.2f}")
    print(f"Grau de pertinência da umidade média: {p_media:.2f}")
    print(f"Grau de pertinência da umidade úmida: {p_umida:.2f}")
    print("")
    print(f"Grau de pertinência da temperatura baixa: {p_baixa:.2f}")
    print(f"Grau de pertinência da temperatura média: {p_media_t:.2f}")
    print(f"Grau de pertinência da temperatura alta: {p_alta:.2f}")
    print("")

    if resultado <= 2:
        c = "irrigação quase nada"
    elif resultado <= 5:
        c = "irrigação moderada"
    else:
        c = "irrigação intensa"
    print(f"Grau de Irrigação: {resultado:.2f} → Classificação: {c}")
