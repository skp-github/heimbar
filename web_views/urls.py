from django.urls import path

from web_views.views import SpecialsListView
urlpatterns = [
    path('specials/', SpecialsListView.as_view(), name="specials_list"),
]
