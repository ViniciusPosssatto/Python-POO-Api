from os.path import isfile
from json import dump, load
from .cls_pessoa import Pessoa
from time import sleep


class Paciente(Pessoa):

    def __init__(self, nome: str, email: str, tel: int, cep: int):
        self.rg = None
        self.cpf = None
        self.convenio = None
        self.data_nasc = None
        self.cep = cep
        self.endereco = None
        self.__chaves = ["nome", "telefone", "rg", "cpf", "email", "convenio", "data_nasc", "CEP"]
        super().__init__(nome, email, tel)

    def cadastrar_paciente(self, nome):
        print(f'Cadastrar paciente {nome}?')
        opc = ' '
        while opc not in 'SN':
            opc = input('Digite [Sim] ou [Não] = ').strip().upper()[0]
            if opc == 'S':
                print('Cadastro de paciente:')
                self.rg = int(input('Digite o número do RG: '))
                self.cpf = int(input('Digite o número do CPF: '))
                self.convenio = input('O paciente possui convenio: ')
                self.data_nasc = input('Digite a data de nascimento [ dd/mm/aaaa ]: ')
                lista_dados = [self.nome, self.email, self.rg, self.cpf, self.celular, self.convenio,
                               self.data_nasc, self.cep]
                data = dict(zip(self.__chaves, lista_dados))
                self.pessoas_p["pacientes"].append(data)
                self.salvar_paciente(self.pessoas_p)
                print('Cadastro de paciente efetuado...')
                sleep(1)
                break
            if opc == 'N':
                print('Cancelando cadastro de paciente...')
                sleep(1)
                break

    def exibir_pessoa(self):
        try:
            with open(self.paciente_path, 'r+') as f:
                data = load(f)
                dados = data['pacientes']
                for item in dados:
                    print(f"O nome da pessoa é {item['nome']}, celular: {item['telefone']} e email: "
                          f"{item['email']}.")
        except Exception as error:
            print(f'Erro exibir paciente = {error}')

    def salvar_paciente(self, paciente):
        try:
            if not isfile(self.paciente_path):
                with open(self.paciente_path, 'w') as f:
                    dump(paciente, f, indent=2, separators=(',', ': '))
            else:
                with open(self.paciente_path, 'r+') as f:
                    dados = load(f)
                    dados["pacientes"].append(paciente["pacientes"][0])
                with open(self.paciente_path, 'w') as f:
                    dump(dados, f, indent=2, separators=(',', ': '))
        except Exception as error:
            print(f'Erro salvar paciente = {error}')
