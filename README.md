# Congestion Control

## Pré-requisitos
1 - Ubuntu 14.04 ou 15.10*

2 - Git.

3 - Emulador de rede celular.

> * Outras versões ou distribuições podem ser usadas, mas não foram testadas.

### Instalando Git
Execute `sudo apt-get update && apt-get install git`

### Instalando Emulador de Rede Celular

Execute `sudo apt-get install build-essential git debhelper autotools-dev dh-autoreconf iptables protobuf-compiler libprotobuf-dev pkg-config libssl-dev dnsmasq-base ssl-cert libxcb-present-dev libcairo2-dev libpango1.0-dev iproute2 apache2-dev apache2-bin iptables dnsmasq-base gnuplot iproute2 apache2-api-20120211 libwww-perl`

Faça o clone com o comando `git clone https://github.com/ravinet/mahimahi`

Entre no diretório mahimahi `cd mahimahi` e compile tudo com `./autogen.sh && ./configure && make`

Por fim instale `sudo make install`

## Obtendo o código

Escolha um diretório, entre em tal diretório e execute `git clone https://github.com/joseflauzino/Congestion_Control.git`


