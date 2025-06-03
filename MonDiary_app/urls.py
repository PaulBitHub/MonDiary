from django.urls import path

from MonDiary_app.views import index
from MonDiary_app.apps import MondiaryAppConfig

app_name = MondiaryAppConfig.name

urlpatterns = [
    path('', index, name='index'),
    # path('lists/', DiaryListView.as_view(), name='list'),
    # path('create/', DiaryCreateView.as_view(), name='create'),
    # path('detail/<int:pk>/', DiaryDetailsView.as_view(), name='detail'),
    # path('update/<int:pk>/', DiaryUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', DiaryDeleteView.as_view(), name='delete'),
]
