"""recipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path

from calculator.views import recipe_fun, home_view

# from calculator.views import recipe_fun omlet_recipe, pasta_recipe, buter_recipe

urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию

    # path('omlet/', omlet_recipe, name="omlet"),
    # # path('omlet/<int:count>/', omlet_recipe),
    #
    # path('pasta/', pasta_recipe, name="omlet"),
    # path('pasta/<int:count>/', pasta_recipe),
    #
    # path('buter/', buter_recipe, name="omlet"),
    # path('buter/<int:count>/', buter_recipe),
    path('', home_view),
    path('<str:recipe_name>/', recipe_fun, name='recipe')
]
