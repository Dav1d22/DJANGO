from django.http import HttpResponse
from django.template import loader
from django.template import Template,Context

import datetime

def saludar(request):
    doc_externo = open("C:/Users/USUARIO/Desktop/proyecto/MiProyecto/MiProyecto/plantillas/primeraplantilla.html")
    plt = loader.get_template(doc_externo.read())
    doc_externo.close()
    cxt = {}  
    documento = plt.render(cxt)
    return HttpResponse(documento)

def fecha(request):
    fechaActual = datetime.datetime.now()
    documento = f"""
        <html>
            <head>
                <title>ESTA ES UNA ESTRUCTURA BASICA DE UN DOCUMENTO HTML</title>
            </head>
            <body>
                <h1> Usted ingreso o actualizo esta vista en la fecha {fechaActual} </h1>
            </body>
        </html>"""
    return HttpResponse(documento)

def tareaEnlistadas(request):
    Tareas = ["aprender sobre el  internet", "Aprender HTML", "Aprender CSS", "Practicar Python", "Aprender Django", "Consultar mi propia WEB"]
    doc_externo = loader.get_template("segundaplantilla.html")
    cxt = {"listado": Tareas}
    documento = doc_externo.render(cxt)
    return HttpResponse(documento)

def games(request):

    agno=datetime.datetime.now().year
    dia=datetime.datetime.now().day
    mes=datetime.datetime.now().month
    hora=datetime.datetime.now().strftime("%X")

    fecha="%s/%s/%s a las %s" %(dia,mes,agno,hora)
    doc_externo=loader.get_template("games.html")
    documento=doc_externo.render({"fecha":fecha})
    return HttpResponse(documento)