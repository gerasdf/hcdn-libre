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
    "strCantPagina":"10",
}

FILE = "file:home/gera/src/hdcn/all.html"

def build_url(base, parameters):
    answer = base + "?"
    for name, value in parameters.items():
        answer += '{}={}&'.format(name, value)

    return answer

SEARCH_BASE = FILE #build_url(URL_BASE, ARGS_BASE)

class Proyecto(scrapy.Item):
    titulo = scrapy.Field()
    expediente_diputados = scrapy.Field()
    expediente_senado = scrapy.Field()
    iniciado_en = scrapy.Field()
    publicado_en = scrapy.Field()
    fecha = scrapy.Field()
    ley = scrapy.Field()

class HCDN(scrapy.Spider):
    name = "hcdn"

    def start_requests(self):
        yield scrapy.Request(url=SEARCH_BASE, callback=self.parse)

    def parse(self, response):
        in_this_page = response.css('div.detalle-proyecto')
        for proyecto in in_this_page:
            item = Proyecto()

            item['titulo'] = proyecto.css('div.dp-texto::text').extract_first()

            metadata = proyecto.css('div.dp-metadata')
            names  = metadata.css('strong::text').extract()
            values = metadata.css('span::text').extract()

            for name, value in zip(names, values):
                good_name = name[:-2].replace(' ','_').lower()
                item[good_name] = value

            if names[-1].lower().startswith('ley '):
               ley = names[-1].split(' ')[1]
               item['ley'] = ley

            yield item

        next_page = response.css('ul.pagination').css('a[aria-label="Siguiente"]::attr(href)').extract_first()
        if next_page is not None:
           if '2' in next_page:
               yield response.follow(next_page, callback=self.parse)
