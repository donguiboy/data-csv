import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, skipinitialspace= True)
    #archivo     importado. Lee como diccionari (open('data/phone_book.csv', mode='r'), skipintialspace=)
    #next(csv_reader) #esto nos ayuda a skippear la primer fila(row) solo con listas

    for row in csv_reader:
        print(f'{row["first_name"]}: {row["phone_number"]}')
        line_count += 1
