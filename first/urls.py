from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from budget import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'budget.views.home', name="home"),
    url(r'^contact/$', 'budget.views.contact', name="contact"),
    url(r'^incomes/$', 'budget.views.incomes', name="incomes"),
    url(r'^expenses/$', 'budget.views.expenses', name="expenses"),
    url(r'^budget/$', 'budget.views.budget', name="budget"),
    url(r'^savings/$', 'budget.views.savings', name="savings"),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
