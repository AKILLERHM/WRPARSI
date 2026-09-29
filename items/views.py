from django.shortcuts import render, get_object_or_404
from items.models import Item, ItemType
from django.db.models import Q

def items_page(request):

    item_types = ItemType.objects.prefetch_related("items").all()
    context = {"item_types": item_types}

    return render(request, "items/items.html", context)


def item_search(request):

    query = request.GET.get("q", "").strip()

    if not query:
        item_types = ItemType.objects.prefetch_related("items").all()

        return render(request, "partials/item_sections.html",
                      {
                          "item_types": item_types,
                          }
                          )
    else:

        items = Item.objects.filter(
        Q(name__icontains=query)
        )
    

    return render(request, "partials/item_search_results.html", 
                  {
                      "items": items,
                      "query": query,
                  })


def item_page(request, slug):

    item = get_object_or_404(Item, slug=slug)
    context = {"item": item}

    return render(request, "partials/item_detail_partial.html", context)