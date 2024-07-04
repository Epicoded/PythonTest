import csv


def read_csv(path):
  with open(path, 'r') as csvfile: # abre el archivo
    reader = csv.reader(csvfile, delimiter=',') #lector del archivo csv
    header = next(reader) # lee la primera linea del archivo csv

    data = [] # lista vacia
    for row in reader: # recorre las lineas del archivo csv
      iterable = zip(header, row) # une los encabezados con las filas

      #country_dict = {key: value for key, value in iterable} # convierte en diccionario
      country_dict = dict(iterable)# convierte en diccionario
      
      data.append(country_dict) # agrega el diccionario a la lista
    return data # retorna la lista

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0]) 