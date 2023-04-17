from scrape import raspagem
import sql
import datetime

def main():
    print('Iniciando raspagem...')
    dados = raspagem()
    print(dados)
    print('Raspagem finalizada!', 'Inserindo dados no banco...', sep='\n')
    for relatorio in dados:
        sql.criarRelatorio(relatorio)
        print()

if __name__ == '__main__':
    main()
    sql.listarColecoes()
    sql.listarRelatoriosDiarios()
