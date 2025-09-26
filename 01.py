import numpy as np
import skfuzzy as fuzz
from utils import fuzz_p

""" 
=> Exercício 1
TODO: quente AND lotado == baixo 
TODO: amena AND medio == alto 
TODO: frio AND poucas == médio
"""

x_pessoas = np.arange(0,21,1) # sala com no máximo 35 pessoas 
x_temp = np.arange(0,41,1) # Cidadezinha quente, doido
x_conforto = np.arange(0,11,1) # conforto de 0 -> 10

# ? Função tringular de pessoas
poucas = fuzz.trimf(x_pessoas, [0,0,5])
medio = fuzz.trimf(x_pessoas,[3,7,12])
lotado = fuzz.trimf(x_pessoas,[8,15,20])

# ? Def trinagular de temperatura
frio = fuzz.trimf(x_temp,[0,0,15])
morno = fuzz.trimf(x_temp,[10,20,30])
quente = fuzz.trimf(x_temp,[25,40,40])

# ? Def triangular de conforto
desgostoso = fuzz.trimf(x_conforto,[0,0,4])
deboa = fuzz.trimf(x_conforto,[3,7,8])
resenha = fuzz.trimf(x_conforto,[6,10,10])

# * inputs
temp = 25
pessoas = 10 

# TODO: criação das pertinencias

# ? temperatura
p_frio = fuzz_p(x_temp,frio,temp)
p_morno = fuzz_p(x_temp,morno,temp)
p_quente = fuzz_p(x_temp,quente,temp)

# ? pessoas
p_db = fuzz_p(x_pessoas,poucas,pessoas)
p_diapadrao = fuzz_p(x_pessoas,medio,pessoas)
p_prova = fuzz_p(x_pessoas,lotado,pessoas)

# TODO: Aplicação das regras

regra1 = np.fmin(p_quente,p_prova)    # quente AND lotado == baixo 
regra2 = np.fmin(p_morno,p_diapadrao) # amena AND medio == alto 
regra3 = np.fmin(p_frio,p_prova)      # frio AND poucas == médio

# ! ativacao das regras
r1_ativado = np.fmin(regra1,desgostoso)
r2_ativado = np.fmin(regra2,resenha)
r3_ativado = np.fmin(regra3,deboa)
#? não entendi o por que dessas ativações, não parece intuitivo

# TODO: defusando a spike
conforto = np.fmax(r1_ativado, np.fmax(r2_ativado, r3_ativado))
resultado = fuzz.defuzz(x_conforto,conforto,'centroid') # ? também não entendi esse centroid


print("")
print(f"Grau de pertinência da temperatura fria: {p_frio:.2f}")
print(f"Grau de pertinência da temperatura amena: {p_morno:.2f}")
print(f"Grau de pertinência da temperatura quente: {p_quente:.2f}")
print("")
print(f"Grau de pertinência de pessoas poucas: {p_db:.2f}")
print(f"Grau de pertinência de pessoas média: {p_diapadrao:.2f}")
print(f"Grau de pertinência de pessoas lotado: {p_prova:.2f}")
print("")

if resultado <= 2 :
    c = "aqui já foi pra deus"
elif resultado <= 4:
    c = "paia"
elif resultado <= 6:
    c = "massinha"
elif resultado <= 8:
    c = "resenha máxima"
else:
    c = "SONO BOM DOIDO"
print(f"Grau de Conforto: {resultado:.2f} → Classificação: {c}")
