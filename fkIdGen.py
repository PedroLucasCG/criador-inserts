from uuid_extensions import uuid7
import random

def generateIds(idType, idAmount):
    print(idType, idAmount)
    if (idType == "uuid"):
        with open('fkidValues.txt', 'w') as file:
            for index in range(1, idAmount+1):
                file.write(f"fk{index}:{uuid7()}\n")
    else:
        with open('fkidValues.txt', 'w') as file:
            for index in range(1, idAmount+1):
                file.write(f"fk{index}:{random.randrange(1, 200)}\n")