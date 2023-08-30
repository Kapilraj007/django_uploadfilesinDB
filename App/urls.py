
from django.contrib import admin
from django.urls import path
from Appfiles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="Home"),
    path('myuploadfile',views.myuploadfile,name="Uploadfile"),
        path('deletefile/<int:id>',views.deletefile,name="Deletefile"),

]
#to view the file in data base
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)