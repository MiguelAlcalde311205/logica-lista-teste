# Script oficial do teste da lógica binária
# Miguel Alcalde 2022

# Declaração de personagens

init python:
    cir = [0, False]
    est = [0, False]
    qua = [0, False]
    tri = [0, False]
    sixnine = False;

define a = Character("[povname]")
define c = Character("Círculo")
define e = Character("Estrela")
define q = Character("Quadrado")
define t = Character("Triângulo")
define z = Character("???")

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

    e "Seja bem-vindo a High School [povname]! Eu sou a Estrela, fique à vontade!"
    a "oi... é... espera um pouco"
    a "Como que você sabe o meu nome?"
    e "É que eu sou a líder da turma"
    e "E como líder da turma, um dos meus trabalhos é recepcionar os alunos novos!"
    a "Ahhh, tá explicado então"
    a "Só me tira uma dúvida"
    e "Claro, qual seria?"
    a "Essa é a sala 39?"
    e "É sim! A melhor de toda a escola"
    e "Você não foi na sala 69 não foi?"
    a "É......"

    menu:
        "Falar a verdade":
            a "Olha... infelizmente eu entrei sem querer"

            stop music fadeout 1.0

            e "âh? Você não consegue ler por acaso?"
            e "Estava claramente escrito sala 69 na porta da sala!"
            e "Você recebeu o papelzinho?"
            "Ela do nada começa ficar muito grosseira"
            "Falar pra você que eu gosto do tipo dela"
            "Mas agora não é hora de ficar exitado, é hora de resolver esse problema"
            a "Sim"
            e "E VOCÊ LEU ELE POR ACASO?"
            "Ela começa a berrar comigo"
            a "É... eu achei que não era nada muito importante... sabe?"
            "Nisso outras pessoas chegam para tentar acalmar a Estrela"
            
            show cir at right:
                yalign 0.5
            with moveinright

            z "Estrela, o que aconteceu? Por que você começou a gritar do nada?"
            e "É que esse CABAÇO não leu a FOLHA QUE ENTREGARAM PRA ELE NA ENTRADA!"
            a "Ei, não precisa xingar também né?"
            e "CALA A BOCA!"
            z "É melhor não falar nada, sério, não tá ajudando"
            a "Tá bom, tá bom, desculpa"
            
            show cir with moveinright:
                    xalign 0.7

            z "Isso acontece, calma, nem todo mundo é tão organizada quanto você"
            "Ela parece estar se acalmando"
            e "Eu sei, eu sei, é só que ele poderia ter visto o..."
            a "E ela começa a sussurar pra outra"
            a "Meu deus o que que eu perdi naquela sala?"
            a "Fiquei curioso agora, talvez um dia eu volte lá"
            $ sixnine = True
       
            hide cir with dissolve

            e "Enfim"

            play music "audio/feliz.mp3"
            jump nice

        "Mentir":
            a "Claro que não"
            "A Estrela parece aliviada"
            a "Tinha avisando no papelzinho"
            e "Ahhhh, ainda bem que você não foi lá"
            e "Estamos planejando algumas coisas pra sala 69"
            e "Mas por agora, sua entrada está proibida"
            a "Que interessante"
            e "Enfim"

            jump nice

    label nice:
        e "Venha comigo! Ainda há muitas pessoas que você tem que conhecer!"
        "Bom, eu não tenho nenhum amigo aqui nessa escola"
        "E eu não tô fazendo nada da minha vida também"
        "Vai que todas elas sejam meninas"
        "Aí eu vi vantagem"
        a "Claro! Vamos lá!"
        "Nisso ela me guia mais pro fundo da sala, onde tem mais 3 meninas"

        show est with moveinleft:
            xalign 0.33

        e "Então [povname], essa aqui é a Círculo"

        show cir with dissolve:
            xalign 0.0
            yalign 0.5

        a "Prazer em te conhecer, Círculo"
        c "O prazer também é meu, [povname]"
        e "Essa aqui é a Quadrado"
        
        show qua with dissolve:
            xalign 0.66
            yalign 0.5
        
        a "Olá"
        q "Oi"
        e "E essa aqui é a Triângulo"

        show tri with dissolve:
            xalign 1.0
            yalign 0.5

        a "Bom dia, Triângulo"
        t "Muito bom dia"

        if sixnine:
            c "Olha [povname] revele o que aconteceu hoje de manhã com a sala 69"
            a "Não não, podem ficar tranquilas, eu entendo a preocupação"
            e "Me desculpe também [povname], eu fui meio grossa com você"
            "Ahhhh se ela for assim comigo na cama eu nunca que reclamaria"
            a "Acontece, deve ser algo muito sério pra estar no papelzinho que eles entregam na entrada"
            a "E foi culpa minha não ter lido ele a tempo também"

        q "Mas.. e aí, o que você faz da vida [povname]?"

    return
