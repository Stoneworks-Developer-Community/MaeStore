from django.shortcuts import render, get_object_or_404

from archive.models import Book


def read(request, snowflake_id):
    entry = get_object_or_404(Book, pk=snowflake_id)
    return render(request, 'archive/read.html', {'entry': entry})


def search(request):
    world_list = {}
    for world in Book._meta.get_field('world').choices:
        try:
            world_list[world] = Book.objects.filter(world=world[0])
        except Book.DoesNotExist:
            pass
    return render(request, 'archive/index.html', {'results': world_list})
