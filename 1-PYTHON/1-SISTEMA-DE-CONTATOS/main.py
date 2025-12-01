import os
from time import sleep

contatos = [
    {
    "nome":"Leirisson",
    "telefone":"98996589965",
    "email":"leirisson@example.com",
    "favorito": "Favorito"
    },
    {
    "nome":"Maria",
    "telefone":"96332459986",
    "email":"maria@example.com",
    "favorito": "Não é favorito"
    }
    ]


def linha(qtd_caracter):
    print("#" * qtd_caracter)

def limpar_tela():
    os.system("cls")

def pausar_terminal(tempo):
    sleep(tempo)
    
def iniciar_sistema(titulo:str):
    caracteres = len(titulo)
    for i in range(caracteres):
        pausar_terminal(.1)
        limpar_tela()
        linha(i)
        print(titulo.upper())
        linha(i)
        print(end="")
        
        

def titulo_sistema(titulo: str):
    qtd_caracter = len(titulo)
    titulo_upper =  titulo.upper()
    iniciar_sistema(titulo)
    limpar_tela()
    linha(qtd_caracter)
    print(titulo_upper)
    linha(qtd_caracter)

def verifica_se_e_favorito(status):
    e_favorito = (status == "sim" or status == "s")
    if e_favorito:
        return "Favorito"
    return "Não é favorito"

def pesquisar_contato_por_nome(nome):
    for contato in contatos:
        nome_contato = contato['nome'].lower()
        if(nome in nome_contato):
            return contato
        
        
def menu(opcoes_menu):
    for opcao in opcoes_menu:
        print(opcao.upper())

def main():
    titulo = "sistema de registro de contato".upper()
    opcoes_menu = [
            '1 - Adicionar novo contato', 
            '2 - Listar contatos', 
            '3 - favoritar um contato', 
            '4 - Listar favoritos',
            '5 - Apagar um contato',
            '6 - Editar um contato',
            '0 - Sair do sistema'
            ]
    
    while True:
        titulo_sistema(titulo)
        menu(opcoes_menu)
        op = input("Escolha uma opção <: ")
        match(op):
            case "1":
          
                while True:
                    titulo_sistema("Cadastrar Novo contato")
                    nome = input("nome <: ")
                    telefone = input("telefone <: ")
                    email = input("e-mail <: ")
                    favorito = input("adicionar aos favoritos (S-sim / N-Não) <: ").lower()
                    
                    e_favorito = verifica_se_e_favorito(favorito)
                    
                    contatos.append({
                        "nome":nome,
                        "telefone":telefone,
                        "email":email,
                        "favorito":e_favorito
                    })
                    
                    cad_outro = input("deseja cadastrar ouro contato: (S-sim / N-Não)").lower()
                    vai_cadastrar_de_novo = (cad_outro == "s" or cad_outro == "sim")
                    
                    if vai_cadastrar_de_novo:
                        continue
                    else:
                        break
            case "2":
                titulo_sistema("Todos os contatos")
                contador_contatos = 0
                if(len(contatos) == 0):
                    print("Nem um contatos adicionado até o momento.")
                    input("Aperte qualquer tecla para continuar...")
                    
                else:
                    for contato in contatos:
                        print(f"{contador_contatos+1}: Nome: {contato['nome']} | Telefone: {contato['telefone']} | E-mail: {contato['email']} | Favorito:  {contato['favorito']}")
                        contador_contatos += 1
                    input("Aperte qualquer tecla para continuar...")
                    
            case "3":
                titulo_sistema("Adicionar um contato como favorito")
                pesquisar_nome = input("digite o nome do contato: ")
                contato_encontrato  = pesquisar_contato_por_nome(pesquisar_nome)
                if(len(contato_encontrato) == 0 ):
                    print("Nem um contato encontrado com esse nome.")
                else: 
                    print(f"Contato: ")
                    print(f"Nome: {contato_encontrato['nome']} | Favorito: {contato_encontrato['favorito']}")
                    favorito = input("adicionar aos favoritos (S-sim / N-Não) <: ").lower()
                    e_favorito = verifica_se_e_favorito(favorito)
                    contato_encontrato['favorito'] = e_favorito
                    input("Aperte em qualquer tecla para continuar...")

            case "4":
                titulo_sistema("Lista de contatos favoritos")
                for contato_favorito in contatos:
                    if(contato_favorito['favorito'] == "Favorito"):
                        print(f"Nome: {contato_favorito['nome']} | Telefone {contato_favorito['telefone']} | E-mail {contato_favorito['email']} | Favorito: {contato_favorito['favorito']}")
                input("A perte qualquer tecla para continuar ...")
            
            case "5":
                titulo_sistema("Deletar um contato")
                pesquisar_nome = input("digite o nome do contato: ")
                contato_encontrato  = pesquisar_contato_por_nome(pesquisar_nome)
                if(len(contato_encontrato) == 0 ):
                    print("Nem um contato encontrado com esse nome.")
                else:
                    print(f"Contato: ")
                    print(f"Nome: {contato_encontrato['nome']} | Favorito: {contato_encontrato['favorito']}")
                    op = input("deseja Apagar esse contato, (S-sim/N-Não)")
                    if op in 'Ss' or op == "sim" or op == "SIM":
                        contatos.remove(contato_encontrato)
                        print("Contato Apagado com sucesso...")
                        input("aperte qualquer tecla para continuar")
                    else:
                        print("Contato não foi apagado ...")
                        input("aperte qualquer tecla para continuar")
                        continue
                
            case "6":
                titulo_sistema("Editar um contato")
                pesquisar = input("digite o nome do contato: ")
                for contato in contatos:
                    nome_contato = contato['nome'].lower()
                    if(pesquisar.lower() in nome_contato):
                        nome = input("nome <: ")
                        telefone = input("telefone <: ")
                        email = input("e-mail <: ")
                        favorito = input("adicionar aos favoritos (S-sim / N-Não) <: ").lower()
                        e_favorito = verifica_se_e_favorito(favorito)
                        salvar = input("deseja salvar ?  (s-Sim/n-Não): ").lower()
                        if salvar in 'sS' or salvar == "Sim":
                            contato['nome'] = nome
                            contato['telefone'] = telefone
                            contato['email'] = email
                            contato["favorito"] = e_favorito
                        else:
                            continue
            case "0":
                break

if __name__ == "__main__":
    main()