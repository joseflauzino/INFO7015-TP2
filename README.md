# Congestion Control

## Pré-requisitos
- Ubuntu 14.04 ou 15.10*

- Git.

- Emulador de rede celular.

- Biblioteca python matplotlib

> \* Outras versões ou distribuições podem ser usadas, mas não foram testadas.

### Instalando Git
Execute `sudo apt-get update && apt-get install git`

### Instalando Emulador de Rede Celular

Execute `sudo apt-get install build-essential git debhelper autotools-dev dh-autoreconf iptables protobuf-compiler libprotobuf-dev pkg-config libssl-dev dnsmasq-base ssl-cert libxcb-present-dev libcairo2-dev libpango1.0-dev iproute2 apache2-dev apache2-bin iptables dnsmasq-base gnuplot iproute2 apache2-api-20120211 libwww-perl`

Faça o clone com o comando `git clone https://github.com/ravinet/mahimahi`

Entre no diretório mahimahi `cd mahimahi` e compile tudo com `./autogen.sh && ./configure && make`

Por fim instale `sudo make install`

### Instalando a biblioteca matplotlib
Instale o matplotlib `sudo apt-get install python-matplotlib`

## Obtendo o código

Escolha um diretório, entre em tal diretório e execute `git clone https://github.com/joseflauzino/INFO7015-TP2.git`

## Executando Exercício A

Entre no diretório exerciseA `cd datagrump/exerciseA/`

Execute `./run.sh`

A saída resultante é:
- arquivo "output.txt" contendo o throughput e delay (cada linha representa a saída da execução com um tamanho da janela de congestionamento).
- figura "plot.png" (apresenta em forma de gráfico o resultado de todas as execuções)
- figura "plot_zoom.png" (apresenta em forma de gráfico o resultado dos tamanhos de janela que obtiveram potências mais significativas)

> Em resumo o script run.sh desse diretório faz o seguinte:
> - exclui o arquivo 'controller.cc'
> - faz uma cópia do 'controller_exeA.cc' com o nome 'controller.cc'
> - compila tudo
> - executa o experimento

## Executando Exercício B
Entre no diretório exerciseB `cd datagrump/exerciseB/`

Execute `./run.sh`

> Em resumo o script run.sh desse diretório faz o seguinte:
> - exclui o arquivo 'controller.cc'
> - faz uma cópia do 'controller_exeB.cc' com o nome 'controller.cc'
> - compila tudo
> - executa o experimento

## Executando Exercício C
Entre no diretório exerciseC `cd datagrump/exerciseC/`

Execute `./run.sh`

> Em resumo o script run.sh desse diretório faz o seguinte:
> - exclui os arquivos 'controller.cc' e 'controller.hh'
> - faz uma cópia do 'controller_exeC.cc' 'controller_exeC.hh', respectivamente, com os nomes 'controller.cc' e 'controller.hh'
> - compila tudo
> - executa o experimento

