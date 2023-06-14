from tkinter import*
from tkinter import Tk, ttk

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def verificar_senha(self, senha):
        if senha == self.senha:
            print("Senha Correta!!")
        else:
            print("Senha Incorreta!!")

class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao

class Gerenciamento:
    def __init__(self):
        self.projeto = []

    def adicionar_projetos(self, projeto):
        self.projetos.append(projeto)

    def exibir_projetos(self):
        for projeto in self.projetos:
            print("Nome: ", projeto.nome)
            print("Descrição: ", projeto.descricao)