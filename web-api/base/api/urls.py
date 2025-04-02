from django.urls import path

from . import views


urlpatterns = [
    path('exh/<int:id>', views.get_exhibit_by_id, name='get_exhibit_by_id'),
    path('sec/<int:id>', views.get_section_by_id, name='get_sectiont_by_id'),
    path('exhs_by_sec/<int:section_id>', views.get_exhibit_by_section, name='get_exhibit_by_section'),
    path('all_sec/', views.get_all_sections, name='get_all_sections'),
    path('game/<int:id>/', views.get_game, name='get_game'),
    path('ques_by_game/<int:id>/', views.get_questions_by_game_id, name='get_questions_by_game_id'),
    path('index/', views.index, name='index'),
    path('games/', views.games, name='games'),
    path('edit/<str:type>/<int:id>/', views.edit, name='edit'),
    path('create/<str:type>/', views.create, name='create'),
    path('delete/<str:type>/<int:id>/', views.delete, name='delete'),
    path('rank/<int:id>/<int:rank>/', views.rank, name='rank'),
    path('get_img/<int:id>/', views.get_image, name='get_image'),
    path('backup/<str:key>/', views.backup, name='backup'),
    path('backup_images/<str:key>/', views.backup_images, name='backup_images'),
]
