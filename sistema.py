import sqlite3

def criar_tabela():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            idade INTEGER NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()

def adicionar_usuario():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    idade = input("Digite a idade: ")

    try:
        cursor.execute("INSERT INTO usuarios (nome, email, idade) VALUES (?, ?, ?)", (nome, email, idade))
        conexao.commit()
        print("Usuário adicionado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Já existe um usuário com este e-mail.")
    finally:
        conexao.close()

def listar_usuarios():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    if usuarios:
        print("\nLista de Usuários:")
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, E-mail: {usuario[2]}, Idade: {usuario[3]}")
    else:
        print("Nenhum usuário cadastrado.")

    conexao.close()

def atualizar_usuario():
    listar_usuarios()
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    try:
        usuario_id = int(input("Digite o ID do usuário que deseja atualizar: "))
        nome = input("Digite o novo nome: ")
        email = input("Digite o novo e-mail: ")
        idade = input("Digite a nova idade: ")

        cursor.execute("""
            UPDATE usuarios 
            SET nome = ?, email = ?, idade = ?
            WHERE id = ?
        """, (nome, email, idade, usuario_id))
        
        if cursor.rowcount == 0:
            print("Usuário não encontrado.")
        else:
            conexao.commit()
            print("Usuário atualizado com sucesso!")
    except ValueError:
        print("Por favor, insira um ID válido.")
    finally:
        conexao.close()

def remover_usuario():
    listar_usuarios()
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()

    try:
        usuario_id = int(input("Digite o ID do usuário que deseja remover: "))
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))

        if cursor.rowcount == 0:
            print("Usuário não encontrado.")
        else:
            conexao.commit()
            print("Usuário removido com sucesso!")
    except ValueError:
        print("Por favor, insira um ID válido.")
    finally:
        conexao.close()

def menu():
    criar_tabela()
    while True:
        print("\nSistema de Gerenciamento de Usuários")
        print("1 - Adicionar usuário")
        print("2 - Listar usuários")
        print("3 - Atualizar usuário")
        print("4 - Remover usuário")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            remover_usuario()
        elif opcao == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o sistema de gerenciamento
menu()

