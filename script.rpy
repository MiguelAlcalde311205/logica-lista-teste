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

    scene sala aula with dissolve
    play music "audio/calmo.mp3"

    "Hoje é meu primeiro dia de aula nessa nova escola"
    "Mas acho que essa é a sala errada"
    "Não tem ninguém nessa sala"
    "Nenhum aluno, professor, nada!"
    "Calma aí, deixe-me ver o papelzinho que eles me entregaram"

    show papel with moveinbottom:
        xalign 0.5
        yalign 0.5

    "Que sala é essa que eu estou?"

    hide papel with moveoutbottom

    "Ah, a 69"
    "Pera aí"

    show papel with moveinbottom:
        xalign 0.5
        yalign 0.5
    
    "Putz"
    "Entrei na sala proibida"

    hide papel with moveoutbottom

    "Preciso sair daqui vazado!"
    
    scene preto with dissolve

    "Imagina se eu tivesse sido pego numa sala que não pode!"
    "Nada bom pro meu primeiro dia de aula"
    "Deixa eu achar essa sala 39"

    stop music fadeout 1.0
    scene sala aula 2 with dissolve

    "Acho que essa é a sala certa"

    play music "audio/feliz.mp3"

    show est with dissolve:
        xalign 0.5
        yalign 0.5

    e "Seja bem-vindo a High School [povname]!"
    a "oi... é... espera um pouco"
    a "Como que você sabe o meu nome?"

    return
