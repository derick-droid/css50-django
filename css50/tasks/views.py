from django.shortcuts import render, render_to_response
from django import forms
# Create your views here.
# generating django html forms 
class NewTask(forms.Form):
    tasks1 = forms.CharField(label = "New activity")
    # priority = forms.IntegerField(label="priority", min_value=1, max_value= 10)
    
# list of activities
def tasks(request):
    tasks = ["python", "research", "attachment report"]


    return render(request, "tasks/todo.html", {
        "tasks":tasks
    })
    
# adding more activities 
def add(request):
    if request.method == "POST":
        forms = NewTask(request.POST)
        if forms.is_valid():
            taskz = forms.cleaned_data["tasks1"]
            tasks.append(taskz)
        else:
            return render(request, "tasks/add.html", {
                "form": forms
            })
            
    return render(request,"tasks/add.html", {
        "forms":NewTask()
    })