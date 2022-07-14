from core.config.settings import Settings


class Pessoa:

    def __init__(self, nome, celular, email):
        self.nome: str = nome
        self.celular: int = celular
        self.email: str = email
        self.pessoas_p = {"pacientes": []}
        self.pessoas_m = {"medicos": []}
        self.medico_path = Settings().DATA_MEDICO_PATH
        self.paciente_path = Settings().DATA_PACIENTE_PATH

    def cadastrar_pessoa(self):
        pass

    def exibir_pessoa(self):
        pass

    @staticmethod
    def salvar_pessoa(path, pessoa):
        pass
