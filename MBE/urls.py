from django.conf.urls.static import static
from django.urls import path
from mysite import settings
from .views import base_views, question_views, answer_views

app_name = 'MBE'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<str:category_name>/',
         base_views.index, name='index'),
    path('question/detail/<int:question_id>/',
         base_views.detail, name='detail'),

    # question_views.py
    path('question/create/<str:category_name>/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),
    path('question/vote/<int:question_id>/',
         question_views.question_vote, name='question_vote'),
    path('question/download/<int:question_id>/',
         question_views.question_download_view, name="question_download"),



    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),
    path('answer/vote/<int:answer_id>/',
         answer_views.answer_vote, name='answer_vote'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
