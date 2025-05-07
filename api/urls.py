from django.urls import path
from . import views

urlpatterns = [
    # Subject
    path('subjects/', views.SubjectListView.as_view()),
    path('subjects/create/', views.SubjectCreateView.as_view()),
    path('subjects/<int:pk>/update/', views.SubjectUpdateView.as_view()),
    path('subjects/<int:pk>/delete/', views.SubjectDeleteView.as_view()),

    # Lecture
    path('lectures/<int:subject_id>/', views.LectureListView.as_view()),
    path('lectures/create/', views.LectureCreateView.as_view()),
    path('lectures/<int:pk>/update/', views.LectureUpdateView.as_view()),
    path('lectures/<int:pk>/delete/', views.LectureDeleteView.as_view()),

    # Practice
    path('practices/<int:lecture_id>/', views.PracticeListView.as_view()),
    path('practices/create/', views.PracticeCreateView.as_view()),
    path('practices/<int:pk>/update/', views.PracticeUpdateView.as_view()),
    path('practices/<int:pk>/delete/', views.PracticeDeleteView.as_view()),

    path('subscribers/', views.SubscriberListView.as_view(), name='subscriber-list'),
    path('subscribers/subscribe/', views.SubscriberCreateView.as_view(), name='subscriber-create'),
]
