from django.conf.urls import url, include
from django.contrib import admin

import todos.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # URLs for the todos app will be at the top of the site.
    url(r'^', include(todos.urls)),
]
