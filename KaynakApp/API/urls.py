from django.urls import path
from KaynakApp.API import views as api_views
urlpatterns = [
    path('Mesajlar/', api_views.MesajAPIView.as_view()),
    path('Kullanıcılar/', api_views.KullanıcıAPIView.as_view()),
    path('Kullanıcılar/<str:pk>/', api_views.KullanıcıSpesificAPIView.as_view()),
    path('Kullanıcılar/Genel/TYTDeneme/', api_views.KullanıcıTYTDenemeAPIView.as_view()),
    path('Kullanıcılar/Genel/AYTDeneme/', api_views.KullanıcıAYTDenemeAPIView.as_view()),
    path('1/', api_views.SoruBankasıAPIView.as_view()),
    path('1/<str:pk>/', api_views.SoruBankasıSpesificAPIView.as_view()),
    path('1/Genel/Yorumlar/', api_views.SoruBankasıYorumAPIView.as_view()),
    path('1/Genel/Yorumlar/Beğeni/', api_views.SoruBankasıYorumBeğeniAPIView.as_view()),
    path('1/Genel/Yorumlar/Beğeni/<str:pk>', api_views.SoruBankasıSpesificYorumBeğeniAPIView.as_view()),
    path('1/Genel/Yorumlar/<str:pk>/', api_views.SoruBankasıSpesificYorumAPIView.as_view()),
    path('1/Genel/Puanlar/', api_views.SoruBankasıPuanlamaAPIView.as_view()),
    path('1/Genel/Puanlar/<int:pk>', api_views.SoruBankasıSpesificPuanlamaAPIView.as_view()),
    path('2/', api_views.KanalAPIView.as_view()),
    path('2/<str:pk>/', api_views.KanalSpesificAPIView.as_view()),
    path('2/Genel/Yorumlar/', api_views.KanalYorumAPIView.as_view()),
    path('2/Genel/Yorumlar/Beğeni/', api_views.KanalYorumBeğeniAPIView.as_view()),
    path('2/Genel/Yorumlar/Beğeni/<str:pk>', api_views.KanalYorumSpesificBeğeniAPIView.as_view()),
    path('2/Genel/Yorumlar/<str:pk>/', api_views.KanalSpesificYorumAPIView.as_view()),
    path('2/Genel/Puanlar/', api_views.KanalPuanlamaAPIView.as_view()),   
    path('2/Genel/Puanlar/<int:pk>', api_views.KanalSpesificPuanlamaAPIView.as_view()),
    path('3/', api_views.GenelDenemeAPIView.as_view()),
    path('3/<str:pk>/', api_views.GenelDenemeSpesificAPIView.as_view()),
    path('3/Genel/Yorumlar/', api_views.GenelDenemeYorumAPIView.as_view()),
    path('3/Genel/Yorumlar/Beğeni/', api_views.GenelDenemeYorumBeğeniAPIView.as_view()),
    path('3/Genel/Yorumlar/Beğeni/<str:pk>', api_views.GenelDenemeSpesificYorumBeğeniAPIView.as_view()),
    path('3/Genel/Yorumlar/<str:pk>/', api_views.GenelDenemeSpesificYorumAPIView.as_view()),
    path('3/Genel/Puanlar/', api_views.GenelDenemePuanlamaAPIView.as_view()),
    path('3/Genel/Puanlar/<int:pk>', api_views.GenelDenemeSpesificPuanlamaAPIView.as_view()),
    path('4/', api_views.BranşDenemesiAPIView.as_view()),
    path('4/<str:pk>/', api_views.BranşDenemesiSpesificAPIView.as_view()),
    path('4/Genel/Yorumlar/', api_views.BranşDenemesiYorumAPIView.as_view()),
    path('4/Genel/Yorumlar/Beğeni/', api_views.BranşDenemesiYorumBeğeniAPIView.as_view()),
    path('4/Genel/Yorumlar/Beğeni/<str:pk>', api_views.BranşDenemesiSpesificYorumBeğeniAPIView.as_view()),
    path('4/Genel/Yorumlar/<str:pk>/', api_views.BranşDenemesiSpesificYorumAPIView.as_view()),
    path('4/Genel/Puanlar/', api_views.BranşDenemesiPuanlamaAPIView.as_view()),
    path('4/Genel/Puanlar/<int:pk>', api_views.BranşDenemesiSpesificPuanlamaAPIView.as_view()),
 
]