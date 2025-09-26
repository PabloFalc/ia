import numpy as np
import skfuzzy as fuzz
from utils import fuzz_p

""" 
=> Exercício 5 - Direção Autônoma
TODO: perto AND acentuada == velocidade baixa
TODO: longe AND reta == velocidade alta
"""

x_distancia = np.arange(0, 21, 1)   # distância 0 → 20m
x_curva = np.arange(0, 91, 1)       # ângulo da curva 0° → 90°
x_velocidade = np.arange(0, 101, 1) # velocidade 0 → 100 km/h

# ? Funções de pertinência da distância
perto = fuzz.trimf(x_distancia, [0, 0, 10])
media = fuzz.trimf(x_distancia, [5, 10, 15])
longe = fuzz.trimf(x_distancia, [8, 20, 20])

# ? Funções de pertinência da curvatura
reta = fuzz.trapmf(x_curva, [0,5,10,15])
leve = fuzz.trapmf(x_curva, [10,20,30,45])
acentuada = fuzz.trapmf(x_curva, [35,45,90,90])

# ? Funções de pertinência da velocidade
baixa = fuzz.trimf(x_velocidade, [0, 0, 40])
media_v = fuzz.trimf(x_velocidade, [30, 50, 70])
alta = fuzz.trimf(x_velocidade, [60, 100, 100])

# * inputs
distancia = 8   # metros
curva = 40      # graus

# TODO: criação das pertinencias

# ? distância
p_perto = fuzz_p(x_distancia, perto, distancia)
p_media = fuzz_p(x_distancia, media, distancia)
p_longe = fuzz_p(x_distancia, longe, distancia)

# ? curva
p_reta = fuzz_p(x_curva, reta, curva)
p_leve = fuzz_p(x_curva, leve, curva)
p_acentuada = fuzz_p(x_curva, acentuada, curva)

# TODO: Aplicação das regras

regra1 = np.fmin(p_perto, p_acentuada)  # perto AND acentuada == velocidade baixa
regra2 = np.fmin(p_longe, p_reta)       # longe AND reta == velocidade alta

# ! ativacao das regras
r1_ativado = np.fmin(regra1, baixa)
r2_ativado = np.fmin(regra2, alta)

# TODO: agregação das regras
velocidade = np.fmax(r1_ativado, r2_ativado)

# TODO: defuzzificação

resultado = fuzz.defuzz(x_velocidade, velocidade, 'centroid')

print("")
print(f"Grau de pertinência da distância perto: {p_perto:.2f}")
print(f"Grau de pertinência da distância média: {p_media:.2f}")
print(f"Grau de pertinência da distância longe: {p_longe:.2f}")
print("")
print(f"Grau de pertinência da curva reta: {p_reta:.2f}")
print(f"Grau de pertinência da curva leve: {p_leve:.2f}")
print(f"Grau de pertinência da curva acentuada: {p_acentuada:.2f}")
print("")

if resultado <= 33:
    c = "velocidade baixa"
elif resultado <= 66:
    c = "velocidade média"
else:
    c = "velocidade alta"
print(f"Velocidade sugerida: {resultado:.2f} → {c}")
