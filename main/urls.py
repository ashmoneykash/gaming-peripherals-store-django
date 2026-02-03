from os import path
from . import views

urlpatterns = [
    # existing urls...
    path("contact/", views.contact_view, name="contact"),
]
