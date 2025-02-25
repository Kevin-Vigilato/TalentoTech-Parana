import pandas as pd
import os

data = {
    'Nome': [],
    'Idade': [],
    'Emprego': [],
    'Salário': []
}
df = pd.DataFrame(data)

def limpar_tela():
    os.system('clear')  # Para Linux/macOS
    # os.system('cls')  # Para Windows

def exibir_cadastros():
    limpar_tela()
    if df.empty:
        print("Nenhum registro encontrado.")
    else:
        print("\nLista de Cadastros:")
        print(df.to_string(index=True))

def adicionar():
    global df
    limpar_tela()
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    emprego = input("Emprego: ").strip()
    salario = float(input("Salário: "))
    df = pd.concat([df, pd.DataFrame({'Nome': [nome], 'Idade': [idade], 'Emprego': [emprego], 'Salário': [salario]})], ignore_index=True)
    limpar_tela()
    print("\nCadastro concluído com sucesso!\nPressione Enter para voltar à tela inicial.")
    input()

def listar():
    exibir_cadastros()
    input("\nPressione Enter para voltar ao menu.")

def editar():
    global df
    exibir_cadastros()
    if df.empty:
        input("\nPressione Enter para voltar ao menu.")
        return

    try:
        escolha = input("\nDigite o nome ou o número do cadastro a editar: ").strip()
        if escolha.isdigit():
            escolha = int(escolha)  
        else:
            escolha = df[df['Nome'].str.lower() == escolha.lower()].index[0]  

        if escolha in df.index:
            print(f"\nEditando {df.loc[escolha, 'Nome']}:")
            df.at[escolha, 'Nome'] = input("\nNome: ").strip()
            df.at[escolha, 'Idade'] = int(input("\nIdade: "))
            df.at[escolha, 'Emprego'] = input("\nEmprego: ").strip()
            df.at[escolha, 'Salário'] = float(input("\nSalário: "))
            limpar_tela()
            print("\nCadastro concluído com sucesso!\nPressione Enter para voltar à tela inicial.")
        else:
            print("\nCadastro não encontrado.")
    except (ValueError, IndexError):
        print("\nOpção inválida. Tente novamente.")
    input()

def deletar():
    global df
    exibir_cadastros()
    if df.empty:
        input("\nPressione Enter para voltar ao menu.")
        return

    try:
        escolha = input("\nDigite o nome ou o número do cadastro a excluir: ").strip()
        if escolha.isdigit():  
            escolha = int(escolha)  
        else:
            escolha = df[df['Nome'].str.lower() == escolha.lower()].index[0] 

        if escolha in df.index:
            df = df.drop(escolha).reset_index(drop=True)  
            limpar_tela()
            print("\nCadastro excluido com sucesso!\nPressione Enter para voltar à tela inicial.")
        else:
            print("\nCadastro não encontrado.")
    except (ValueError, IndexError):
        print("\nOpção inválida. Tente novamente.")
    input()

def menu():
    while True:
        limpar_tela()
        print("\n[1] Adicionar | [2] Listar | [3] Editar | [4] Deletar | [5] Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            adicionar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            editar()
        elif opcao == '4':
            deletar()
        elif opcao == '5':
            limpar_tela()
            print("Saindo...")
            break
        else:
            print("Opção inválida.")
            input("\nPressione Enter para tentar novamente.")

menu()
