import re

# Definindo a expressão regular para formato nacional padrão
formato_nacional = r'^[A-Za-zÀ-ÿ]+(?:[\s\.][A-Za-zÀ-ÿ]+)*,?\s*\d+$'

# # Exemplos de teste
enderecos = [
    "Milton 74",
    "Rua Vasconcellos 54",
    "Rua Ferraz de Vasconcelos Moreira 98",
    "Avenida Brasil 1234",
    "Calle de la Paz 56",
    "Travessa da Luz, 88",
    "Rua das Flores, 12",
    "74, Milton",
    "Rua Milton"
]

for endereco in enderecos:
    if re.match(formato_nacional, endereco):
        print(f"{endereco} -> Corresponde")
    else:
        print(f"{endereco} -> Não corresponde")

# Padrão brasileiro ex: Rua Saraiva 8... com possível espaço e letra após o número
## Formato para corresponde apenas para casos que possuam o número com letras
formato_nacional_letra = r"^[A-Za-zÀ-ÿ]+(?:[\s\.][A-Za-zÀ-ÿ]+)*,?\s*\d+\s*[A-Za-zÀ-ÿ]*\s*([A-Za-zÀ-ÿ]+\s*)*$"


enderecos2 = [
    "Milton 74",
    "Rua Vasconcellos 54",
    "Rua Ferraz de Vasconcelos Moreira 98",
    "Avenida Brasil 1234",
    "Calle de la Paz 56",
    "Travessa da Luz, 88",
    "Rua das Flores, 12",
    "74, Milton",
    "Rua Milton",
    "Rua Moreira de Barros 123 B",
    "Rua moreira de barros 12B",
    "Rua Moreira de BArros 12 b c d"
]

for endereco in enderecos2:
    if re.match(formato_nacional_letra, endereco):
        print(f"{endereco} -> Corresponde")
    else:
        print(f"{endereco} -> Não corresponde")


formato_internacional1 = r"^[0-9]+,?\s*(?:[\s\.'-][A-Za-zÀ-ÿ]+)+$"


endercosInt = {
"12, Avenue des Champs-Élysées",
"45, Boulevard Saint-Germain",
"78, Rue de la Paix",
"22, Rue de l'Université",
"33, Rue de la République",
"89, Rue du Faubourg Saint-Antoine",
"15, Place de la Bastille",
"67, Rue de Rivoli",
"100, Boulevard Montmartre",
"25, Rue des Rosiers",
"90, Avenue Victor Hugo",
"10, Rue du Bac",
"56, Rue des Martyrs",
"7, Place de la Concorde",
"36, Avenue de l'Opéra",
"52, Rue de la Sorbonne",
"14, Rue de la Mairie",
"88, Rue de la Liberté",
"40, Avenue de la Gare",
"5, Rue des Archives"
}


for ende in endercosInt:
    if re.match(formato_internacional1,ende):
        print(f"{ende} -> Corresponde")
    else:
        print(f"{ende} -> Não Corresponde")

formato_internacional2 = r"^[A-Za-zÀ-ÿ\s\.'-]+\s+\d+\s+[A-Za-zÀ-ÿ\s\.'-]+\s+\d+$"

enderecosInt2 = {
    "Calle 44 No 1991",
    "Calle 12 A 34",
    "Avenida 5 Norte 88",
    "Calle de los Olmos 42",
    "Avenida Central 1500",
    "Calle 7 B 99",
    "Calle 8 Este 204",
    "Calle 9 Sur 33",
    "Avenida 20 de Noviembre 256",
    "Calle 25 No 68",
    "Calle 10 Norte 200",
    "Calle 6 Oriente 15",
    "Avenida Libertad 999",
    "Calle 11 Sur 5",
    "Calle 3 A 123",
    "Avenida 2 de Abril 37",
    "Calle 4 Este 7",
    "Calle 5 Norte 16",
    "Calle 15 No 22",
    "Calle 14 A 88"
}

for address in enderecosInt2:

    if re.match(formato_internacional2,address):
        print(f"{address} -> Corresponde")
    else:
        print(f"{address} -> Não Corresponde")