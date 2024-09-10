# main.py
from jogo import *
from usuario import *
from menu import *
from facades import *
from decorator_jogo import JogoComDesconto  # Importa o decorator

if __name__ == "__main__":
  
    # Criando os jogos
    jogo_coup = JogoDeTabuleiro('coup', 100)  # Adicionei o preço para os jogos
    jogo_uno = JogoDeTabuleiro('UNO', 50)
    jogo_baralho = JogoDeTabuleiro('baralho', 30)
    jogo_war = JogoDeTabuleiro('war', 200)
    jogo_xadrez = JogoDeTabuleiro('xadrez', 120)
    jogo_damas = JogoDeTabuleiro('damas', 80)

    # Criando os usuários
    usuario_eduarda = usuario("Eduarda", 'eduardaaraujo492@gmail.com')
    usuario_nyedson = usuario("Nyedson", 'nyedsonlorranoficial@gmail.com')
    usuario_eduardo = usuario("Eduardo", 'eduardodosreissouza@gmail.com')
    usuario_joaoPaulo = usuario('Joao Paulo', 'joaopaulocarneirofialho@gmail.com')
    usuario_diogo = usuario('Diogo', 'diogo.rslira@gmail.com')
    usuario_vinicius = usuario('Vinicius', 'basilio.vinicius@academico.ifpb.edu.br')

    # Adicionando observadores aos jogos
    jogo_coup.AddObsrvadores(usuario_eduarda)
    jogo_uno.AddObsrvadores(usuario_nyedson)
    jogo_baralho.AddObsrvadores(usuario_eduardo)
    jogo_war.AddObsrvadores(usuario_joaoPaulo)
    jogo_xadrez.AddObsrvadores(usuario_diogo)
    jogo_damas.AddObsrvadores(usuario_vinicius)

    # Alterando a disponibilidade dos jogos
    jogo_coup.alterarDisponibilidade(True)
    jogo_uno.alterarDisponibilidade(False)
    jogo_baralho.alterarDisponibilidade(True)
    jogo_war.alterarDisponibilidade(True)
    jogo_xadrez.alterarDisponibilidade(True)
    jogo_damas.alterarDisponibilidade(True)

    # Aplicando o decorator para adicionar desconto em alguns jogos
    jogo_couple_com_desconto = JogoComDesconto(jogo_coup, 0.10)  # 10% de desconto
    jogo_war_com_desconto = JogoComDesconto(jogo_war, 0.20)  # 20% de desconto

    # Exibindo detalhes dos jogos com desconto
    print("\nJogos com desconto:")
    jogo_couple_com_desconto.exibir_detalhes()
    jogo_war_com_desconto.exibir_detalhes()

    # Exibindo detalhes dos jogos sem desconto
    print("\nJogos sem desconto:")
    jogo_uno.exibir_detalhes()
    jogo_baralho.exibir_detalhes()
    jogo_xadrez.exibir_detalhes()
    jogo_damas.exibir_detalhes()
