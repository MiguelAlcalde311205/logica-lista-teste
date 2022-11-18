# Script oficial do teste da lógica binária
# Miguel Alcalde 2022

# Declaração de personagens

define a = Character("[povname]")
define c = Character("Círculo")
define e = Character("Estrela")
define q = Character("Quadrado")
define t = Character("Triângulo")


# O jogo começa aqui

label start:
    "Antes do jogo começar"
    $ povname = renpy.input("Qual é o seu nome?: ")
    $ povname = povname.strip()

    "Ótimo, vamos começar o jogo então [povname]!"

    show est with dissolve:
        xalign 0.5
        yalign 0.5
    e "Isso é um teste lol"

    return
