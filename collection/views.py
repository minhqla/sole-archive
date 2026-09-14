from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import CollectionItem
from .forms import CollectionItemForm

# Create your views here.
# SIGNUP - create a new user account, then log them straight in
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('collection_list')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})

# READ - show all items that belong to the logged in user
@login_required
def collection_list(request):
    items = CollectionItem.objects.filter(user=request.user)
    return render(request, 'collection/collection_list.html', {'items': items})


# READ - show one item in detail
@login_required
def collection_detail(request, pk):
    item = get_object_or_404(CollectionItem, pk=pk, user=request.user)
    return render(request, 'collection/collection_detail.html', {'item': item})


# CREATE - add a new item to the collection
@login_required
def collection_create(request):
    if request.method == 'POST':
        form = CollectionItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)  # don't save to db yet
            new_item.user = request.user         # attach the logged in user
            new_item.save()
            messages.success(request, f'"{new_item.sneaker}" was added to your collection.')
            return redirect('collection_list')
    else:
        form = CollectionItemForm()

    return render(request, 'collection/collection_form.html', {'form': form})


# UPDATE - edit an existing item
@login_required
def collection_create(request):
    if request.method == 'POST':
        form = CollectionItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)  # don't save to db yet
            new_item.user = request.user         # attach the logged in user
            new_item.save()
            messages.success(request, f'"{new_item.sneaker}" was added to your collection.')
            return redirect('collection_list')
    else:
        form = CollectionItemForm()

    return render(request, 'collection/collection_form.html', {'form': form})


# DELETE - remove an item from the collection
@login_required
ef collection_delete(request, pk):
    item = get_object_or_404(CollectionItem, pk=pk, user=request.user)

    if request.method == 'POST':
        sneaker_name = str(item.sneaker)  # grab the name before it's deleted
        item.delete()
        messages.success(request, f'"{sneaker_name}" was removed from your collection.')
        return redirect('collection_list')

    return render(request, 'collection/collection_confirm_delete.html', {'item': item})  