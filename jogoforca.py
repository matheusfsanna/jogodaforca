# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 15:30:14 2023
Interface gráfica criada pelo CHATGPT
@author: Matheus
"""

import random
import pandas as pd
from unidecode import unidecode
import tkinter as tk
from tkinter import messagebox

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        self.palavras = self.importar_csv('palavras.csv')
        self.palavra_a_adivinhar = ""
        self.letras_tentadas = []
        self.tentativas_maximas = 6
        self.tentativas = 0

        self.iniciar_jogo()

    def importar_csv(self, caminho_arquivo):
        try:
            # Lê o arquivo CSV e cria um DataFrame sem índice
            df = pd.read_csv(caminho_arquivo, delimiter=',', index_col=None)
            return df
        except FileNotFoundError:
            messagebox.showerror("Erro", f"Arquivo não encontrado: {caminho_arquivo}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao importar o arquivo CSV: {e}")

    def obter_palavra(self):
        a = random.randint(0, len(self.palavras) - 1)
        self.palavra_a_adivinhar = unidecode(self.palavras['Palavra'][a].lower())

    def exibir_palavra_oculta(self):
        palavra_oculta = ""
        for letra in self.palavra_a_adivinhar:
            if letra in self.letras_tentadas or letra.isspace():
                palavra_oculta += letra
            else:
                palavra_oculta += "_"
        return palavra_oculta

    def validar(self, letra):
        if len(letra) == 1 and letra.isalpha():
            letra_validada = unidecode(letra.lower())
            return letra_validada
        else:
            messagebox.showwarning("Aviso", "Por favor, digite exatamente uma letra.")

    def adivinhar_letra(self):
        letra = self.entry_letra.get()
        letra_validada = self.validar(letra)

        if letra_validada:
            # Verifica se a letra já foi tentada
            if letra_validada in self.letras_tentadas:
                messagebox.showwarning("Aviso", "Você já tentou essa letra. Tente outra.")
            else:
                self.letras_tentadas.append(letra_validada)

                # Verifica se a letra está na palavra
                if letra_validada in self.palavra_a_adivinhar:
                    messagebox.showinfo("Informação", f"Letra '{letra_validada}' correta!")
                else:
                    self.tentativas += 1
                    messagebox.showinfo("Informação", f"Letra '{letra_validada}' incorreta. Tentativas restantes: "
                                                    f"{self.tentativas_maximas - self.tentativas}")

                # Exibe a palavra oculta atualizada
                palavra_oculta = self.exibir_palavra_oculta()
                self.label_palavra.config(text=palavra_oculta)

                # Verifica se o jogador adivinhou a palavra
                if palavra_oculta == self.palavra_a_adivinhar:
                    messagebox.showinfo("Parabéns!", "Você adivinhou a palavra.")
                    self.palavras['Palavra'] = self.palavras['Palavra'].str.replace(self.palavra_a_adivinhar, '')
                    self.palavras = self.palavras.dropna()
                    self.palavras.to_csv('palavras.csv', index=False)
                    self.iniciar_jogo()

                # Verifica se o jogador atingiu o número máximo de tentativas
                elif self.tentativas == self.tentativas_maximas:
                    messagebox.showinfo("Game Over", f"A palavra era: {self.palavra_a_adivinhar}")
                    self.iniciar_jogo()

    def iniciar_jogo(self):
        self.tentativas = 0
        self.letras_tentadas = []
        self.obter_palavra()

        # Configuração da interface gráfica
        self.label_palavra = tk.Label(self.root, text=self.exibir_palavra_oculta(), font=('Arial', 16))
        self.label_palavra.pack(pady=10)

        self.label_letra = tk.Label(self.root, text="Digite uma letra:", font=('Arial', 12))
        self.label_letra.pack(pady=5)

        self.entry_letra = tk.Entry(self.root, font=('Arial', 12))
        self.entry_letra.pack(pady=5)

        self.button_adivinhar = tk.Button(self.root, text="Adivinhar Letra", command=self.adivinhar_letra, font=('Arial', 12))
        self.button_adivinhar.pack(pady=10)

        self.root.mainloop()

# Criar a instância do jogo
root = tk.Tk()
jogo = JogoDaForca(root)
