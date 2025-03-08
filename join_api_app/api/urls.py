from django.urls import path
from .views import TaskOverViewSet, ContactViewSet, SummaryDetailViewSet, FindContactByEmailView

urlpatterns = [
    path("tasks/", TaskOverViewSet.as_view()),
    path("contacts/", ContactViewSet.as_view()),
    path("contacts/find-by-email/", FindContactByEmailView.as_view()),
    path("summary-detail/", SummaryDetailViewSet.as_view()),
]