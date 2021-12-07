from django.shortcuts import render, render_to_response

# Create your views here.

def tasks(request):
    tasks = ["python", "research", "attachment report"]

    return render(request, "tasks/todo.html", {
        "tasks":tasks
    })
    
def add(request):
    return render(request,"tasks/add.html", {})