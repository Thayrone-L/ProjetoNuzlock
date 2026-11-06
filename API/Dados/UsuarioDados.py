from Dao.ConfiguracaoBanco import Dao
from sqlalchemy.exc import SQLAlchemyError

class UsuarioDados:
    def __init__(self):
        self.dao = Dao()

    def salvar_usuario_temporario(self, usuario_temporario):
        try:
            self.dao.adicionar(usuario_temporario)
            self.dao.commit()
        except SQLAlchemyError as e:
            self.dao.rollback()
            raise ValueError(f"Erro ao salvar usuário temporário: {e}")

    def obter_usuario_temporario_por_email_e_codigo(self, email, codigo):
        try:
            # Supondo que você tenha um método de consulta personalizado em sua classe DAO
            usuario_temporario = self.dao.obter_usuario_temporario_por_email_e_codigo(email, codigo)
            return usuario_temporario
        except SQLAlchemyError as e:
            raise ValueError(f"Erro ao obter usuário temporário: {e}")

    def salvar_usuario_definitivo(self, usuario_definitivo):
        try:
            self.dao.adicionar(usuario_definitivo)
            self.dao.commit()
        except SQLAlchemyError as e:
            self.dao.rollback()
            raise ValueError(f"Erro ao salvar usuário definitivo: {e}")

    def remover_usuario_temporario(self, usuario_temporario):
        try:
            self.dao.remover(usuario_temporario)
            self.dao.commit()
        except SQLAlchemyError as e:
            self.dao.rollback()
            raise ValueError(f"Erro ao remover usuário temporário: {e}")
