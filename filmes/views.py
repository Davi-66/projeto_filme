from django.shortcuts import render, redirect

from sistema.models import Filme

from filmes.forms import FilmeForm

def cadastrarFilme(request):
    #Verificar se a requisição será do tipo GET ou POST
    if request.method == 'POST':
        
        form = FilmeForm(request.POST, request.FILES)

        if form.is_valid(): 
            form.save()
            return redirect('listarfilmes')


    else:
        

        form = FilmeForm()
    
    return render (
        request, 
        'filmes/cadastrar.html', 
        {'form': form}
    )



def listarFilmes(request):
    filmes = Filme.objects.all() 

    context = {
        'filmes': filmes,
    }

    return render(
        request,
        'filmes/listar.html',
        context,
    )


# Create your views here.
