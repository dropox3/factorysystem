import xml.etree.ElementTree as ET
import os
from datetime import datetime

# Função para criar um novo pedido de produção
def criar_ordem_producao():
    try:
        produto = str(input("Nome do produto: "))
        quantidade = int(input("Quantidade desejada: "))
        data_entrega = input("Data de entrega (YYYY-MM-DD): ")

        # Validar a data de entrega
        datetime.strptime(data_entrega, '%Y-%m-%d')

        ordem = ET.Element("ordem")
        ET.SubElement(ordem, "produto").text = produto
        ET.SubElement(ordem, "quantidade").text = str(quantidade)
        ET.SubElement(ordem, "data_entrega").text = data_entrega

        ordens_producao.append(ordem)
        tree.write("ordens_producao.xml")
        print("Ordem de produção criada com sucesso.")
    except ValueError:
        print("Erro: Quantidade inválida. Certifique-se de inserir um número inteiro.")
    except (ValueError, ValueError):
        print("Erro: Data de entrega inválida. Certifique-se de inserir a data no formato YYYY-MM-DD.")

# Função para listar todas as ordens de produção existentes
def listar_ordens_producao():
    if not ordens_producao:
        print("Nenhuma ordem de produção encontrada.")
    else:
        for i, ordem in enumerate(ordens_producao, 1):
            print(f"Ordem {i}:")
            print("Produto:", ordem.find("produto").text)
            print("Quantidade:", ordem.find("quantidade").text)
            print("Data de Entrega:", ordem.find("data_entrega").text)
            status = ordem.get("status", "Não Concluída")
            print("Status:", status)
            print()

# Função para verificar se a produção é possível com base nos materiais disponíveis
def verificar_disponibilidade_materiais():
    # Implemente a lógica de verificação aqui
    pass

# Função para atualizar o status de uma ordem de produção
def atualizar_status():
    listar_ordens_producao()
    if not ordens_producao:
        print("Nenhuma ordem de produção encontrada para atualizar o status.")
        return

    try:
        index = int(input("Selecione o número da ordem de produção a ser atualizada: ")) - 1
        status = input("Status (Concluída/Não Concluída): ").lower()

        if status not in ["concluída", "não concluída"]:
            print("Erro: Status inválido. Use 'concluída' ou 'não concluída'.")
            return

        ordens_producao[index].set("status", status)
        tree.write("ordens_producao.xml")
        print("Status atualizado com sucesso.")
    except (ValueError, IndexError):
        print("Erro: Número de ordem inválido.")

# Função para visualizar relatórios de produção
def visualizar_relatorios():
    listar_ordens_producao()

# Verificar se o arquivo XML existe, senão, criar um novo
if not os.path.exists("ordens_producao.xml"):
    root = ET.Element("ordens_producao")
    tree = ET.ElementTree(root)
    tree.write("ordens_producao.xml")
else:
    tree = ET.parse("ordens_producao.xml")
    root = tree.getroot()

ordens_producao = root.findall("ordem")

while True:
    print("Escolha uma opção:")
    print("1. Registrar uma nova ordem de produção")
    print("2. Listar todas as ordens de produção")
    print("3. Verificar disponibilidade de materiais")
    print("4. Atualizar o status de uma ordem de produção")
    print("5. Visualizar relatórios de produção")
    print("6. Sair")
    
    opcao = input("Opção: ")
    
    if opcao == "1":
        criar_ordem_producao()
    elif opcao == "2":
        listar_ordens_producao()
    elif opcao == "3":
        verificar_disponibilidade_materiais()
    elif opcao == "4":
        atualizar_status()
    elif opcao == "5":
        visualizar_relatorios()
    elif opcao == "6":
        break
    else:
        print("Opção inválida. Tente novamente.")
