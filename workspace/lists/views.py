from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from lists.models import Item, List

def home_page(request):
    return render(request, 'home.html')

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = '빈 아이템을 등록할 수 없습니다'
        return render(request, 'home.html', {'error': error})
    return redirect('/lists/%d/' % (list_.id,))

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item.objects.create(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect('/lists/%d/' % (list_.id,))
        except ValidationError:
            item.delete()
            error = '빈 아이템을 등록할 수 없습니다'
    return render(request, 'list.html', {'list': list_, 'error': error})
