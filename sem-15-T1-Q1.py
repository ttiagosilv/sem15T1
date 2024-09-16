def converter_para_celsius(temperatura, escala):
    """Converte uma temperatura para Celsius."""
    if escala.upper() == 'C':
        return temperatura
    elif escala.upper() == 'F':
        return (temperatura - 32) * 5.0/9.0
    else:
        raise ValueError("Escala desconhecida. Use 'C' para Celsius ou 'F' para Fahrenheit.")

def temperatura_maior(temp1, temp2):
    """Compara duas temperaturas e retorna a mais alta."""
    temp1_valor, temp1_escala = temp1
    temp2_valor, temp2_escala = temp2
    
    temp1_em_celsius = converter_para_celsius(temp1_valor, temp1_escala)
    temp2_em_celsius = converter_para_celsius(temp2_valor, temp2_escala)
    
    if temp1_em_celsius > temp2_em_celsius:
        return temp1
    else:
        return temp2

def main():
    temp1_valor = float(input("Digite a primeira temperatura: "))
    temp1_escala = input("Digite a escala da primeira temperatura (C/F): ").upper()[0]

    temp2_valor = float(input("Digite a segunda temperatura: "))
    temp2_escala = input("Digite a escala da segunda temperatura (C/F): ").upper()[0]

    temp1 = (temp1_valor, temp1_escala)
    temp2 = (temp2_valor, temp2_escala)

    maior_temp = temperatura_maior(temp1, temp2)
    print(f"A temperatura maior é ({maior_temp[0]}), '{maior_temp[1]}')")

if __name__ == "__main__":
    main()