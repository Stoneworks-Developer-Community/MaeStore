import re

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from archive.models import Book
from .forms import BookUploadForm


def read(request, snowflake_id):
    entry = get_object_or_404(Book, pk=snowflake_id)
    return render(request, 'archive/read.html', {'entry': entry})


def index(request):
    world_list = {}
    for world in Book._meta.get_field('world').choices:
        try:
            world_list[world] = Book.objects.filter(world=world[0])
        except Book.DoesNotExist:
            pass
    return render(request, 'archive/index.html', {'results': world_list})


def upload(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES['file'])
        form = BookUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")
            file = request.FILES['file']

            contents = file.read().decode("utf-8")

            # Extracting title using regex
            title_match = re.search(r"title:\s*(.*)", contents)
            title = title_match.group(1).strip()

            # Extracting author using regex
            author_match = re.search(r"author:\s*(.*)", contents)
            author = author_match.group(1).strip()

            # Extracting pages using regex
            pages_match = re.search(r"pages:\s*(.*)", contents, re.DOTALL)
            pages = pages_match.group(1).strip()

            # Splitting pages into a list
            pages_list = pages.split("#-")

            if pages_list[0] == "":
                pages_list = pages_list[1:]
            
            new_item = Book(text=pages_list, title=title, author=author, genre=request.POST['genre'],
                            world=request.POST['world'])
            new_item.save()

        return HttpResponseRedirect("/index/")

    form = BookUploadForm()

    return render(request, "archive/upload.html", {"form": form})
