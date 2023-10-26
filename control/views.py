from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def listAlunos(request):

    alunos = Aluno.objects.all()
    return render(request, "listaAlunos.html", {'alunos':alunos})

def detalheAluno(request, pk):

    aluno = Aluno.objects.get(pk=pk)
    return render(request, "detalheAluno.html", {'aluno':aluno})


def alunoForm(request):

    if request.method == "GET":
        form = formAluno()

    else:
        form = formAluno(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ListAluno')

    return render(request, "formsAluno.html", {'form':form})