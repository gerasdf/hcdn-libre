# -*- coding: utf-8 -*-
import unicodedata
import scrapy

URL_BASE  = "https://www.hcdn.gob.ar/proyectos/resultados-buscador.html"
ARGS_BASE = {
    "strTipo":"ley", 
    #"strNumExp",
    #"strNumExpOrig",
    #"strNumExpAnio",
    #"strCamIni",
    #"strFirmante",
    #"strComision",
    #"strFechaInicio":"01/01/2018",
    #"strFechaFin",:"31/07/2018"
    #"strPalabras",
    #"strOrdenDelDiaNro",
    #"strOrdenDelDiaAnio",
    #"strLey",
    "strAprobadoDiputados":"on",
    "strMostrarTramites":"on",
    "strMostrarDictamenes":"on",
    "strMostrarFirmantes":"on",
    "strMostrarComisiones":"on",
    "strCantPagina":"50",
}

FILE = "file:home/gera/src/hdcn/all.html"

def build_url(base, parameters):
    answer = base + "?"
    for name, value in parameters.items():
        answer += '{}={}&'.format(name, value)

    return answer

BASE_URL = build_url(URL_BASE, ARGS_BASE)
# BASE_URL = FILE 

class Proyecto(scrapy.Item):
    titulo = scrapy.Field()
    expediente_diputados = scrapy.Field()
    expediente_senado = scrapy.Field()
    iniciado_en = scrapy.Field()
    publicado_en = scrapy.Field()
    fecha = scrapy.Field()
    ley = scrapy.Field()
    firmantes = scrapy.Field()
    comisiones = scrapy.Field()
    dictamenes = scrapy.Field()
    en_diputados = scrapy.Field()
    en_senado = scrapy.Field()
    tramites = scrapy.Field()

class Firmante(scrapy.Item):
    orden = scrapy.Field()
    firmante = scrapy.Field()
    distrito = scrapy.Field()
    bloque = scrapy.Field()

class Comision(scrapy.Item):
    orden = scrapy.Field()
    comision = scrapy.Field()
    
class Tramite(scrapy.Item):
    orden = scrapy.Field()
    camara = scrapy.Field()
    movimiento = scrapy.Field()
    resultado = scrapy.Field()
    fecha = scrapy.Field()

class Dictamen(scrapy.Item):
    orden = scrapy.Field()
    camara = scrapy.Field()
    dictamen = scrapy.Field()
    texto = scrapy.Field()
    fecha = scrapy.Field()

def noTildes(string):
    return unicodedata.normalize('NFKD',string).encode('ascii','ignore').decode()

class HCDN(scrapy.Spider):
    name = "hcdn"

    def start_requests(self):
        yield scrapy.Request(url=BASE_URL, callback=self.parse)

    def parse_metadata(self, proyecto, item):
        metadata = proyecto.css('div.dp-metadata')
        names  = metadata.css('strong::text').extract()
        values = metadata.css('span::text').extract()

        for name, value in zip(names, values):
            good_name = name[:-2].replace(' ','_').lower()
            item[good_name] = value

        if names[-1].lower().startswith('ley '):
           ley = names[-1].split(' ')[1]
           item['ley'] = ley

    def parse_box(self, box, Item):
        answer = []
        columnas = box.css('tr').css('th::text').extract()
        columnas = [noTildes(columna.lower()) for columna in columnas]
        orden = 1
        for linea in box.css('tr'):
            firmante = linea.css('td::text').extract()
            if firmante:
               firmante = Item(dict(zip(columnas, firmante)))
               firmante['orden'] = orden
               answer.append(firmante)
               orden += 1
        return answer
        
    def parse_firmante(self, proyecto, item, box):
        item['firmantes'] = self.parse_box(box, Firmante)

    def parse_comisiones(self, proyecto, item, box, titulo):
        item[titulo] = self.parse_box(box, Comision)

    def parse_tramite(self, proyecto, item, box):
        item['tramites'] = self.parse_box(box, Tramite)

    def parse_dictamenes(self, proyecto, item, box):
        item['dictamenes'] = self.parse_box(box, Dictamen)

    def parse(self, response):
        in_this_page = response.css('div.detalle-proyecto')
        for proyecto in in_this_page:
            item = Proyecto()

            item['titulo'] = proyecto.css('div.dp-texto::text').extract_first()

            self.parse_metadata(proyecto, item)

            for box in proyecto.css('div.dp-box'):
                title = box.css('h5::text').extract_first()
                title = noTildes(title)
                if   title == "FIRMANTES":
                   self.parse_firmante(proyecto, item, box)
                elif title == "GIRO A COMISIONES EN DIPUTADOS":
                   self.parse_comisiones(proyecto, item, box, "en_diputados")
                elif title == "GIRO A COMISIONES EN SENADO":
                   self.parse_comisiones(proyecto, item, box, "en_senado")
                elif title == "TRAMITE":
                   self.parse_tramite(proyecto, item, box)
                elif title == "DICTAMENES DE COMISION":
                   self.parse_dictamenes(proyecto, item, box)
                else:
                   print("************* <- Unknown section") # ({})".format(title))

            yield item

        next_page = response.css('ul.pagination').css('a[aria-label="Siguiente"]::attr(href)').extract_first()
        if next_page is not None:
           #if '2' in next_page: 
               if next_page[0] == '?':
                  next_page = "{}&{}".format(BASE_URL,next_page[1:])
                  yield scrapy.Request(next_page, callback=self.parse)
