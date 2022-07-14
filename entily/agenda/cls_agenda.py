from os.path import isfile
from json import dump, load
from time import sleep
from core.config.settings import Settings
from entily.pessoas import Paciente, Medico


class Agenda(Paciente, Medico):

    def __init__(self, crm: str, cpf: str, dia: int, mes: int, ano: int, hora: str, obs: str):
        self.crm_med = crm
        self.cpf_paciente = cpf
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.hora = hora
        self.obs = obs
        self.__chaves = ["CRM", "CPF-Paciente", 'Dia', 'Mês', 'Ano', 'Hora', 'Observação']
        self.agenda = {"agenda": []}
        self.agenda_path = Settings().DATA_AGENDA_PATH

    def cadastrar_agenda(self):

        lista_dados = [self.crm_med, self.cpf_paciente, self.dia, self.mes, self.ano, self.hora, self.obs]
        data = dict(zip(self.__chaves, lista_dados))
        self.agenda["agenda"].append(data)
        self.salvar_agenda(self.agenda)
        print('Consulta agendada...')
        sleep(1)

    def exibir_agenda(self):
        try:
            with open(self.agenda_path, 'r+') as f:
                data = load(f)
                dados = data['agenda']
                for item in dados:
                    print(f"Dia {item['Dia']}/{item['Mês']}/{item['Ano']} = consulta com o médico CRM: "
                          f"{item['CRM']} para o paciente CPF: {item['CPF-Paciente']} - OBS: {item['Observação']}.")

        except Exception as error:
            print(f'Erro exibir agenda = {error}')

    def salvar_agenda(self, agenda):
        try:
            if not isfile(self.agenda_path):
                with open(self.agenda_path, 'w') as f:
                    dump(agenda, f, indent=2, separators=(',', ': '))
            else:
                with open(self.agenda_path, 'r+') as f:
                    dados = load(f)
                    dados["agenda"].append(agenda["agenda"][0])
                with open(self.agenda_path, 'w') as f:
                    dump(dados, f, indent=2, separators=(',', ': '))
        except Exception as error:
            print(f'Erro salvar agenda = {error}')
