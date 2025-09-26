import numpy as np
import skfuzzy as fuzz
from utils import fuzz_p

""" 
=> Exercício 2: Qualidade de Serviço
TODO: longa + alta → aceitável
TODO: curta + baixa → ruim
"""

x_espera = np.arange(0,61,1)       # espera de 0 a 60 minutos
x_satisfacao = np.arange(0,11,1)   # satisfação de 0 a 10
x_qualidade = np.arange(0,11,1)    # qualidade de 0 a 10

# ? Função triangular de espera
curta = fuzz.trimf(x_espera,[0,0,20])
media = fuzz.trimf(x_espera,[15,20,30])
longa = fuzz.trimf(x_espera,[24,50,60])

# ? Função triangular de satisfação
baixa = fuzz.trimf(x_satisfacao,[0,0,4])
media_s = fuzz.trimf(x_satisfacao,[3,7,8])
alta = fuzz.trimf(x_satisfacao,[6,10,10])

# ? Função triangular de qualidade
ruim = fuzz.trimf(x_qualidade,[0,0,4])
aceitavel = fuzz.trimf(x_qualidade,[3,5,8])
excelente = fuzz.trimf(x_qualidade,[6,10,10])

# * inputs
espera = 25
satisfacao = 8

# TODO: criação das pertinencias

# ? espera
p_curta = fuzz_p(x_espera,curta,espera)
p_media_esp = fuzz_p(x_espera,media,espera)
p_longa = fuzz_p(x_espera,longa,espera)

# ? satisfação
p_baixa = fuzz_p(x_satisfacao,baixa,satisfacao)
p_media_sat = fuzz_p(x_satisfacao,media_s,satisfacao)
p_alta = fuzz_p(x_satisfacao,alta,satisfacao)




# TODO: Aplicação das regras

regra1 = np.fmin(p_longa, p_alta)  # longa + alta → aceitável
regra2 = np.fmin(p_curta, p_baixa) # curta + baixa → ruim

# ! ativacao das regras
r1_ativado = np.fmin(regra1, aceitavel)
r2_ativado = np.fmin(regra2, ruim)

# TODO: agregação das regras

qualidade = np.fmax(r1_ativado, r2_ativado) 
print(r1_ativado, r2_ativado)
# TODO: deffuzy
resultado = fuzz.defuzz(x_qualidade, qualidade, 'centroid')

print("")
print(f"Grau de pertinência espera curta: {p_curta:.2f}")
print(f"Grau de pertinência espera média: {p_media_esp:.2f}")
print(f"Grau de pertinência espera longa: {p_longa:.2f}")
print("")
print(f"Grau de pertinência satisfação baixa: {p_baixa:.2f}")
print(f"Grau de pertinência satisfação média: {p_media_sat:.2f}")
print(f"Grau de pertinência satisfação alta: {p_alta:.2f}")
print("")

if resultado <= 4 :
    c = "Ruim"
elif resultado <= 7:
    c = "Aceitável"
else:
    c = "Excelente"
print(f"Resultado defuzzificado da Qualidade: {resultado:.2f} → Classificação: {c}")
