import requests as rq
import jsonpath_ng.ext as jp
import pandas as pd
from lxml import etree
import time 
import json

URL_ESearch = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
URL_ESummary = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
URL_EFetch = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

class API_NCBI:
    """
        Clase para realizar instancias de las peticiones a la API REST de NCBI / E-utils: E-Search, E-summary, E-fetch.
    """
    def __init__(self, consulta = None, codigoAcceso = None, parametros = None):
        self.consulta = consulta #  Si realiza la consulta por terminos
        self.codigoAcceso = codigoAcceso # Si realiza la consulta por el ID Access.
        self.parametros = parametros
        self.modo = None
        self.respuesta = None
        
    def definir_parametros_ESearch(bbdd, consulta, modo, maximoRespuesta):
        
        self.parametros = parametros
        return parametros
    
    def definir_parametros(bbdd, id, modo, maximoRespuesta, tipo):
        match tipo:
            case "EFetch":
                parametros = {
                    "db": bbdd,
                    "id": id,
                    "retmode": modo,
                    "retmax": maximoRespuesta
                }
            case "ESearch":
                parametros = {
                    "db": bbdd,
                    "term": consulta,
                    "retmode": modo,
                    "retmax": maximoRespuesta
                }        
        self.parametros = parametros
        return parametros
    
    def realizar_busqueda(url, timeout=30):
        try:
            respuesta = rq.get(url = url, params = self.parametros, timeout = timeout)
            if response.status_code == 200:
                print("La consulta fue existosa")                   
        except Exception:
            print(f"Error en la consulta: {response.status_code}")
        
        if (self.modo == "json"):
            datos = respuesta.json()
        elif (self.modo == "xml"):
            datos = respuesta.etree()
        elif (self.modo == "text"):
            datos = respuesta.text
        
        self.respuesta = datos
        return datos
        
    
    def buscar_gen(consulta, modo, maximoRespuesta):
        """
            Función para buscar un gen en la BBDD Nuccore de NCBI por su ID.
            Realiza una petición a Nuccore con E-search.
        """
        
        self.modo = modo
        self.definir_parametros("nuccore", consulta, modo, maximoRespuesta, "ESearch")
        self.realizar_busqueda(URL_ESearch)
        
    def buscar_proteina(consulta, modo, maximoRespuesta):
        """
            Función para buscar un gen en la BBDD Nuccore de NCBI por su ID.
            Realiza una petición a Protein con E-search.
        """
        
        self.modo = modo
        self.definir_parametros("protein", consulta, modo, maximoRespuesta, "ESearch")
        self.realizar_busqueda_ESearch(URL_ESearch)        
        