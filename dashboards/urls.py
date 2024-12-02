from django.urls import path
from . import views

urlpatterns = [
    # Power BI dashboard URLs
    path('powerbi/faculty/', views.powerbi_faculty_view, name='powerbi_faculty'),
    path('powerbi/iku/', views.powerbi_iku_view, name='powerbi_iku'),
    path('powerbi/uad/', views.powerbi_uad_view, name='powerbi_uad'),

    # Redash URLs (jika diperlukan)
    path('raw-data/', views.redash_embed_view, name='redash_embed'),
    path('raw-data/download/', views.redash_download_excel, name='redash_download')
]