# Teste da Lógica de Listas

Este repositório é um jogo feito no [Renpy](https://www.renpy.org/) que visa testar a lógica que será implementada no jogo [Anglo Dating Simulator](https://github.com/Bruno-Mai/Anglo-Dating-Sim---BETA) de [Bruno-Mai](https://github.com/Bruno-Mai)

## O que é "Anglo Dating Simulator"?

Anglo Dating Simulator é um jogo no Renpy que eu estou fazendo junto com o [Bruno-Mai](https://github.com/Bruno-Mai) apenas como hobby, infelizmente, o jogo ainda não está disponível para o público

## Como a lógica funciona?
Essa lógica tem 2 gols principais
- Lembrar sua escolha de personagem
- Fazer sua conexão evoluir de modo natural
- Possibilitar discussões no meio do jogo

Para isso, cada personagem tem sua lista (por isso o nome teste da lógica de listas) com 2 atributos, o nível de amizade, e se ele já se aplica na lógica binária, que será explicada depois.

#### Nível de Amizade
Esse nível vai de 1 a 5, e ele diz o quão amigo você é de um dos personagens, quando esse número chega em 2, o personagem é colocado na lógica binária

#### Lógica Binária
Quando você atinge o nível de amizade 2 com algum personagem, ele é adicionado a variável da lógica binária, singnificando que cada personagem equivale a 1 bit.
Para explicar isso melhor, aqui vai um exemplo.  
Vamos supor que você se interessou por 2 personagens no jogo, vamos chamá-las de A e B.
Você chegou no nível 2 com a A, ou seja, ela foi adicionada na lógica binária

0000 --> 0001(bin) = 1(dec)

Mas, ao longo do jogo você também ficou interessada pela B, chegando ao nível 2 com ela também.

0001 --> 0011(bin) = 3(dec)

O Jogo então percebe que a lógica binária é igual a 3, ou seja, você está interessado por 2 personagens, e elas irão brigar, quem vence a briga é quem tem o maior nível de amizade. Se os níveis de amizade são iguais, nesse jogo de teste, você terá que escolher.

Após uma briga, as 2 personagens perdem 1 nível de amizade com você  
Para um exemplo ainda mais claro, vamos dizer que agora adicionamos a personagem C, ocupando o terceiro bit na nossa lógica binária.
Se você se interessar por A e C, a lógica fica assim:

0101(bin) = 5(dec)

Se você se interessar por A e B, a lógica fica assim:

0011(bin) = 3(dec)

Se você se interessar por B e C, a lógica fica assim:

0110(bin) = 6(dec)

## Como faço para testar o jogo?
Para testar o jogo, primeiro baixe uma cópia do [Renpy 8.0.3](https://www.renpy.org/latest.html) para o seu sistema operacional, após isso, crie um novo projeto com o nome "Logica Lista Teste", o renpy irá gerar um projeto novo para você, agora, você tem algumas opções  
#### Usando o git
Vá na pasta `game/` do projeto que você criou, e execute o comando
`git clone https://github.com/MiguelAlcalde311205/logica-lista-teste.git` para URL, ou
`git clone git@github.com:MiguelAlcalde311205/logica-lista-teste.git` para SSH  
#### Baixando o ZIP
Pelo GitHub, você pode baixar um zip desses arquivos, se você preferir, baixe o zip e coloque os arquivos dele na pasra `game/` do seu projeto do Renpy

## Agradecimentos
Obrigado [Bruno-Mai](https://github.com/Bruno-Mai) pela oportunidade de jogo
Obrigado [Yashinkar](https://github.com/Yashinkar) pela ideia da lógica
