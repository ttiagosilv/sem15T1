def converter_para_celsius(temperatura, escala):
    if escala.upper() == 'C':
        return temperatura
    elif escala.upper() == 'F':
        return (temperatura - 32) * 5.0/9.0
    else:
        raise ValueError("Escala desconhecida. Use 'C' para Celsius ou 'F' para Fahrenheit.")

def converter_para_fahrenheit(temperatura, escala):
    if escala.upper() == 'F':
        return temperatura
    elif escala.upper() == 'C':
        return (temperatura * 9.0/5.0) + 32
    else:
        raise ValueError("Escala desconhecida. Use 'C' para Celsius ou 'F' para Fahrenheit.")

def somar_temperaturas(temp1, temp2):
    temp1_valor, temp1_escala = temp1
    temp2_valor, temp2_escala = temp2

    if temp1_escala.upper() == temp2_escala.upper():
        resultado = temp1_valor + temp2_valor
        resultado_escala = temp1_escala
    else:
        temp1_em_temp2_escala = converter_para_fahrenheit(temp1_valor, temp1_escala) if temp2_escala.upper() == 'F' else converter_para_celsius(temp1_valor, temp1_escala)
        resultado = temp1_em_temp2_escala + temp2_valor
        resultado_escala = temp2_escala
    return round(resultado, 4), resultado_escala

def main():
    temp1_valor = float(input("Digite a primeira temperatura: "))
    temp1_escala = input("Digite a escala da primeira temperatura (C/F): ").upper()[0]

    temp2_valor = float(input("Digite a segunda temperatura: "))
    temp2_escala = input("Digite a escala da segunda temperatura (C/F): ").upper()[0]

    temp1 = (temp1_valor, temp1_escala)
    temp2 = (temp2_valor, temp2_escala)

    resultado = somar_temperaturas(temp1, temp2)
    print(f"A soma das temperaturas é ({resultado[0]}, '{resultado[1]}')")

if __name__ == "__main__":
    main()