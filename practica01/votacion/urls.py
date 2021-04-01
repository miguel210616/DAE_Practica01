from django.urls import path

from . import views

app_name='votacion'

urlpatterns=[
    # ex: /votacion/
    path('',views.index,name='index'),
    # ex: /votacion/1/
    path('<int:region_id>/',views.resultados,name='resultados'),
    # ex: /votacion/1/
    path('<int:region_id>/urna/',views.urna,name='urna'),
    # ex: /votacion/1/
    path('<int:region_id>/voto/',views.votar,name='votar')
    
]