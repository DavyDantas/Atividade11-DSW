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

def editAluno(request, pk):

    obj = Aluno.objects.get(pk = pk)
    form = formAluno(request.POST, instance=obj)

    if request.method == "GET":
        initial_data = {field: getattr(obj, field) for field in obj.__dict__.keys() if field in formAluno.Meta.fields}
        form = formAluno(instance=obj, initial=initial_data)
    if request.method == "POST":

        if form.is_valid():
            form.save()
            return redirect('ListAluno')

    return render(request, 'edit-aluno.html', {'form':form})

def deletAluno(request, pk):

    obj = Aluno.objects.get(pk=pk)

    if request.method == "POST":

        obj.delete()
        return redirect('ListAluno')
    
    return render(request, 'delet-aluno.html')
