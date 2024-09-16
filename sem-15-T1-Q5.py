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

def cidades_por_criterios(mes, populacao_minima, cidades):
    return [cidade for cidade in cidades if cidade[4] == mes and cidade[5] > populacao_minima]

def main():
    caminho_csv = 'cidades.csv'
    cidades = carrega_cidades(caminho_csv)
    
    try:
        mes = int(input("Digite o mês (1-12): "))
        populacao_minima = int(input("Digite a população mínima: "))
        
        if not (1 <= mes <= 12):
            print("Mês inválido. O mês deve estar entre 1 e 12.")
            return
        
        cidades_filtradas = cidades_por_criterios(mes, populacao_minima, cidades)
        
        if cidades_filtradas:
            mes_nome = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'][mes-1]
            print(f"CIDADES COM MAIS DE {populacao_minima} HABITANTES E ANIVERSÁRIO EM {mes_nome.upper()}:")
            for uf, ibge, nome, dia, _, populacao in cidades_filtradas:
                print(f"{nome}({uf}) tem {populacao} habitantes e faz aniversário em {dia} de {mes_nome.lower()}.")
        else:
            mes_nome = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'][mes-1]
            print(f"Não há cidades com mais de {populacao_minima} habitantes que fazem aniversário em {mes_nome.upper()}.")
    
    except ValueError:
        print("Por favor, digite números válidos para o mês e a população.")

if __name__ == "__main__":
    main()
