CONSTANTE_BONUS = 1000

nome = input("Digite o seu nome: ")
salario = float(input("Digite o seu salário atual: "))
bonus = float(input("Digite o seu bônus: "))

valor_bonus = CONSTANTE_BONUS + (salario * bonus)

print(f"Parabéns {nome}, seu bônus será de R$ {valor_bonus}")