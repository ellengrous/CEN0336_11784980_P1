#!/bin/bash

# Comando para mostrar o diretório atual
echo "Diretório atual: $(pwd)"

#Comando que gere uma lista com detalhes do conteúdo da sua pasta HOME e redirecione essa lista para o arquivo: lista_HOME.txt
ls -l ~ > lista_HOME.txt
echo "Lista da pasta HOME gerada e salva em lista_HOME.txt"

#Imprimir a data atual
echo "Data atual: $(date)"
