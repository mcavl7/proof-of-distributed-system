### Prova de Sistema Distribuido

<hr>

#### Projeto atualizado para atender aos requisistos da 2a Unidade.

##### 🔄 Atualiazações:

- [x] Projeto refatorado utilizando Docker
- [x] Cada processo da aplicação foi adicionado em um Container único

##### ❓ Vantagens:

Com a separação dos processos cada um em um container único, fica mais fácil realizar manunteção/refatoração na atividade, pois nos permite que cada processo seja manipulado exclusivamente, sem ter efeitos colaterais nas outras partes.

Através da seperação dos Containers, matemos somente o necessário que cada parte precisa pra executar, permitindo que o ambiente fique mais limpo.

##### ⚙️ Dependências e Como usar:

A única dependência necessária para se executar esse projeto é ter o docker instalado. Pois todo o processo de resolver dependências é feito automaticamentet pela imagem de cada processo (Encontrado nas pastas)

Para instalar o docker (No Linux em distribuições debian based):

> sudo apt-get update

> sudo apt-get remove docker-engine docker.io

> sudo apt-get install docker.io

Para iniciar o Docker na sua máquina:

> sudo systemctl start docker

Clone esse repositório em uma pasta a sua escolha através do git clone

Feito a clonagem, entre em cada uma das pastas (nomeadas de: calc_serve, processoA, processoB e Serv)

ao entrar em cada pasta execute dentro de cada pasta o seguinte comando para construir as imagens

> docker build -t nome_processo .

###### OBS: Não esquecer do ponto ( . ) pois ele construirá a imagem com os arquivos contido no diretório que você está (logo, é necessário estar dentro da pasta de cada projeto. NÃO ESQUECER!)

Feito o build de todos os processos, você pode executar. Para que o programa execute corretamente na sua máquina você deve seguir uma ordem de iniciação, sendo elas:

1. docker run -it calc_serve
2. docker run -it serv 
3. docker run -it processoB
4. docker run -it processoA

##### 🥷🏻 E pronto :)

