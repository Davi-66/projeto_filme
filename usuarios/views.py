from django.shortcuts import render, redirect

from usuarios.forms import UsuarioForm

from sistema.models import Usuario


#def cadastro(request):
    #return render(
        #request,
        #'cadastro.html'
    #)

def login(request):
    return render(
        request,
        'login.html'
    )

def criarUsuario(request):
    #Verificar se a requisição será do tipo GET ou POST
    if request.method == 'POST':
        # Será criado um objeto Usuario(model) com os dados enviados
        # post -> São os campos do forms (nome, sobrenome...) preenchidos.
        # files -> Conté, os arquicos ou e/imagens.
        form = UsuarioForm(request.POST, request.FILES)

        if form.is_valid(): # Se os dados forem validos são salvos no banco de dados(BD)
            form.save()
            return redirect('/usuario/login')


    else:
        # Se a reposição for GET, exibir o formulário de cadastro

        form = UsuarioForm()
    
    return render (
        request, 
        'cadastro.html', 
        {'form': form}
    )


def listarUsuarios(request):
    usuarios = Usuario.objects.all() 

    context = {
        'usuarios': usuarios,
    }

    return render(
        request,
        'usuarios/listar.html',
        context,
    )
