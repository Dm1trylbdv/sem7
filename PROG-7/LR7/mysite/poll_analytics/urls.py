from django.urls import path, include

from . import views

app_name = 'poll_analytics'
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("questions/", views.question_collection, name='questions'),
    path("questions/<int:pk>/", views.question_element, name='element'),
    path("choices/", views.choice_collection, name="choices"),
    path("choices/<int:q>", views.choices_for_question, name="choice_list")
]