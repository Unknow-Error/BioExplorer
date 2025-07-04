import requests as rq
import jsonpath_ng.ext as jp
import pandas as pd
from lxml import etree
import time 
import json

URL_UniprotKB = "https://rest.uniprot.org/uniprotkb/search"

class API_Uniprot:
    """
        Cliente para la REST API moderna de UniProt u otras como UniRef.
        Devuelve resultados en formato TSV como pandas.DataFrame.
    """
    
    def __init__(self, parametros, base_url, timeout=30, cursor=None):
        self.parametros = parametros
        self.base_url = base_url
        self.timeout = timeout
    
    def _conseguir_pagina(self, url, parametros):
        """
            Realiza la petición HTTP a UniProt  y retorna el DataFrame de la página y el link next (o None).
        """
        #Peticion:
        respuesta = requests.get(url, params=parametros, timeout=self.timeout)
        respuesta.raise_for_status()
        
        #Leer TSV:
        df = pd.read_csv(StringIO(response.content.decode("utf-8")), sep="\t", header=0)
        
        # Extraer enlace "siguiente" de encabezado Link
        siguiente_link = None
        link_header = response.headers.get("Link", "")
        # Updated regex pattern to extract the URL with the scheme
        pattern = re.compile(r'<([^>]+)>;\s*rel="next"')
        match = pattern.search(link_header)
        if match:
            siguiente_link = match.group(1)

        return df, siguiente_link

    def data_de_paginacion_tsv(self, delay):
        '''
            Similar a response_data pero paginable, utilizando la funcion anterior.
            Retorna un DataFrame con los datos obtenidos en batch de la paginacion.
            Requiere que en parametros se solicite los datos en .tsv
        '''
        # Preparar primera petición
        url_actual = self.base_url
        parametros = self.parametros.copy()

        paginas = []  # Para guardar de cada pagina

        while True:
            time.sleep(delay)
            df, siguiente_link = self._conseguir_pagina(url_actual, parametros)
            
            if df.empty:
                break
            paginas.append(df) # Guardar la página
            
            if siguiente_link is None:
                break
            # Preparar siguiente iteración: usar URL completa en next_link
            url_actual  = siguiente_link
            # Vaciar params para que requests use URL tal cual
            parametros = None

        # Concatenamos todo en un solo DataFrame (si hubo al menos una página)
        return pd.concat(paginas, ignore_index=True) if paginas else pd.DataFrame()
