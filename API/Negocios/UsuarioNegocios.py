import sys
sys.path.append(r'C:\Users\thayr\OneDrive\Documentos\repositorios\Python\ProjetoNuzlock\API')
import re
import random
import string
from flask_mail import Message
from flask import current_app
from Dados.Dao.extensoes import mail
from Dados.UsuarioDados import UsuarioDados

class UsuarioNegocios:
    def __init__(self):
        self.usuario_dados = UsuarioDados()

    def validar_formato_email(self, email):
        regex_email = re.compile(r'^\S+@\S+\.\S+$')
        return bool(regex_email.match(email))

    def gerar_codigo_aleatorio(self, tamanho=6):
        caracteres = string.ascii_letters + string.digits
        return ''.join(random.choice(caracteres) for _ in range(tamanho))

    def enviar_codigo_por_email(self, destinatario, codigo):
        mensagem = Message('Código de Verificação', sender=current_app.config['MAIL_USERNAME'], recipients=[destinatario])
        mensagem.body = f'Seu código de verificação: {codigo}'
        
        try:
            mail.send(mensagem)
        except Exception as e:
            # Lidar com exceções de envio de e-mail conforme necessário
            print(f"Erro ao enviar e-mail: {e}")

    def criar_usuario_temporario(self, nome, email, senha):
        if not nome or not email or not senha:
            raise ValueError("Nome, e-mail e senha são obrigatórios.")

        if not self.validar_formato_email(email):
            raise ValueError("E-mail inválido.")

        codigo_aleatorio = self.gerar_codigo_aleatorio()
        self.enviar_codigo_por_email(email, codigo_aleatorio)

        usuario_temporario = {"nome": nome, "email": email, "senha": senha, "codigo": codigo_aleatorio}
        self.usuario_dados.salvar_usuario_temporario(usuario_temporario)

        return {"codigo_aleatorio": codigo_aleatorio}

    def verificar_codigo_e_criar_usuario_definitivo(self, email, codigo):
        usuario_temporario = self.usuario_dados.obter_usuario_temporario_por_email_e_codigo(email, codigo)

        if usuario_temporario:
            self.usuario_dados.salvar_usuario_definitivo(usuario_temporario)
            self.usuario_dados.remover_usuario_temporario(usuario_temporario)
            return {"mensagem": "Usuário criado com sucesso!"}
        else:
            raise ValueError("Código inválido ou expirado.")
