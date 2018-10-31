from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core.forms import FuncionarioForm
from core.models import Setor


def register(request):
    form = FuncionarioForm()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        funcionario = form.save(commit=False)

        if form.is_valid():
            print("Formulário válido, setor: {}".format(funcionario.setor))

    return render(request, "register.html", locals())


def register_with_sector(request, setor_pk):
    setor = get_object_or_404(Setor, pk=setor_pk)
    form = FuncionarioForm(setor=setor)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, setor=setor)
        funcionario = form.save(commit=False)

        if form.is_valid():
            print("Formulário válido, setor: {}".format(funcionario.setor))

    return render(request, 'register.html', locals())