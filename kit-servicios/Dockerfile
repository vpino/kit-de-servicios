FROM debian:jessie

RUN echo "deb http://200.11.148.219/debian jessie main contrib non-free" > /etc/apt/sources.list

RUN echo "deb http://200.11.148.219/seguridad jessie/updates main contrib non-free" >> /etc/apt/sources.list

# Dependencias con instalacion de virtualenv, falta refinar
RUN apt update && apt -y install nano python openssh-server sudo htop
