# main.py
from jogo import *
from usuario import *
from menu import *
from facades import *

if __name__ == "__main__":
  
    jogo_couple = JogoDeTabuleiro('couple')
    jogo_uno = JogoDeTabuleiro('UNO')
    jogo_baralho = JogoDeTabuleiro('baralho')
    jogo_war = JogoDeTabuleiro('war')
    jogo_xadrez = JogoDeTabuleiro('xadez')
    jogo_damas = JogoDeTabuleiro('damas')

    usuario_eduarda = usuario("Eduarda", 'eduardaaraujo492@gmail.com')
    usuario_nyedson = usuario("Nyedson", 'nyedsonlorranoficial@gmail.com')
    usuario_eduardo = usuario("Eduardo", 'eduardodosreissouza@gmail.com')
    usuario_joaoPaulo = usuario('Joao paulo', 'joaopaulocarneirofialho@gmail.com')
    usuario_diogo = usuario('Diogo', 'diogo.rslira@gmail.com')
    usuario_vinicius = usuario('Vinicius', 'basilio.vinicius@academico.ifpb.edu.br')


    jogo_couple.AddObsrvadores(usuario_eduarda)
    jogo_uno.AddObsrvadores(usuario_nyedson)
    jogo_baralho.AddObsrvadores(usuario_eduardo)
    jogo_war.AddObsrvadores(usuario_joaoPaulo)
    jogo_xadrez.AddObsrvadores(usuario_diogo)
    jogo_damas.AddObsrvadores(usuario_vinicius)


    jogo_couple.alterarDisponibilidade(True)
    jogo_uno.alterarDisponibilidade(False)
    jogo_baralho.alterarDisponibilidade(True)
    jogo_war.alterarDisponibilidade(True)
    jogo_xadrez.alterarDisponibilidade(True)
    jogo_damas.alterarDisponibilidade(True)
    