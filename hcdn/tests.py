# -*- coding: latin-1 -*-
import unittest
import hcdn_spider
from scrapy.http.response.html import HtmlResponse

html_one = """
   <div class="proyectos-encontrados">
       <div class="detalle-proyecto">
             
             <h4>PROYECTO DE LEY</h4>
             <div class="dp-metadata">
                <span><strong>Iniciado en: </strong>Diputados</span>
                <span><strong>Expediente Diputados: </strong>2919-D-2018</span>
                <br>
                
                <span><strong>Publicado en: </strong>Trámite Parlamentario N° 48</span>
                <span><strong>Fecha: </strong>15/05/2018</span>
                <br>
                
                </div>
             <div class="dp-texto">VINCULO JURIDICO ENTRE LA CRUZ ROJA ARGENTINA Y EL ESTADO NACIONAL. REGULACION.</div>
             
             <div class="dp-box">
                   <h5>FIRMANTES</h5>
                   <table class="dp-firmantes table table-condensed table-striped">
                      <thead>
                         <tr>
                            <th>FIRMANTE</th>
                            <th>DISTRITO</th>
                            <th>BLOQUE</th>
                         </tr>
                      </thead>
                      <tbody>
                      
                         <tr>
                            <td>LAVAGNA, MARCO</td>
                            <td>CIUDAD de BUENOS AIRES</td>
                            <td>FEDERAL UNIDOS POR UNA NUEVA ARGENTINA</td>
                         </tr>
                         <tr>
                            <td>MASSOT, NICOLAS MARIA</td>
                            <td>CORDOBA</td>
                            <td>PRO</td>
                         </tr>
                         <tr>
                            <td>CAMAÑO, GRACIELA</td>
                            <td>BUENOS AIRES</td>
                            <td>FEDERAL UNIDOS POR UNA NUEVA ARGENTINA</td>
                         </tr>
                         <tr>
                            <td>NEGRI, MARIO RAUL</td>
                            <td>CORDOBA</td>
                            <td>UCR</td>
                         </tr>
                         <tr>
                            <td>KOSINER, PABLO FRANCISCO JUAN</td>
                            <td>SALTA</td>
                            <td>JUSTICIALISTA</td>
                         </tr>
                         </tbody>
                   </table>
                </div>
                <div class="dp-box">
                   <h5>GIRO A COMISIONES EN DIPUTADOS</h5>
                   <table class="dp-giros-diputados table table-condensed table-striped">
                      <thead>
                         <tr>
                            <th>COMISIÓN</th>
                         </tr>
                      </thead>
                      <tbody>
                         <tr>
                            <td>ASUNTOS COOPERATIVOS, MUTUALES Y DE ORG.NO GUBERNAMENTALES</td>
                            
                         </tr>
                         <tr>
                            <td>ACCION SOCIAL Y SALUD PUBLICA</td>
                            
                         </tr>
                         <tr>
                            <td>PRESUPUESTO Y HACIENDA</td>
                            
                         </tr>
                         </tbody>
                   </table>
                </div>
                <div class="dp-box">
                   <h5>TRÁMITE</h5>
                   <table class="dp-tramites table table-condensed table-striped">
                  <thead>
                     <tr>
                        <th>CÁMARA</th>
                        <th>MOVIMIENTO</th>
                        <th>FECHA</th>
                        <th>RESULTADO</th>
                     </tr>
                  </thead>
                  <tbody>
                     <tr>
                        <td>Diputados</td>
                        <td>CITACION SESION ESPECIAL</td>
                        <td>04/07/2018</td>
                        <td> </td>
                     </tr>
                     <tr>
                        <td>Diputados</td>
                        <td>MOCION CAMARA EN COMISION, CONFERENCIA</td>
                        <td>04/07/2018</td>
                        <td> </td>
                     </tr>
                     <tr>
                        <td>Diputados</td>
                        <td>CONSIDERACION Y APROBACION</td>
                        <td>04/07/2018</td>
                        <td>MEDIA SANCION</td>
                     </tr>
                     <tr>
                        <td>Senado</td>
                        <td>PASA A SENADO -</td>
                        <td></td>
                        <td> </td>
                     </tr>
                     </tbody>
                   </table>
                </div>
                <div class="text-center" style="margin-bottom:20px;">
            <button type="button" class="btn btn-info" data-toggle="collapse" data-target="#sumario215059">Sumario</button>
            <a target="_blank" class="btn btn-info" href="https://www.hcdn.gob.ar/proyectos/textoCompleto.jsp?exp=2919-D-2018&tipo=LEY">Texto completo del proyecto</a>
            
            </div>
         
         <div id="sumario215059" class="collapse well" style="margin:0;">
               DISPOSICIONES PRELIMINARES; OBJETO; COLABORACION CON LAS AUTORIDADES DEL ESTADO NACIONAL; AUTORIZACION; VOLUNTARIADO EN LA CRUZ ROJA; ACTIVIDADES; COOPERACION CON EL ESTADO NACIONAL Y BIENES DE LA CRUZ ROJA; BENEFICIOS; EXENCIONES IMPOSITIVAS; DISPOSICIONES FINALES; MODIFICACION DEL ARTICULO 7 DE LA LEY 27287 (SISTEMA NACIONAL PARA LA GESTION INTEGRAL DEL RIESGO Y LA PROTECCION CIVIL) E INCORPORACION AL ANEXO UNICO EL SIGUIENTE TEXTO: "CRUZ ROJA ARGENTINA". </div>
         </div>
       <div class="detalle-proyecto">
             
             <h4>PROYECTO DE LEY</h4>
             <div class="dp-metadata">
                <span><strong>Iniciado en: </strong>Diputados</span>
                <span><strong>Expediente Diputados: </strong>2648-D-2018</span>
                <br>
                
                <span><strong>Publicado en: </strong>Trámite Parlamentario N° 42</span>
                <span><strong>Fecha: </strong>07/05/2018</span>
                <br>
                
                </div>
             <div class="dp-texto">TRANSFERENCIA DE TERRENOS PROPIEDAD DE LA PROVINCIA DE BUENOS AIRES AL ESTADO NACIONAL PARA LA CREACION DEL "PARQUE NACIONAL CIERVO DE LOS PANTANOS", UBICADO EN LA PROVINCIA DE BUENOS AIRES.</div>
             
             <div class="dp-box">
                   <h5>FIRMANTES</h5>
                   <table class="dp-firmantes table table-condensed table-striped">
                      <thead>
                         <tr>
                            <th>FIRMANTE</th>
                            <th>DISTRITO</th>
                            <th>BLOQUE</th>
                         </tr>
                      </thead>
                      <tbody>
                      
                         <tr>
                            <td>LOSPENNATO, SILVIA GABRIELA</td>
                            <td>BUENOS AIRES</td>
                            <td>PRO</td>
                         </tr>
                         <tr>
                            <td>WOLFF, WALDO EZEQUIEL</td>
                            <td>BUENOS AIRES</td>
                            <td>PRO</td>
                         </tr>
                         <tr>
                            <td>BANFI, KARINA</td>
                            <td>BUENOS AIRES</td>
                            <td>UCR</td>
                         </tr>
                         <tr>
                            <td>LIPOVETZKY, DANIEL ANDRES</td>
                            <td>BUENOS AIRES</td>
                            <td>PRO</td>
                         </tr>
                         <tr>
                            <td>ECHEGARAY, ALEJANDRO CARLOS AUGUSTO</td>
                            <td>BUENOS AIRES</td>
                            <td>UCR</td>
                         </tr>
                         <tr>
                            <td>AMADEO, EDUARDO PABLO</td>
                            <td>BUENOS AIRES</td>
                            <td>PRO</td>
                         </tr>
                         <tr>
                            <td>ACERENZA, SAMANTA MARIA CELESTE</td>
                            <td>BUENOS AIRES</td>
                            <td>PRO</td>
                         </tr>
                         <tr>
                            <td>VILLALONGA, JUAN CARLOS</td>
                            <td>CIUDAD de BUENOS AIRES</td>
                            <td>PRO</td>
                         </tr>
                         </tbody>
                   </table>
                </div>
                <div class="dp-box">
                   <h5>GIRO A COMISIONES EN DIPUTADOS</h5>
                   <table class="dp-giros-diputados table table-condensed table-striped">
                      <thead>
                         <tr>
                            <th>COMISIÓN</th>
                         </tr>
                      </thead>
                      <tbody>
                         <tr>
                            <td>LEGISLACION GENERAL</td>
                            
                         </tr>
                         <tr>
                            <td>RECURSOS NATURALES Y CONSERVACION DEL AMBIENTE HUMANO</td>
                            
                         </tr>
                         <tr>
                            <td>PRESUPUESTO Y HACIENDA</td>
                            
                         </tr>
                         </tbody>
                   </table>
                </div>
                <div class="dp-box">
                   <h5>DICTÁMENES DE COMISIÓN</h5>
                   <table class="dp-dictamenes table table-condensed table-striped">
                      <thead>
                         <tr>
                            <th>CÁMARA</th><th>DICTAMEN</th><th>TEXTO</th><th>FECHA</th>
                         </tr>
                      </thead>
                      <tbody>
                         <tr>   <td>Diputados</td>
                           <td><a href='https://www4.hcdn.gob.ar/dependencias/dcomisiones/periodo-136/136-124.pdf' target="_blank">Orden del Dia 0124/2018</a></td>
                           <td>FE DE ERRATAS</td>
                           <td>29/05/2018</td>   
                           
                           </tr>
                         </tbody>
                   </table>
                </div>
                <div class="dp-box">
                   <h5>TRÁMITE</h5>
                   <table class="dp-tramites table table-condensed table-striped">
                  <thead>
                     <tr>
                        <th>CÁMARA</th>
                        <th>MOVIMIENTO</th>
                        <th>FECHA</th>
                        <th>RESULTADO</th>
                     </tr>
                  </thead>
                  <tbody>
                     <tr>
                        <td>Diputados</td>
                        <td>CITACION SESION ESPECIAL</td>
                        <td>04/07/2018</td>
                        <td> </td>
                     </tr>
                     <tr>
                        <td>Diputados</td>
                        <td>CONSIDERACION Y APROBACION CON MODIFICACIONES</td>
                        <td>04/07/2018</td>
                        <td>MEDIA SANCION</td>
                     </tr>
                     <tr>
                        <td>Senado</td>
                        <td>PASA A SENADO -</td>
                        <td></td>
                        <td> </td>
                     </tr>
                     </tbody>
                   </table>
                </div>
                <div class="text-center" style="margin-bottom:20px;">
            <a target="_blank" class="btn btn-info" href="https://www.hcdn.gob.ar/proyectos/textoCompleto.jsp?exp=2648-D-2018&tipo=LEY">Texto completo del proyecto</a>
            
            </div>
         
         </div>
       <div class="detalle-proyecto">
             
             <h4>PROYECTO DE LEY</h4>
             <div class="dp-metadata">
                <span><strong>Iniciado en: </strong>Diputados</span>
                <span><strong>Expediente Diputados: </strong>1919-D-2018</span>
                <br>
                
                <span><strong>Publicado en: </strong>Trámite Parlamentario N° 27</span>
                <span><strong>Fecha: </strong>12/04/2018</span>
                <br>
                
                </div>
             <div class="dp-texto">REGIMEN DE INTEGRACION SOCIO URBANA Y REGULARIZACION DOMINIAL. CREACION. INMUEBLES REGISTRADOS EN EL "REGISTRO NACIONAL DE BARRIOS POPULARS -RENABAP-.</div>
             
             <div class="dp-box">
                   <h5>FIRMANTES</h5>
                   <table class="dp-firmantes table table-condensed table-striped">
                      <thead>
                         <tr>
                            <th>FIRMANTE</th>
                            <th>DISTRITO</th>
                            <th>BLOQUE</th>
                         </tr>
                      </thead>
                      <tbody>
                      
                         <tr>
                            <td>MASSOT, NICOLAS MARIA</td>
                            <td>CORDOBA</td>
                            <td>PRO</td>
                         </tr>
                         <tr>
                            <td>NEGRI, MARIO RAUL</td>
                            <td>CORDOBA</td>
                            <td>UCR</td>
                         </tr>
                         <tr>
                            <td>CARRIO, ELISA MARIA AVELINA</td>
                            <td>CIUDAD de BUENOS AIRES</td>
                            <td>COALICION CIVICA</td>
                         </tr>
                         </tbody>
                   </table>
                </div>
                <div class="dp-box">
                   <h5>GIRO A COMISIONES EN DIPUTADOS</h5>
                   <table class="dp-giros-diputados table table-condensed table-striped">
                      <thead>
                         <tr>
                            <th>COMISIÓN</th>
                         </tr>
                      </thead>
                      <tbody>
                         <tr>
                            <td>ASUNTOS CONSTITUCIONALES</td>
                            
                         </tr>
                         <tr>
                            <td>VIVIENDA Y ORDENAMIENTO URBANO</td>
                            
                         </tr>
                         <tr>
                            <td>LEGISLACION GENERAL</td>
                            
                         </tr>
                         <tr>
                            <td>PRESUPUESTO Y HACIENDA</td>
                            
                         </tr>
                         </tbody>
                   </table>
                </div>
                <div class="dp-box">
                   <h5>DICTÁMENES DE COMISIÓN</h5>
                   <table class="dp-dictamenes table table-condensed table-striped">
                      <thead>
                         <tr>
                            <th>CÁMARA</th><th>DICTAMEN</th><th>TEXTO</th><th>FECHA</th>
                         </tr>
                      </thead>
                      <tbody>
                         <tr>   <td>Diputados</td>
                           <td><a href='https://www4.hcdn.gob.ar/dependencias/dcomisiones/periodo-136/136-215.pdf' target="_blank">Orden del Dia 0215/2018 - DICTAMEN CONJUNTO DE LOS EXPEDIENTES 1919-D-2018 y 3240-D-2018</a></td>
                           <td>CON MODIFICACIONES; CON 42 DISIDENCIAS PARCIALES</td>
                           <td>02/07/2018</td>   
                           
                           </tr>
                         </tbody>
                   </table>
                </div>
                <div class="dp-box">
                   <h5>TRÁMITE</h5>
                   <table class="dp-tramites table table-condensed table-striped">
                  <thead>
                     <tr>
                        <th>CÁMARA</th>
                        <th>MOVIMIENTO</th>
                        <th>FECHA</th>
                        <th>RESULTADO</th>
                     </tr>
                  </thead>
                  <tbody>
                     <tr>
                        <td>Diputados</td>
                        <td>SOLICITUD DE SER ADHERENTE DEL DIPUTADO FLORES, HECTOR (A SUS ANTECEDENTES)</td>
                        <td></td>
                        <td> </td>
                     </tr>
                     <tr>
                        <td>Diputados</td>
                        <td>SOLICITUD DE SER ADHERENTE DE LA DIPUTADA GONZALEZ ORIETA (A SUS ANTECEDENTES)</td>
                        <td></td>
                        <td> </td>
                     </tr>
                     <tr>
                        <td>Diputados</td>
                        <td>CITACION SESION ESPECIAL CONJUNTAMENTE PARA LOS EXPEDIENTES 1919-D-2018 y 3240-D-2018</td>
                        <td>04/07/2018</td>
                        <td> </td>
                     </tr>
                     <tr>
                        <td>Diputados</td>
                        <td>CONSIDERACION Y APROBACION CON MODIFICACIONES CONJUNTAMENTE PARA LOS EXPEDIENTES 1919-D-2018 y 3240-D-2018</td>
                        <td>04/07/2018</td>
                        <td>MEDIA SANCION</td>
                     </tr>
                     <tr>
                        <td>Senado</td>
                        <td>PASA A SENADO -  CONJUNTAMENTE PARA LOS EXPEDIENTES 1919-D-2018 y 3240-D-2018</td>
                        <td></td>
                        <td> </td>
                     </tr>
                     </tbody>
                   </table>
                </div>
                <div class="text-center" style="margin-bottom:20px;">
            <button type="button" class="btn btn-info" data-toggle="collapse" data-target="#sumario213842">Sumario</button>
            <a target="_blank" class="btn btn-info" href="https://www.hcdn.gob.ar/proyectos/textoCompleto.jsp?exp=1919-D-2018&tipo=LEY">Texto completo del proyecto</a>
            
            </div>
         
         <div id="sumario213842" class="collapse well" style="margin:0;">
               DECLARAR DE UTILIDAD PUBLICA Y SUJETO A EXPROPIACION LA TOTALIDAD DE LOS BIENES INMUEBLES EN LOS QUE SE ASIENTAN LOS BARRIOS POPULARES RELEVADOS EN EL RENABAP; SUJETO EXPROPIANTE: AGENCIA DE ADMINISTRACION DE BIENES DEL ESTADO; CREACION DE FIDEICOMISO; LEY 21890: MODIFICACION DEL ARTICULO 2; INVITACION A LAS PROVINCIAS Y CABA A ADHERIR.</div>
         </div>
    </div>
"""

class HCDNParserTest(unittest.TestCase):
    def setUp(self):
        self.spider = hcdn_spider.HCDN()

    def testNProyectos(self):
        response = HtmlResponse(url='', body=html_one, encoding='utf-8')
        titulos = [
             'VINCULO JURIDICO ENTRE LA CRUZ ROJA ARGENTINA Y EL ESTADO NACIONAL. REGULACION.',
             'TRANSFERENCIA DE TERRENOS PROPIEDAD DE LA PROVINCIA DE BUENOS AIRES AL ESTADO NACIONAL PARA LA CREACION DEL "PARQUE NACIONAL CIERVO DE LOS PANTANOS", UBICADO EN LA PROVINCIA DE BUENOS AIRES.',
             'REGIMEN DE INTEGRACION SOCIO URBANA Y REGULARIZACION DOMINIAL. CREACION. INMUEBLES REGISTRADOS EN EL "REGISTRO NACIONAL DE BARRIOS POPULARS -RENABAP-.',
        ]
        for i, proyecto in enumerate(self.spider.parse(response)):
            self.assertEqual(titulos[i], proyecto['titulo'])
        self.assertEqual(2, i, "Cantidad de proyectos")

        
