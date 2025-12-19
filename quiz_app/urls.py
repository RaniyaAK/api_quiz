from django.urls import path
from . import views

urlpatterns=[
    path ('api/all_quiz/',views.quiz,name="quiz"),
    path ('api/add_quiz/',views.add_quiz,name="add_quiz"),
    path ('api/update_quiz/<int:quiz_id>/',views.update_quiz,name="update_quiz"),
    path ('api/delete_quiz/<int:quiz_id>/',views.delete_quiz,name="delete_quiz"),
    path ('api/search_quiz/',views.search_quiz,name="search_quiz"),
]