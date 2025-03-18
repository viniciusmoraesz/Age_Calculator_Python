from datetime import date, datetime

#Obtendo o dia atual
dia_atual = date.today()

#Formatando o dia_atual para dd/mm/aaaa
dia_atual_formatado = dia_atual.strftime("%d/%m/%Y")


#Usuario digita a data de nascimento
data_nascimento_usuario = str(input("Digite a sua data de aniversário no modelo dd/mm/aaaa: "))

#Formatando a String obtida pelo input
data_nascimento_usuario_formatado = datetime.strptime(data_nascimento_usuario, "%d/%m/%Y")

print(f"Data atual: {dia_atual_formatado}")

print(f"Data do seu Nascimento: {data_nascimento_usuario_formatado.strftime("%d/%m/%Y")}")

#Convertendo dia_atual_formatado para datetime
dia_atual_convertido = datetime.strptime(dia_atual_formatado, "%d/%m/%Y")

#Contando quantos anos/meses/dias você tem
anos = dia_atual_convertido.year - data_nascimento_usuario_formatado.year
meses = dia_atual_convertido.month - data_nascimento_usuario_formatado.month
dias = dia_atual_convertido.day - data_nascimento_usuario_formatado.day

# Ajustando o número de anos, meses e dias se necessário
if meses < 0:
    anos -= 1
    meses += 12
if dias < 0:
    meses -= 1
    dias += 30  # Aproximadamente, já que o número de dias no mês varia

#Resultado Final
print(f"Você tem {anos} anos, {meses} meses e {dias} dias de vida. Parabéns!")