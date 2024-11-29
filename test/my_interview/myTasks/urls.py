from django.urls import path
from . import views


app_name = 'mytasks'

urlpatterns = [
    path('',views.tasks,name='mytasks'), ##SPA
    path('tasks/insert',views.insert,name='insert'), ##API INSERT 
    path('tasks/getlist',views.getlist,name='getlist'), ##API listsALL
    path('tasks/getid',views.getid,name='getid'), ##API getbyID
    path('tasks/deleteid',views.deleteid,name='deleteid'), ##API deletebyID
    path('tasks/updateid',views.updateid,name='updateid'), ##API updatesbyID

]

