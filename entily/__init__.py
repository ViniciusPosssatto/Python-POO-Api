from time import sleep

from entily.agenda.cls_agenda import Agenda
from entily.pessoas.cls_pessoa import Pessoa
from entily.pessoas.cls_medico import Medico
from entily.pessoas.cls_paciente import Paciente
from entily.endereco.cls_endereco import Endereco


if __name__ == "__main__":
    while True:
        print(

            '''
            Bem vindo ao sistema clínico de saúde
                    Opções:
                    [1] Cadastrar Médico
                    [2] Cadastrar Paciente
                    [3] Cadastrar Agenda
                    [4] Exibir endereços cadastrados
                    [0] Sair \n
            '''

        )
        opc1 = int(input('Digite sua opção: '))
        print('=-=-=-=-=-=-=')
        if opc1 == 1:
            print(f'Cadastro de médico:')
            nome = input('Digite o nome: ')
            email = input('Digite o email: ')
            tel = int(input('Digite um telefone: '))
            cep = int(input('Digite o CEP:'))
            med = Medico(nome, email, tel, cep)
            med.endereco = Endereco().cadastrar_endereco(cep)
            med.cadastrar_medico(nome)
            opc = ' '
            while opc not in 'SN':
                print('Mostrar lista de médicos?')
                opc = input('Digite [Sim] ou [Não] = ').strip().upper()[0]
                if opc == 'S':
                    med.exibir_pessoa()
                    break
                if opc == 'N':
                    break
        if opc1 == 2:
            print('Cadastro de paciente:')
            nome = input('Digite o nome: ')
            email = input('Digite o email: ')
            tel = int(input('Digite um telefone: '))
            cep = int(input('Digite o CEP:'))
            pac = Paciente(nome, email, tel, cep)
            pac.endereco = Endereco().cadastrar_endereco(cep)
            pac.cadastrar_paciente(nome)
            opc = ' '
            while opc not in 'SN':
                print('Mostrar lista de pacientes?')
                opc = input('Digite [Sim] ou [Não] = ').strip().upper()[0]
                if opc == 'S':
                    pac.exibir_pessoa()
                    break
                if opc == 'N':
                    break
        if opc1 == 3:
            print('Cadastro de consulta:')
            crm = input('Digite o CRM do médico: ')
            cpf = input('Digite o CPF do paciente: ')
            dia = int(input('Digite o dia da consulta: '))
            mes = int(input('Digite o mês da consulta: '))
            ano = int(input('Digite o ano da consulta: '))
            hora = input('Qual o horário marcado [ hh:mm ]: ')
            obs = input('Observações da consulta: ')
            agenda = Agenda(crm, cpf, dia, mes, ano, hora, obs)
            agenda.cadastrar_agenda()
            opc = ' '
            while opc not in 'SN':
                print('Mostrar lista de consultas?')
                opc = input('Digite [Sim] ou [Não] = ').strip().upper()[0]
                if opc == 'S':
                    agenda.exibir_agenda()
                    break
                if opc == 'N':
                    break
        if opc1 == 4:
            Endereco().exibir_endereco()

        if opc1 == 0:
            break

    print('Você saiu do sistema...')
    sleep(1)
    print("FIM")
