from django.shortcuts import render, get_object_or_404
from items.models import Item, ItemType
from django.db.models import Q




BOOT_GROUPS = (
    (ItemType.Code.BOOT1, "پایه"),
    (ItemType.Code.BOOT2, "میان رده"),
    (ItemType.Code.BOOT3, "تکامل یافته"),
)
BOOT_CODES = [code for code, _ in BOOT_GROUPS]


def get_section_context():


    item_types = (
        ItemType.objects.prefetch_related("items").exclude(code__in=BOOT_CODES)
    )

    boot_groups = [
        {
            "label": label,
            "items": Item.objects.filter(type__code=code).distinct().order_by("name"),
        }
        for code, label in BOOT_GROUPS
    ]

    return {"item_types": item_types, "boot_groups": boot_groups}



def items_page(request):

    return render(request, "items/items.html", get_section_context())


def item_search(request):

    query = request.GET.get("q", "").strip()

    if not query:
        return render(request, "partials/item_sections.html", get_section_context())
    
    items = Item.objects.filter(Q(name__icontains=query))
    
    return render(request, "partials/item_search_results.html", 
                  {
                      "items": items,
                      "query": query,
                  })


def item_page(request, slug):

    item = get_object_or_404(Item, slug=slug)
    context = {"item": item}

    return render(request, "partials/item_detail_partial.html", context)