import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class usuario:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email

    def atualizar(self, jogo):
        if not jogo.alugado:      #aqui verifica se o jogo esta disponível e so envia se estiver
            self.enviarEmail(jogo)

    def enviarEmail(self,jogo):
        remetente = "nyedson.lorran@academico.ifpb.edu.br"  #zaelli criar email para o tabuland...
        senha= "mrsp uzrk erwg svhm"
        assunto= f"jogo {jogo.titulo} disponível!!"
        #linkSite = "https://github.com/zaelii/TabuLend"

        with open('templates/templateEmail.html', 'r',  encoding='utf-8') as file:
            mensagem = file.read()

        mensagem = mensagem.replace('{{nome}}', self.nome)
        mensagem = mensagem.replace('{{titulo}}', jogo.titulo)
        mensagem = mensagem.replace('{{link}}', 'https://github.com/zaelii/TabuLend')   #mudar para o link do site

        #criando a mensagem do email pela biblioteca 
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = self.email
        msg['Subject'] = assunto 
        msg.attach(MIMEText(mensagem, 'html', 'UTF-8'))


        #configuração da biblioteca 
        try:
            servidor = smtplib.SMTP('smtp.gmail.com', 587)
            servidor.starttls()
            servidor.login(remetente,senha)
            servidor.sendmail(remetente,self.email, msg.as_string())
            servidor.quit()
            print(f'email enviado para {self.email} com sucesso!!')
        except Exception as a:
            print(f'erro ao enviar o email: {a}')






    
