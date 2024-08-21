from django.urls import path
from faceembed.views import FaceEmbedListView

urlpatterns = [
    path('api/face_embed/', FaceEmbedListView.as_view(), name='face_embed_list'),
]