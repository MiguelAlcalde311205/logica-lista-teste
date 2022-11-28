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
define b = Character("Carlos")

# O jogo começa aqui

label start:
    stop music fadeout 2.0
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
    pause 3.0

    "Que sala é essa que eu estou?"

    hide papel with moveoutbottom

    "Ah, a 69"
    "Pera aí"

    show papel with moveinbottom:
        xalign 0.5
        yalign 0.5
    pause 3.0
    
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
            "Nisso uma menina chega pra tentar acalmar a Estrela"
            
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
            "E ela começa a sussurar pra outra"
            "Meu deus o que que eu perdi naquela sala?"
            "Fiquei curioso agora, talvez um dia eu volte lá"

            $ sixnine = True
            hide cir with moveoutright

            e "Enfim"

            play music "audio/feliz.mp3"
            jump nice

        "Mentir":
            a "Claro que não"
            "A Estrela parece aliviada"
            a "Tinha avisando no papelzinho"
            e "Então podemos prosseguir [povname]"

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
    "Eu estava secretamente com medo dessa pergunta"
    "Não é como se eu não fizesse nada da vida mas..."
    "Eu não faço nada de interessante... ou produtivo..."
    "Na verdade é só vergonha de falar pras pessoas que eu assisto anime o dia inteiro mesmo"
    a "Olha... Eu não faço muita coisa pra ser honesto"
    q "Ahhhh qual é, todo mundo gosta de fazer alguma coisa"
    c "Não é possível que você não goste de fazer nada [povname]"
    a "Eu gosto de uma coisa mas..."
    q "Mas?"
    e "Pode contar [povname], ninguém vai te julgar nem nada"
    "Elas me pressionaram"
    "E agora... Eu tô com vergonha e exitado ao mesmo tempo"
    "Sério, eu sou seduzido muito fácil, deve ser os animes que eu assisto"
    a "Eu... gosto de assistir anime..."
    t "Ah~"
    "Todas parecem meio desapontadas, menos a Triângulo, que mandou um gemido estranhaço e parece até surpresa" 
    "Preciso voltar com a conversa"
    "Mas... É... E aí, o que vocês gostam de fazer?"
    c "Eu gosto muito de ler e dar conselho às pessoas"
    c "Eu adoro ajudar a resolver seus problemas e fazer o seu dia melhor!"
    q "Eu gosto de tocar piano"
    q "Eu toco desde os 5 anos e sempre gostei muito!"
    e "Eu adoro liderar"
    e "Gosto de ser a líder em qualquer grupo ou projeto em que eu estou"
    a "E você Triângulo?"
    t "Ah~..."
    t "Eu gosto de assistir... Anime... Também"
    a "Huh?"
    "Eu certamente não esperava por essa"
    "Uma menina que assiste anime!?"
    "Isso existe!?"
    t "Eu disse algo errado?"
    a "Não não... É só..."

    play sound "audio/sinal.mp3"
    pause 3.0

    e "Ahhhh justo agora que a conversa estava tão boa!"
    c "Bom, a gente se vê amanhã então"
    c "Até mais [povname]"
        
    hide cir with dissolve
    show est with moveinleft:
        xalign 0.0
    show qua with moveinleft:
        xalign 0.5
    show tri with moveinleft:
        xalign 1.0

    e "Até amanhã [povname], espero que você tenha gostado na nossa escola"
    a "Tchau tchau"
        
    hide est with dissolve
    show qua with moveinleft:
       xalign 0.0

    q "Bom, essa é minha deixa né"
    a "Acho que sim"
    q "Até amanhã [povname]"
    a "Até"

    hide qua with dissolve
    show tri with moveinleft:
        xalign 0.5

    t "Ah~"
    t "Até... amanhã [povname]..."
    a "Até lá"

    hide tri with dissolve
    
    "Bom, agora só falta eu ir embora"
    "Sair antes que seja tarde demais"

    stop music fadeout 1.0
    scene rua with dissolve
    play music "audio/calmo.mp3"

    "Achei essa escola bem animada"
    "E acho que já fiz umas amizades interessantes"
    "hehehehehehehehehe"

    if sixnine:
        "Mas tem uma coisa no fundo da minha cabeça"
        "O que diabos que tem na sala 69?"
        "Porque a Estrela ficou tão irritada que eu entrei lá?"
        "E porque só ela e a Círculo aparentemente sabem o que aconteceu?"
        "Um dia desses eu volto pra lá"

    "Cada uma daquelas meninas tem qualidades bem interessantes"

    show est at center with dissolve:
        yalign 0.5
        
    "A Estrela sabe liderar e se virar por ela mesma"

    hide est with dissolve
    show cir at center with dissolve:
        yalign 0.5

    "A Círculo parece a pessoa perfeita pra ter uma conversa bem profunda e emocional"

    hide cir with dissolve
    show qua at center with dissolve:
        yalign 0.5

    "A Quadrado parece ser uma ótima companheira pra momentos íntimos também"

    hide qua with dissolve

    "Mas... a Triângulo"

    show tri at center with dissolve:
        yalign 0.5

    "Ela assiste anime também..."
    "Talvez eu possa assistir um com ela um dia desses"

    hide tri with dissolve
    scene casa with dissolve

    "Nossa, fiquei viajando por toda a caminhada"
    "Deixa eu entrar em casa então"

    scene preto with wipeleft
    scene sala with wipeleft

    "Precisa dar uma organizadinha nessa casa"
    "Aparentemente o Carlos não chegou ainda"
    "Enfim, deixa eu ir pro meu quarto"

    scene preto with wipeleft
    scene quarto with wipeleft

    "Vou dar uma dormidinha aqui"
    "Provável que quando eu acordar o Carlos já vai estar aqui"

    stop music fadeout 1.0
    scene preto with dissolve
    pause 3.0
    play music "audio/calmo.mp3"
    scene quarto tarde with dissolve

    "Yawnnnnnnnnn"
    "Bela de uma soneca"
    "Enfim, preciso ver se o Carlos já chegou"

    scene preto with wipeleft
    scene sala tarde with wipeleft
    show carlos with dissolve:
        xalign 0.5
        yalign 0.5

    a "E aí Carlos"
    b "Boa tarde [povname]"
    b "Como foi a nova escola?"
    a "Ah, é legalzinho lá"
    a "Conheci umas amigas também"
    b "Hmmmm, essa sua carinha aí me diz que alguma delas te chamou a atenção em"
    a "Que? Claro que não"
    b "Não se finja de tonto, você gostou de alguém dali hehehehehehe"
    "Meu deus deixa eu trocar de assunto antes que minha reputação vá de base"

    if sixnine:
        a "Mas, mudando de assunto"
        "Ele dá uma risadinha"
        b "Hm"
        a "Tem uma sala muito estranha naquele lugar"
        b "É? Como assim estranha?"
        a "É proibído entrar lá por algum motivo estranho"
        a "Mas o espertão aqui entrou sem querer"
        b "Vish! Você sabe que isso poderia ter dado uma treta né?"
        a "Sei! Por isso saí de lá vazado"
        a "A líder da turma me perguntou se eu fui lá e..."
        b "Hmmmmmmm a líder da turmaaaaaaa saqueeeeei"
        a "Deixa eu terminar de contar Carlos!"
        b "Tá bom tá bom"
        a "Enfim, ela começou a gritar comigo que não era pra eu ter ido lá"
        a "E aí uma amiga dela chegou e elas começaram a falar entre si"
        a "Aparentemente aconteceu algo cabuloso lá naquela sala"
        b "Que isso, deu até medo"
        a "Eu decidi que eu vou voltar pra dar uma averiguada lá um dia desses"
        b "Tem certeza disso? Esse seu plano pode dar muito errado"
        a "Eu sei, mas a curiosidade é maior"
        b "Se você diz..."
    else:
        a "Então, mudando de assunto"
        "Ele dá uma risadinha"
        b "Hm"

    a "Mas e aí, como tá o seu freelance?"
    b "Sinceramente, tá indo melhor do que eu esperava"
    a "Que bom! Já recebeu algum cliente?"
    b "Sim, falei com uma moça que queria que eu fizesse umas artes pro aniversário do filho dela"
    a "Hmmm, boa sorte com isso"
    b "Valeu"

    return
