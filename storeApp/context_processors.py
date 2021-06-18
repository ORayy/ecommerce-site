from .models import Category


# views function for context processors
def categories(request):
    return {
        'categories': Category.objects.all()
    }
