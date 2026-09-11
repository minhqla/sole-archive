from django.shortcuts import render

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