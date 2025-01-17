"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re

def clean_headers(input_directory):
    with(open(input_directory, "r")) as file:
        lines = file.readlines()

    line1 = re.split(r'(?=[A-Z])',lines[0])
    line2 = lines[1].lstrip().rstrip().split()

    line1.pop(0)
    line1[1] += line2[0] + ' ' + line2[1]
    line1[2] += line2[0] + ' ' + line2[1]

    column_names = [re.sub(r"\s+", " ", i.rstrip()) for i in line1]

    column_names = [i.replace(' ', '_').lower() for i in column_names]
        

    return column_names
    
def preprocessing_data():
    with(open('files/input/clusters_report.txt', 'r')) as file:
        lines = file.readlines()
    
    resultados = []
  
    for line in lines[4:]:

        new_line = re.sub(r'\s{5,}', ':', line.strip()).split(':')
        comprobante = re.sub(r'\s{2,}', ':', line.strip()).split(':')
        if comprobante[0].isnumeric():
            if int(comprobante[0]) > 9:
                final_line = comprobante[0:3]
                final_line.append(new_line[2])
                resultados.append(final_line)
            else:  
              resultados.append(new_line)
            
        else:
              if resultados:
                new_line = re.sub(r'\s{5,}', ' ', line.strip())
                resultados[-1][3] += ' ' + new_line
    
    return resultados
    
def cleaning_data(datos, columns_name):
    dataframe = pd.DataFrame(datos, columns=columns_name)

    dataframe['principales_palabras_clave'] = (dataframe['principales_palabras_clave']
                                               .str.replace(r'\s{2,}', ' ', regex=True)
                                               .str.replace('.','').str.rstrip())
    
    dataframe['cluster'] = dataframe['cluster'].astype(int)
    dataframe['cantidad_de_palabras_clave'] = dataframe['cantidad_de_palabras_clave'].astype(int)
    dataframe['porcentaje_de_palabras_clave'] = dataframe['porcentaje_de_palabras_clave'].str.replace('%','').str.replace(',','.').astype(float)

    return dataframe  

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    columns_name = clean_headers('files/input/clusters_report.txt')
    df = preprocessing_data()
    df = cleaning_data(df, columns_name)
    

    return df
print(pregunta_01())