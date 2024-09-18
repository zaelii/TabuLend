import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app import *
from jogo import *
from usuario import  *

jogos_path = 'catalogoJogos.txt'
dados_login_path = 'DadosLogin.txt'
imagens_jogos_path = 'static/imagens/jogos'



class JogoDeTabuleiro:

    def __init__(self, titulo, editora,preco,status,imagem):
        self.titulo = titulo  # Título do jogo de tabuleiro
        self.editora = editora
        self.preco = preco  # Preço do jogo
        self.status = status
        self.imagem = imagem
        self.observadores = []  # Lista onde ficarão usuários que querem receber notificação da alteração do jogo

    def AddObsrvadores(self, email):  # Adiciona um observador na lista
        if email not in self.observadores:
            self.observadores.append(email)

    def RemoverObsrvadores(self, observador):  # Remove um observador da lista
        self.observadores.remove(observador)

    def NotificarObservadores(self):  # Notifica todos da lista sobre a disponibilidade do jogo
        for email in self.observadores:
            enviar_email_para_observadores(email,self)
        self.observadores = []


    def alterarDisponibilidade(self, alugado): 
        self.status = 'alugado' if alugado else 'disponivel'
        if not alugado:
            self.NotificarObservadores()

    def calcular_preco(self):
        """Método que retorna o preço do jogo."""
        return self.preco

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Preço: R$ {self.preco}, Status: {'Alugado' if self.alugado else 'Disponível'}")


    @staticmethod
    def catalogoJogos():
        jogos = []
        try:
            with open('catalogoJogos.txt', 'r') as file:
                for line in file:
                    partes = line.strip().split(', ')
                    titulo = partes[0].split(': ')[1]
                    editora = partes[1].split(': ')[1]
                    preco = partes[2].split(': ')[1]
                    status = partes[3].split(': ')[1]
                    imagem = partes[4].split(': ')[1] if len(partes) > 4 else None
                    jogos.append(JogoDeTabuleiro(titulo, editora, preco, status, imagem))
        except FileNotFoundError:
            print("Arquivo de catálogo de jogos não encontrado.")
        return jogos 
    

    def salvarJogoNovo(self):
        with open('catalogoJogos.txt', 'a') as file:
            file.write(f"titulo: {self.titulo}, editora: {self.editora}, preco: {self.preco}, status: {self.status}, imagem: {self.imagem},  observadores: {','.join(self.observadores)}\n")

    
def buscar_email_do_usuario(username):
    """Função para buscar o e-mail do usuário no arquivo DadosLogin.txt baseado no username."""

    try:
        with open(dados_login_path, 'r') as file:
            for linha in file:
                # Remove espaços em branco nas extremidades e separa as partes da linha
                partes = linha.strip().split(', ')
                
                # Cria um dicionário para armazenar os dados do usuário
                usuario = {}
                
                # Itera sobre cada parte da linha para preencher o dicionário
                for parte in partes:
                    if ': ' in parte:
                        chave, valor = parte.split(': ', 1)
                        usuario[chave.strip()] = valor.strip()
                    else:
                        print(f"Formato inesperado na linha: {parte}")
                
                # Verifica se o username da linha corresponde ao username procurado
                if usuario.get('username') == username:
                    return usuario.get('email')

    except FileNotFoundError:
        print("Arquivo DadosLogin.txt não encontrado.")
    except Exception as e:
        print(f"Erro ao buscar e-mail do usuário: {e}")

    return None  # Retorna None se o username não for encontrado ou se ocorrer um erro
