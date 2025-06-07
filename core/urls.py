"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls import *
from django.urls import include, path
from home.views import *


# urlpatterns = [
#     path("admin/", admin.site.urls),
#     url(r"", include("home", name="login")),
#     url(r"^register.html/", include("home", name="register")),
#     url(r"^home.html/", include("home", name="home")),
# ]

# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path(
#         "", include("home", namespace="home")
#     ),  # Changed to path() and corrected include syntax
#     path(
#         "register.html/", include("home", namespace="home")
#     ),  # Corrected to path() and use include properly
#     path("home.html/", include("home", namespace="home")),  # Same as above
# ]


from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout.html/", include(("home.urls", "logout"), namespace="logout")),
    path("register.html/", include(("home.urls", "register"), namespace="register")),
    path("login.html/", include(("home.urls", "login"), namespace="login")),
    path("", include(("home.urls", "home"), namespace="home")),
    path(
        "forgetPassword.html/",
        include(("home.urls", "forgetPassword"), namespace="forgetPassword"),
    ),
    path("dashboard.html/", include(("home.urls", "dashboard"), namespace="dashboard")),
] + static(settings.STATIC_URL)
