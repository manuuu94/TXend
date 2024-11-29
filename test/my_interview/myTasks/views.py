from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from . import models
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.

def tasks(request):
    try: 
        new_dict = {}
        new_dict["tasks"] = tablelist()
        #print(new_dict)

        if request.method == 'POST' and request.POST.get('editbtn'):
            updateid(request)
            return redirect(request.path)

        if request.method == 'POST' and request.POST.get('deletebtn'):
            delete(request.POST.get('deletebtn'))
            return redirect(request.path)
        
        if request.method == 'POST' and request.POST.get('updatebtn'):
            print(request.POST.get('updatebtn'))
            return redirect(request.path)
        
        if request.method == 'POST':
            createObject(request.POST.get('Title'),
                        request.POST.get('Description'),
                        request.POST.get('status'))
            return redirect(request.path)

        

        return render(request,'spa.html',context=new_dict)
    except:
        return HttpResponse("Action failed")

##lists my tasks
def tablelist():
    new_dict = {}
    tasks = list()
    indexTask = 0
    for task in tasks:
        new_dict[f"task{indexTask}"] = {"pk":task.pk,
                                        "title":task.title,
                             "description":task.description,
                             "status":task.status}
        indexTask = indexTask + 1
    return new_dict


##creates my tasks
def createObject(title,description,status):
    try:
        models.Task.objects.create(title=title, description=description, status=status)   
    except:
        return HttpResponse("Action failed")
    
##initiates creating function
@csrf_exempt
def insert(request): 
    try:   
        if request.method == 'POST':
            title = request.POST.get("title")
            description = request.POST.get("description")
            status = request.POST.get("status")
            createObject(title,description,status)  
        return JsonResponse({"msg":"Task created"})
    except:
        return JsonResponse({"msg":"Task not created"})

def list():
    try:
        items = models.Task.objects.all()
        return items   
    except:
        return HttpResponse("Action failed")
    
def getlist(request):
    try:
        if request.method == 'GET':
            items = list()
        return HttpResponse(items)
    except:
        return HttpResponse("Action failed")

def getid(request):
    try:
        if request.method == 'GET':
            pk = request.GET['id']
            item = models.Task.objects.get(pk=pk)      
        return HttpResponse(item)
    except:
        return HttpResponse("Action failed")

#Deletes function
def delete(pk):
    try:
        models.Task.objects.get(pk=pk).delete()   
        return JsonResponse({"msg":"Task deleted"})
    except:
        return HttpResponse("Action failed")    

#Delete by ID
@csrf_exempt
def deleteid(request):
    try:
        if request.method == 'DELETE':
            pk = request.GET['pk']
            delete(pk)   
        return JsonResponse({"msg":"Task deleted"})
    except:
        return HttpResponse("Action failed")

import json

##updates my tasks PUT for API or POST for in view form
@csrf_exempt
def updateid(request):
    try:
        if request.method == 'POST':   
            pk = request.POST.get('editbtn')
            item = models.Task.objects.get(pk=pk)
            item.title = request.POST.get('edittitle')
            item.description = request.POST.get('editdesc')
            item.status = request.POST.get('status')
            item.save()

        data = json.loads(request.body)
        if request.method == 'PUT':          
            pk = data['pk']
            item = models.Task.objects.get(pk=pk)
            item.title = data['title']
            item.description = data['description']
            item.status = data['status']
            item.save()

        return JsonResponse({"msg":"Task updated"})
    except:
        return HttpResponse("Action failed")

''' update json sample
{
"id":4,
"title":"task4",
"description":"task4description",
"status":"inactive"
}
'''