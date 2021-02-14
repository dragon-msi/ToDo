from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import requires_csrf_token
from .models import TODO
from django.core.mail import send_mail
# Create your views here.
def todo(request):
    todo_item=TODO.objects.all()
    my_context={
        'todo':todo_item
    }
    return render(request,'base.html',my_context)
@requires_csrf_token
def addTodo(request):
    
    new_item=TODO(item=request.POST['todoItem'])
    new_item.save()
    return HttpResponseRedirect('/todo/')


@requires_csrf_token
def deleteTodo(request,todo_id):
    item_to_delete=TODO.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/todo/')
@requires_csrf_token
def contact(request):
    msg_name=request.POST['msg']
    email_name=request.POST['email']


    send_mail(
        'Regarding To Do', # subjecctpip install pylint-django
        "Thanks for the feedback", # Message
        '........', # from Email
        [email_name] # To Email
    )
    return HttpResponseRedirect('/todo/')
