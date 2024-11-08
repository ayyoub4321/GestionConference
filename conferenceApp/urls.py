from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('registre',views.registre,name='registre'),
    path('conference',views.conference,name='conference'),
    path('session',views.session,name='session'),
    path('deconnection',views.deconnection,name='deconnection'),
    path('ajouterSession',views.ajouterSession,name='ajouterSession'),
    path('ajouterConference',views.ajouterConference,name='ajouterConference'),
    path('modifierConference/<int:id>',views.modifierConference,name='modifierConference'),
    path('modifierSession/<int:id>',views.modifierSession,name='modifierSession'),
    path('suprimerConference/<int:id>',views.suprimerConference,name='suprimerConference'),
    path('supprimerSession/<int:id>',views.supprimerSession,name='supprimerSession'),
    path('intervenant/<int:id>',views.intervenant,name='intervenant'),
    path('ajouterIntervenant/<int:id>',views.ajouterIntervenant,name='ajouterIntervenant'),
    path('modifierIntervenant/<int:id>',views.modifierIntervenant,name='modifierIntervenant'),
    path('suprimerIntervenant/<int:id>',views.suprimerIntervenant,name='suprimerIntervenant')


]