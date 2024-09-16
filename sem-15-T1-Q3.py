import csv

def carrega_cidades(caminho_csv):
    cidades = []
    try:
        with open(caminho_csv, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo, delimiter=';')
            next(leitor) 
            for linha in leitor:
                uf, ibge, nome, dia, mes, populacao = linha
                cidades.append((uf, int(ibge), nome, int(dia), int(mes), int(populacao)))
    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_csv}' não foi encontrado.")
    return cidades

def cidades_aniversario(dia, mes, cidades):
    return [cidade for cidade in cidades if cidade[3] == dia and cidade[4] == mes]

def main():
    caminho_csv = 'cidades.csv'
    cidades = carrega_cidades(caminho_csv)
    
    try:
        dia = int(input("Digite o dia (1-31): "))
        mes = int(input("Digite o mês (1-12): "))
        
        if not (1 <= dia <= 31) or not (1 <= mes <= 12):
            print("Dia ou mês inválido. O dia deve estar entre 1 e 31, e o mês entre 1 e 12.")
            return
        
        cidades_filtradas = cidades_aniversario(dia, mes, cidades)
        
        if cidades_filtradas:
            mes_nome = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'][mes-1]
            print(f"CIDADES QUE FAZEM ANIVERSÁRIO EM {dia} DE {mes_nome.upper()}:")
            for uf, ibge, nome, _, _, _ in cidades_filtradas:
                print(f"{nome}({uf})")
        else:
            mes_nome = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'][mes-1]
            print(f"Não há cidades que fazem aniversário em {dia} de {mes_nome.upper()}.")
    
    except ValueError:
        print("Por favor, digite números válidos para o dia e o mês.")

if __name__ == "__main__":
    main()
