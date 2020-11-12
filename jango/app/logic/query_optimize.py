from django.http import HttpResponse

from app.models.many_to import *

def get_books_by_library_id():
    libraries = Library.objects.all()
    result = {}
    
    for library in libraries:
        books_in_library = library.books.all()
        result[library.id] = list(books_in_library)
    return result

def books_by_library_id_view(request):
    from IPython import embed; embed()
    books_by_library_id = get_books_by_library_id()
    return HttpResponse(response)
