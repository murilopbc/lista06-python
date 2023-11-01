hora = int(input("Digite a hora: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

hora_valida = 0 <= hora < 24
minutos_validos = 0 <= minutos < 60
segundos_validos = 0 <= segundos < 60

if hora_valida and minutos_validos and segundos_validos:
    print("A hora é válida.")
else:
    print("A hora é inválida.")
