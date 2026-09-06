senha = input(str("Sua Senha: "))   # aqui varia de acordo com o que vai digitar ( str, float, booleans)
pontos = 0
if len(senha) >=8:
    pontos += 1
if  any(c.isupper()for c in senha):
    pontos += 1
if any(c.isdigit()for c in senha):
    pontos += 1
if any(c in "!@#$"for c in senha):
    pontos += 1

if pontos == 4:
    print("Senha forte!")
elif pontos >=2:
    print("Senha média!")
else:
    print("Senha fraca!")
