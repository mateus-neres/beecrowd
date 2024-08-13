import os
import sys
import re

def escrever_txt(texto, arquivo):
    caminho_diretorio = os.path.dirname(os.path.abspath(sys.argv[0]))
    arquivo_agenda = os.path.join(caminho_diretorio, arquivo)

    with open(arquivo_agenda, 'a', encoding='utf-8') as agenda:
        agenda.write(f'{texto}\n')
    print(f"Contato adicionado ao arquivo '{arquivo}'.")

def ler_txt(arquivo):
    caminho_diretorio = os.path.dirname(os.path.abspath(sys.argv[0]))
    arquivo_agenda = os.path.join(caminho_diretorio, arquivo)
    if not os.path.exists(arquivo_agenda):
        with open(arquivo_agenda, 'w', encoding='utf-8') as agenda:
            agenda.write('Novo arquivo criado.\n')
        print(f"Arquivo '{arquivo}' não encontrado. Um novo arquivo foi criado.")
        return ''
    else:
        with open(arquivo_agenda, 'r', encoding='utf-8') as agenda:
            return agenda.read()

def criar_contato():
    nome = input('Digite o nome do novo contato: ')
    telefone = input('Digite o telefone do novo contato (formato: (xx) x xxxx-xxxx): ')
    return f'{nome}: {telefone}'

def alterar_contato(arquivo):
    nome_busca = input('Digite o nome do contato que deseja alterar: ')
    contatos = ler_txt(arquivo).splitlines()
    
    encontrados = [contato for contato in contatos if nome_busca in contato]
    
    if encontrados:
        print("Contato(s) encontrado(s):")
        for i, contato in enumerate(encontrados, start=1):
            print(f'{i}. {contato}')
        
        try:
            escolha = int(input('Digite o número do contato que deseja alterar: '))
            if 1 <= escolha <= len(encontrados):
                novo_telefone = input('Digite o novo telefone (formato: (xx) x xxxx-xxxx): ')
                
                # Substitui o contato na lista
                contatos = [f'{contato.split(":")[0]}: {novo_telefone}' if i + 1 == escolha else contato for i, contato in enumerate(contatos)]
                
                # Reescreve todos os contatos no arquivo
                with open(arquivo, 'w', encoding='utf-8') as agenda:
                    agenda.write('\n'.join(contatos) + '\n')
                print("Contato alterado com sucesso.")
            else:
                print("Escolha inválida. Número fora do intervalo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
    else:
        print("Nenhum contato encontrado com esse nome.")

def buscar_contato(arquivo):
    nome_busca = input('Digite o nome do contato que deseja buscar: ')
    contatos = ler_txt(arquivo).splitlines()
    encontrados = [contato for contato in contatos if nome_busca in contato]
    
    if encontrados:
        print("Contato(s) encontrado(s):")
        for contato in encontrados:
            print(contato)
    else:
        print("Nenhum contato encontrado com esse nome.")

def menu():
    print("==================================")
    print("|[01] Adicionar novo contato      |")
    print("|[02] Alterar um contato          |")
    print("|[03] Buscar um contato pelo nome |")
    print("|[04] Ver lista de contatos       |")
    print("|[05] Sair                        |")
    print("==================================")

controle = True
while controle:
    menu()
    try:
        botao = int(input('Digite o valor referente à operação desejada: '))
        if botao == 1:
            novo_contato = criar_contato()
            escrever_txt(novo_contato, 'agenda.txt')
        elif botao == 2:
            alterar_contato('agenda.txt')
        elif botao == 3:
            buscar_contato('agenda.txt')
        elif botao == 4:
            print(ler_txt('agenda.txt'))
        elif botao == 5:
            controle = False
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
