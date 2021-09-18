from django.urls import path
from web_views.views import SpecialsListView, SalesOverviewListView

urlpatterns = [
    path('specials/', SpecialsListView.as_view(), name="specials_list"),
    path('drinks_analytics/', SalesOverviewListView.as_view(), name="drinks_analytics"),
]
