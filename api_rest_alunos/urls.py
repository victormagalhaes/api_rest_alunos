from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from disciplinas import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^disciplinas/$', views.DisciplinaList.as_view()),
    url(r'^disciplinas/(?P<pk>[0-9]+)/$', views.DisciplinaDetail.as_view()),

    url(r'^alunos/$', views.AlunoList.as_view()),
    url(r'^alunos/(?P<pk>[0-9]+)/$', views.AlunoDetail.as_view()),

    url(r'^notas/$', views.DisciplinaAlunoList.as_view()),
    url(r'^notas/(?P<pk>[0-9]+)/$', views.DisciplinaAlunoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
