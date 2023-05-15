from django.http import HttpResponse
from django.template import Template, Context

def regUser(request):
    doc_ext = open('/home/moarsot/Escritorio/DjangoEsuc/Clase/Clase/templates/Registro.html')

    plantilla= Template(doc_ext.read())

    doc_ext.close()

    ctx = Context()

    documento = plantilla.render(ctx)

    return HttpResponse(documento)


