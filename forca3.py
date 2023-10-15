# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:30:14 2023

@author: Matheus
"""

import random
import pandas as pd
from unidecode import unidecode

def importar_csv(caminho_arquivo):
    try:
        # Lê o arquivo CSV e cria um DataFrame sem índice
        df = pd.read_csv('palavras.csv', index_col=None)
        return df

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {caminho_arquivo}")
    except Exception as e:
        print(f"Erro ao importar o arquivo CSV: {e}")
    
def obter_palavra(): 
    palavras = importar_csv('palavras.csv')
    print(palavras)
    a = random.randint(0, 30)
    palavra = palavras['Palavra'][a].lower()
    print(f'A palavra escolhida foi: {palavra}')
    return palavra

def exibir_palavra_oculta(palavra, letras_tentadas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_tentadas or letra.isspace():
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta

def jogo_da_forca(palavra):
    palavra_a_adivinhar = palavra.lower()
    letras_tentadas = []
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra_oculta(palavra_a_adivinhar, letras_tentadas))

    while tentativas < tentativas_maximas:
        letra = input("\nDigite uma letra: ").lower()

        # Verifica se a letra já foi tentada
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        # Verifica se a letra está na palavra
        if letra in palavra_a_adivinhar:
            print(f"Letra '{letra}' correta!")
        else:
            tentativas += 1
            print(f"Letra '{letra}' incorreta. Tentativas restantes: {tentativas_maximas - tentativas}")

        # Exibe a palavra oculta atualizada
        palavra_oculta = exibir_palavra_oculta(palavra_a_adivinhar, letras_tentadas)
        print(palavra_oculta)

        # Verifica se o jogador adivinhou a palavra
        if palavra_oculta == palavra_a_adivinhar:
            print("Parabéns! Você adivinhou a palavra.")
            break

    else:
        print(f"\nGame Over! A palavra era: {palavra_a_adivinhar}")

# Chama o jogo
palavra = obter_palavra()
jogo_da_forca(palavra)