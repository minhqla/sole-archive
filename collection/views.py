from django.shortcuts import render
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
            return redirect('collection_list')
    else:
        form = CollectionItemForm()

    return render(request, 'collection/collection_form.html', {'form': form})