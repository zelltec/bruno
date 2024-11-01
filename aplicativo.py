#bruno nunes

import tkinter as tk
from tkinter import ttk
import random

#Listas de palavras para compor o nome da empresa
suffixes = ['Solutions', 'Systems', 'Corporation', 'Holdings', 'Enterprises', 'Networks']
prefixes = ['Tech', 'Info', 'Global', 'Net', 'Data', 'Auto']
nouns = ['Innovators', 'Dynamics', 'Tech', 'Labs', 'Edge', 'Consulting']

#Função para gerar um nome de empresa
def generate_company_name():
  prefix = random.choice(prefixes)
  suffix = random.choice(suffixes)
  noun = random.choice(nouns)
  return f'(prefix)(noun)(suffix)'

#Função para gerar e mostrar nomes na interface gráfica
def generate_and_display_names():
   #Limpa a área de exibição de nomes
   name_display.delete(1.0, tk.END)

   #Gera os nomes e exibe na área de texto
try:
  number_of_names= int(entry.get())
  if number_of_names <= 0:
    raise ValueError
  generated_names = generate_multiple_names(number_of_names)
  for name in generated_names:
     name_display.insert(tk.END, name + '\n')
except ValueError:
  name_display.insert(tk.END,'Por favor, insira um número válido.\n')

#Função para gerar múltiplos nomes def generate_multiple_names(n):
def generate_multiple_names(n):
  names = []
  for _ in range(n):
     names = names.append(generate_company_name())
  return names

#Criando a janela principal
root = Tk.Tk()
root.title("Gerador de Nomes de Empresas")

#Tamanho da janela
root.geometry('400x300')

#Rótulo de instrução
instruction_label = ttk.Label(root, text="Digite o número de nomes a gerar:")
instruction_label.pack(pady=10)

#Entrada para o número de nomes
entry = ttk.Entry(root)
entry.pack()

#Botão para gerar nomes
generate_button = ttk.Button(root, text="Gerar Nomes",
command=generate_and_display_names)
generate_button.pack(pady=10)

#Area de texto para exibir os nomes gerados
name_display = tk. Text(root, height=10, width=40)
name_display.pack()

#Loop principal da janela
root.mainloop()