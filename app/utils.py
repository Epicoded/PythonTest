import re


def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values

def get_pop(country_dict):
  dic={}
  for k in country_dict:
    #Buscar  las llaves con el nombre 'Population'
    key = re.findall('Population',k)
    if key != []:
      #Guardar las llaves y valores que coincidan con 'Population'
      values = country_dict[k]
      #Extraer el año correspondiente a la población
      keys = re.findall('[0-9]+',k)
      if keys != []:
        #Guardar como strings y enterlos los valores en el diccionario
        dic[keys[0]] = int(values)
  k = dic.keys()
  v = dic.values()
  return k,v
      
    

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result