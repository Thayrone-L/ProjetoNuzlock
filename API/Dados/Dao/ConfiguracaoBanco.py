from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config import ConfiguracaoBanco

class ConexaoBanco:
    def __init__(self):
        self.engine = None
        self.session = None
        
    def conectar(self):
        try:
            self.engine = create_engine(ConfiguracaoBanco.CONNECTION_STRING)
            Session = sessionmaker(bind=self.engine)
            self.session = Session()
            print("Conexão bem sucedida!")
        except Exception as ex:
            raise ValueError(f"Erro ao conectar ao banco de dados: {ex}")
        
    def executar_procedure(self, nome_procedure, parametros):
        try:
            placeholders = ', '.join([':' + str(i) for i in range(1, len(parametros)+1)])
            sql = f"EXEC {nome_procedure} {placeholders}"
            result = self.session.execute(text(sql), parametros)
            
            if result.returns_rows:
                results = result.fetchall()
                return results
            else:
                return {"mensagem":"Operação realizada com sucesso!"}
        except Exception as ex:
            self.session.rollback()
            raise ValueError(f"Erro ao executar a procedure: {ex}")
                             
    def fechar_conexao(self):
        try:
            if self.session:
                self.session.close()
                print("Conexão fechada")
        except Exception as ex:
            raise ValueError(f"Erro ao fechar a sessão: {ex}")