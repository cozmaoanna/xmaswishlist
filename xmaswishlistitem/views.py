from django.shortcuts import render, redirect, get_object_or_404
from .models import xmaswishlistitem
from .forms import xmaswishlistitemForm
# Create your views here.
def get_index(request):
    results = xmaswishlistitem.objects.all()
    return render(request, "index.html", {'items': results})


def add_item(request):
    if request.method == "POST":
        # Get the details from the request
        form = xmaswishlistitemForm(request.POST)
        # Handle Saving to DB
        if form.is_valid():
            form.save()
            return redirect(get_index)
    else:
        # GET Request so just give them a blank form
        form = xmaswishlistitemForm()    
    
    return render(request, "item_form.html", { 'form': form })



def edit_item(request, id):
    
    item = get_object_or_404 (xmaswishlistitem, pk = id)
    
    if request.method == "POST": 
        form = xmaswishlistitemForm(request.POST, instance=item)
        if form.is_valid(): 
            form.save()
            return redirect(get_index)
        
        
    else: 
        form = xmaswishlistitemForm(instance=item)
        
        
    return render(request, "item_form.html", { 'form': form })
    
    

def toggle_status(request, id):     
    item = get_object_or_404(xmaswishlistitem, pk=id)
    
   # if item.done == True: 
    #     item.done = False 
    # else: 
    #     item.done = True


    item.done = not item.done
    item.save()
    
    return redirect(get_index)
