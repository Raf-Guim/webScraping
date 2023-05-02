from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from dados import string_conexao

import datetime

engine = create_engine(string_conexao)


def criarColecao(nome):

    with Session(engine) as sessao, sessao.begin():
        report = {
            'nome': nome
        }
        sessao.execute(text("INSERT INTO colecao (nome) VALUES (:nome)"), report)

def obterColecao(nome):
    with Session(engine) as sessao:
        parametros = {
            'nome': nome
        }
        colecao = sessao.execute(text("SELECT id, nome FROM colecao WHERE nome = :nome"), parametros).first()

        # if colecao == None:
        #     print('Coleção não encontrada!')
        
        return colecao

def listarColecoes():
    
    with Session(engine) as sessao:
        colecoes = sessao.execute(text("SELECT id, nome FROM colecao ORDER BY id"))
        for colecao in colecoes:
            print(f'\nid: {colecao.id} / nome: {colecao.nome}')
        print('- - - - - - - - - -')

def criarRelatorio(relatorio):
    #Para impedir que mais de um relatório seja criado para o mesmo dia
    hoje = datetime.datetime.now().strftime('%Y-%m-%d')

    with Session(engine) as sessao, sessao.begin():
        reports = sessao.execute(text("SELECT * FROM relatorioDiario"))
    for item in reports:

        #item[9] = data relatório já existente
        #item[2] = nome da coleção do relatório já existente
        #relatorio[1] = nome da coleção do relatório a ser criado
        if (str(item[9]) == hoje and item[2] == relatorio[1]):
            print(f'Já existe um relatório {relatorio[1]} para hoje ({hoje})!')
            return
        
    #Lógica para criar a coleção caso seja necessário
    #relatorio[1] = nome da coleção
    validaExistencia = obterColecao(relatorio[1])
    if (validaExistencia == None):
        criarColecao(relatorio[1])
        validaExistencia = obterColecao(relatorio[1])


    #Lógica para criar o relatório

    report = {
            'posicao': int(relatorio[0]),
            'colecao_nome': relatorio[1],
            'volume': int(relatorio[2].replace(',', '').replace('K', '000').replace(' ', '').replace('ETH','').replace('BNB','')),
            'variacao': float(relatorio[3].replace(',', '').replace('%', '')),
            'preco': float(relatorio[4].replace(',', '').replace('K','000').replace(' ', '').replace(';','').replace('&lt','').replace('USDC','').replace('ETH','').replace('MATIC','').replace('BNB','').replace('—', '0')),
            'vendas': int(relatorio[5].replace(',', '').replace('K','000').replace(' ','')),
            'donosUnicos': int(relatorio[6].replace('%','')),
            'listagem': float(relatorio[7].replace('%', '')),
            'data': relatorio[8]
        }    
    with Session(engine) as sessao, sessao.begin():
        sessao.execute(text(f"INSERT INTO relatorioDiario (colecao_id, posicao, colecao_nome, volume, variacao, preco, vendas, donosUnicos, listagem, dia) VALUES ({validaExistencia[0]}, :posicao, :colecao_nome, :volume, :variacao, :preco, :vendas, :donosUnicos, :listagem, :data)"), report)
    print(f'Relatório {relatorio[1]} criado com sucesso para o dia {hoje}!')

def listarRelatoriosDiarios():
    
    with Session(engine) as sessao:
        reports = sessao.execute(text("SELECT * FROM relatorioDiario INNER JOIN colecao ON relatorioDiario.colecao_id = colecao.id ORDER BY dia DESC"))
        for report in reports:
            print(f'colecao_id: {report[10]} / posicao: {report[1]} / nome: {report[2]} / volume: {report[3]} / variacao: {report[4]} / preco: {report[5]} / vendas: {report[6]} / donosUnicos: {report[7]} / listagem: {report[8]} / data: {report[9]}')
        print('- - - - - - - - - -')
        



# if __name__ == '__main__':
#     # relatorio = ['8', 'Hey Jude', '435 ETH', '+182%', '9.50 ETH', '47', '61%', '6%']
#     # criarRelatorio(relatorio)
    # listarRelatoriosDiarios()
#     listarColecoes()