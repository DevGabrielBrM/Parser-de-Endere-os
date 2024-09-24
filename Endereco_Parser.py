#Utilizando-se de Regex criei 4 possíveis formatos que poderemos receber como input...
import re

# Checando os formatos,formatando e imprimindo
def formatadora(endereco):
    try:
        formato_nacional = r'^[A-Za-zÀ-ÿ]+(?:[\s\.][A-Za-zÀ-ÿ]+)*\s*,?\s*\d+\s*$'
        formato_nacional_letra = r"^[A-Za-zÀ-ÿ]+(?:[\s\.][A-Za-zÀ-ÿ]+)*,?\s*\d+\s*[A-Za-zÀ-ÿ]*\s*([A-Za-zÀ-ÿ]+\s*)*$"
        formato_internacional1 = r"^[0-9]+,?\s*(?:[\s\.'-][A-Za-zÀ-ÿ]+)+$"
        formato_internacional2 = r"^([A-Za-zÀ-ÿ\s\.'-]+\s+\d+)\s*,?\s+((No|no|NO|N°|Nº|Núm\.|nr|número|numero)\s+\d+)$"
        match =  re.match(formato_internacional2,endereco)
        
        if re.match(formato_nacional,endereco):

            # Criando listas e Dividindo a string completa em substrings, espaço como default de divisão, resulta em string completas, não char
            endereco_split = endereco.split()
            nome = []
            numero = []
            
            # Iterando sobre endereco_split e checando se é um digito ou não, dependendo da filtragem adiciona a uma das duas listas
            for str in endereco_split:
                if str.isdigit():
                    numero.append(str)
                else:
                    nome.append(str)
            
            
            nome = " ".join(nome).strip(",")
            numero = "".join(numero).strip(",")

            return {'Rua': nome, 'Número': numero}

        elif re.match(formato_nacional_letra,endereco):

            endereco_split = endereco.split()
            nome = []
            numero = []
            letra = []
            final = endereco_split[-1]

            if not final.isdigit():
                letra.append(final)
            else:
                numero.append(final)
            
            for str in endereco_split[:-1]:
                if not str.isdigit():
                    nome.append(str)
                elif str.isdigit():
                    numero.append(str)
            
            nome = " ".join(nome).strip(',')

            if letra != []:
                for char in letra:
                    numero.append(char)
                numero = " ".join(numero)

            return {'Rua': nome, 'Número': numero}  

        elif re.match(formato_internacional1,endereco):

            endereco_split = endereco.split()
            nome = []
            numero = []
            
            # Iterando sobre endereco_split e checando se é um digito ou não, dependendo da filtragem adiciona a uma das duas listas
            for str in endereco_split:
                if re.match(r"\d+\s*,?",str):
                    numero.append(str)
                else:
                    nome.append(str)
            
            #Formatando...
            nome = " ".join(nome)
            numero = "".join(numero).strip(',')
            
            return {'Rua': nome, 'Número': numero}

        
        elif match:
            nome = match.group(1)
            numero = match.group(2)

            return {'Rua': nome, 'Número': numero}
        
        else:

            return "\n!!! Formato Errado !!!\nSerá redirecionado para o menu"
    
    except Exception as e:
        return f"Erro ao processar p endereço: {e}"


if __name__ == "__main__":
    task = 5
    while task != 0:

        endereco = input("Digite seu endreço: ")
        resultado = formatadora(endereco)
        print(resultado)

        print("\nDigite Qualquer número para continuar...\nOu Digite 0 para SAIR!\n")
        task = int(input("Sua escolha ->"))

