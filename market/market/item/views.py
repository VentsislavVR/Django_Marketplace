from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from market.item.forms import NewItemForm, EditItemForm
from market.item.models import Item, Category


def browse(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)

    if category_id:
        items = items.filter(category_id=category_id)

    query = request.GET.get('query', '')
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    context = {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    }

    return render(
        request,
        'item/browse.html',
        context
    )
# Create your views here.
def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(
        category=item.category,
        is_sold=False,
    ).exclude(pk=item.pk)[:3]

    context = {
        'item': item,
        'related_items': related_items
    }

    return render(
        request,
        'item/detail.html',
        context
    )


@login_required
def add_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('detail', pk=item.pk)

    form = NewItemForm()

    context = {
        'form': form,
        'title': 'New item'
    }

    return render(
        request,
        'item/form.html',
        context)


@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return render(request,
                  'dashboard/dashboard.html',
                  )


@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('detail', pk=item.pk)

    form = EditItemForm(instance=item)

    context = {
        'form': form,
        'title': 'Edit item'
    }

    return render(
        request,
        'item/form.html',
        context)
