import os
import requests as r
import json as j
import pandas as pd
from datetime import datetime

def revision_existencia_api(url):
    try:
        respuesta = r.get(url, timeout=30)
        if respuesta.status_code <= 299:
            print("La API fue Encontrada:", url)
            print("Parte de respuesta")
            print(respuesta.text[:250])
        else:
            print("No fue encontrada:", respuesta.status_code)
    except r.exceptions.ConnetionError:
        print("No se pudo conectar a", url)
    except r.exceptions.ReadTimeout:
        print("Pasaron mas de 30 seg para conectarse a", url)
    except r.exceptions.RequestException as error:
        print("Error de requests al extraer datos de Meteo:", error)
    return respuesta

url = "https://redmeteo.cl/last-data.json"

path_carpeta_salida = "data/raw_data"

respuesta = revision_existencia_api(url)

data = respuesta.json()
dataFrame = pd.DataFrame(data)

# Busque para crear el archivo con la fecha actual, asi se esta seguro de en que fecha quedo
# Uso datetime para escribir parecido al formato del json
fecha_actual = datetime.now().strftime("%Y%m%d_%H%M") # Segun busque esta deberia ser la forma
nombre_arch = f"RedMeteo_last_data_{fecha_actual}.csv"
path_archivo = os.path.join(path_carpeta_salida, nombre_arch)

# Lo guarda en el archivo que se indica path_archivo
dataFrame.to_csv(path_archivo)
print("Se deverian haber guardado los datos en data/ xd ")
