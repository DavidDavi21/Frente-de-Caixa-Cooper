from Frente_Cx_Classes import *

lista_operadores = Operador.select()

semana_caixa_par = 0
#Se 0 manhã serão os rápidos ÍMPARES e a tarde PARES
dia_semana = 0
caixas_tarde = [10,12,14,16,18,[3,5,7],[4,6,8],[11,13,15,17]]

for a in lista_operadores:
    print(a)