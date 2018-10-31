from django.shortcuts import render
from core.forms import FuncionarioForm

def register(request):
    form = FuncionarioForm()

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        funcionario = form.save(commit=False)

        if form.is_valid():
            print("Formulário válido, setor: {}".format(funcionario.setor))

    return render(request, "register.html", locals())
