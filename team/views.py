from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .forms import TeamForm
from .models import Team
# Create your views here.

@login_required
def teams_list(request):
    teams =Team.objects.filter(members__in=[request.user])

    return render(request,'team/teams_list.html',{ 'teams':teams })


@login_required
def detail(request,pk):
   team=get_object_or_404(Team,created_by=request.user,pk=pk)
   
   return render(request,'team/detail.html',{ 'team':team })



@login_required
def edit_team(request,pk):
    team=get_object_or_404(Team,created_by=request.user,pk=pk)

    
    

    if request.method == 'POST':
        form = TeamForm(request.POST,instance=team)

        if form.is_valid():
            form.save()

            messages.success(request,'The Changes were Saved!')
            return redirect('userprofile:myaccount')

    else:
        form=TeamForm(instance=team)
    return render(request, 'team/edit_team.html',{
        'team':team,
        'form':form
    })