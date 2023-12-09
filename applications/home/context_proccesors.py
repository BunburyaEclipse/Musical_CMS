from .models import Contact

def Contact_Processor(request):
    contact = Contact.objects.last()
    return {
        'contact': contact
    }