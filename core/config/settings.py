from os.path import abspath, join, dirname


class Settings:

    ROOT_PATH = dirname(dirname(dirname(abspath(__file__))))

    DATA_PATH = join(ROOT_PATH, "data")

    DATA_ENDERECO_PATH = join(DATA_PATH, "enderecos.json")
    DATA_MEDICO_PATH = join(DATA_PATH, "medico.json")
    DATA_PACIENTE_PATH = join(DATA_PATH, "paciente.json")
    DATA_AGENDA_PATH = join(DATA_PATH, "agenda.json")

    ENTILY_PATH = join(ROOT_PATH, "entily")
    PESSOA_PATH = join(ENTILY_PATH, "cls_pessoa.py")

    ENDERECOS_PATH = join(ENTILY_PATH, "endereco")
    CLS_ENDERECO_PATH = join(ENDERECOS_PATH, "cls_endereco.py")

    AGENDA_PATH = join(ENTILY_PATH, "agenda")
    CLS_AGENDA_PATH = join(AGENDA_PATH, "cls_agenda.py")


