import requests
from os.path import isfile
from json import dump, load
from time import sleep
from core.config.settings import Settings


class Endereco:

    def __init__(self):
        self.logradouro: str = None
        self.numero: int = None
        self.complemento: str = None
        self.bairro: str = None
        self.cidade: str = None
        self.uf: str = None
        self.enderecos = []
        self.endereco_path = Settings().DATA_ENDERECO_PATH

    def cadastrar_endereco(self, cep):
        print('Cadastrar endereço?')
        opc1 = ' '
        while opc1 not in 'SN':
            opc1 = input('Digite [Sim] ou [Não] = ').strip().upper()[0]
            if opc1 == 'S':
                try:
                    request = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
                    num = int(input('Digite o número da sua casa: '))
                    end = request.json()
                    end['numero'] = num
                    print(f"Confirmar endereço: {end['localidade']}/{end['uf']}, {end['bairro']}, Nº {num}?")
                    opc = ' '
                    while opc not in 'SN':
                        opc = input('Digite [Sim] ou [Não] = ').strip().upper()[0]
                        if opc == 'S':
                            del end['gia']
                            del end['siafi']
                            del end['ibge']
                            self.enderecos.append(end)
                            print(self.enderecos)
                            Endereco.salvar_endereco(self.endereco_path, self.enderecos)
                            print('Cadastro de endereço efetuado...')
                            sleep(1)
                            break
                        if opc == 'N':
                            self.cidade = input('Digite sua cidade: ').capitalize()
                            self.uf = input('Digite seu estado: ').upper()
                            self.bairro = input('Digite seu bairro: ').capitalize()
                            self.logradouro = input('Digite sua rua: ').capitalize()
                            self.numero = int(input('Digite o número da sua casa: '))
                            self.complemento = input('Digite o complemento: ').capitalize()
                            self.enderecos.append({'cep': cep,
                                                   'logradouro': self.logradouro,
                                                   'complemento': self.complemento,
                                                   'bairro': self.bairro,
                                                   'localidade': self.cidade,
                                                   'uf': self.uf,
                                                   'numero': self.numero})
                            Endereco.salvar_endereco(self.endereco_path, self.enderecos)
                            print('Cadastro de endereço efetuado...')
                            sleep(1)
                            break
                except Exception as exception:
                    print(f'Erro cadastro endereço = {exception}')

            if opc1 == 'N':
                print('Cadastro de endereço cancelado...')
                sleep(1)
                break

    def exibir_endereco(self):
        try:
            with open(self.endereco_path, 'r+') as f:
                datas = load(f)
                for data in datas:
                    print(f"Endereço: {data['localidade']}/{data['uf']}, {data['logradouro']} - "
                          f"bairro {data['bairro']}, número {data['numero']}.")

        except FileNotFoundError as error:
            print('Arquivo não existe.')
            cep = int(input('Informe o seu CEP: '))
            self.cadastrar_endereco(cep)
        except Exception as error:
            print(f'Erro exibir endereço = {error}')

    @staticmethod
    def salvar_endereco(filepath, endereco):
        try:
            path_enderecos = filepath
            if not isfile(path_enderecos):
                with open(path_enderecos, 'w') as f:
                    dump(endereco, f, indent=2, separators=(',', ': '))
            else:
                with open(path_enderecos, 'r+') as f:
                    dados = load(f)
                    dados.append(endereco[0])
                with open(path_enderecos, 'w') as f:
                    dump(dados, f, indent=2, separators=(',', ': '))
        except Exception as exception:
            print(f'Erro save endereço = {exception}')
