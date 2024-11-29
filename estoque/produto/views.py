from django.shortcuts import render, redirect
from .forms import ProdutoForm

def produto_new(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/')  
    else:
        form = ProdutoForm()

    return render(request, 'produto_new.html', {'form': form})
