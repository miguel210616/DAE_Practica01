from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Region, Candidato

def index(request):
    latest_question_list=Region.objects.order_by()[:5]
    context={'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

def resultados(request,region_id):
    print(region_id,"--")
    region=get_object_or_404(Region, pk=region_id)
    print(region,"--")
    print(region.nombre_region,"--")
    return render(request, 'resultados.html',{'region':region})

def votar(request, region_id):
    region=get_object_or_404(Region, pk=region_id)
    try:
        selected_candidato=region.candidato_set.get(pk=request.POST['candidato'])
    except (KeyError, Candidato.DoesNotExist):
        return render(request, 'resultados.html', {
            'region': region,
            'error_message':"No has seleccionado un candidato.",
        })
    else:
        selected_candidato.votos +=1
        selected_candidato.save()
        return HttpResponseRedirect(reverse('votacion:urna', args=(region.id,)))

def urna(request, region_id):
    region=get_object_or_404(Region, pk=region_id)
    return render(request, 'urna.html',{'region':region})
