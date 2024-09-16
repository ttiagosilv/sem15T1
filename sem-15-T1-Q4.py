
import csv

def carrega_cidades():
    resultado = []
    try:
        with open('cidades.csv', 'r', encoding='utf-8') as arquivo:
            next(arquivo)
            for linha in arquivo:
                uf, ibge, nome, dia, mes, pop = linha.strip().split(';')
                resultado.append(
                    (uf, int(ibge), nome, int(dia), int(mes), int(pop))
                )
    except FileNotFoundError:
        print("O arquivo 'cidades.csv' não foi encontrado. Verifique o caminho e tente novamente.")
    return resultado

def filtrar_cidades_por_populacao(cidades, populacao_minima):
    return [cidade for cidade in cidades if cidade[5] > populacao_minima]

def main():
    cidades = carrega_cidades()
    try:
        populacao_minima = int(input("Digite a população mínima: "))
        cidades_filtradas = filtrar_cidades_por_populacao(cidades, populacao_minima)
        if cidades_filtradas:
            print(f"CIDADES COM MAIS DE {populacao_minima} HABITANTES:")
            for uf, ibge, nome, dia, mes, populacao in cidades_filtradas:
                print(f"IBGE: {ibge} - {nome}({uf}) - POPULAÇÃO: {populacao}")
        else:
            print(f"Não há cidades com mais de {populacao_minima} habitantes.")

    except ValueError:
        print("Por favor, digite um número válido para a população.")

if __name__ == "__main__":
    main()
