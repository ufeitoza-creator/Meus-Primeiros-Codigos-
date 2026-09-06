import turtle

#Configuração da tela
tela = turtle.Screen()
tela.title("Animação simples com Turtle")
tela.bgcolor("black")

#Criação do objeto (bola)
bola = turtle.Turtle()
bola.shape("circle")
bola.color("cyan")
bola.penup()
bola.speed(0)

x = -250  # Posição inicial no eixo x

#loop da animação
while True:
    bola.goto(x, 0)
    tela.update() # Atualiza a tela manualmente
    
    x += 50# Velocidade do movimento
    if x > 250:
        x = -250 # reinicia a posição quando chegar ao fim
