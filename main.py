from fkIdGen import generateIds as genIds
from dataAccess import execute as exec
from datetime import datetime
from faker import Faker
import traceback
import random
import re

Faker.seed(42)
fake = Faker()

generateIds = input("Gerar IDs? (s/n): ").lower()

if generateIds == "s":
    IdType = input("Qual o tipo de ID: \n int \n uuid: ").lower()

    IdAmount = int(input("Quantidade de Ids: "))
    genIds(IdType, IdAmount)

try:
    with open('fkidValues.txt', 'r') as file:
        fksValues = dict(line.strip().split(":") for line in file)

    with open('fknames.txt', 'r') as file:
        fksNames = dict(line.strip().split("=") for line in file)
except Exception as err:
    print(f"Verifique se os arquivos: fkidValues.txt e fknames.txt existem. \n Erro ao ler os arquivos: {err}")

try:
    querys = ""
    for key, fkValue in fksNames.items():
        table, fk = key.split(">")

        fk = fk.split(",")
        fkValue = fkValue.split(",")

        columnNames = [col[0] for col in exec(f"describe {table}")]
        columnTypes = [col[1] for col in exec(f"describe {table}")]

        values = []
        for index, value in enumerate(columnNames):
            if value in fk:
                fkValueIndex = fk.index(value)
                values.append(fksValues[fkValue[fkValueIndex]])
            else:
                column_type = columnTypes[index]
                if re.search(r"int", column_type):
                    values.append(fake.random_number(digits=3))
                elif re.search(r"(decimal|float|double)", column_type):
                    values.append(fake.pyfloat(left_digits=3, right_digits=2, positive=True))
                elif re.search(r"(bool|boolean)", column_type):
                    values.append(random.choice([True, False]))
                elif re.search(r"(date|Date)", column_type):
                    values.append(str(datetime.now().date()))
                else:
                    values.append(fake.name())

        formattedValues = [
            f"'{value}'" if isinstance(value, str) else str(value)
            for value in values
        ]

        querys += f"INSERT INTO {table} ({', '.join(columnNames)}) VALUES ({', '.join(formattedValues)})\n"
        
        print(F"Insert criado para a tabela {table} com sucesso.\n FKs columns: {fk} \n FKs chaves: {fkValue}")

    with open('output.sql', 'w') as file:
        file.write(querys)


except Exception as err:
    print(f"Erro ao efetuar a criação dos inserts{err}")
    traceback.print_exc()
    
input("Finalizar...")