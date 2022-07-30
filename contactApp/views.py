from django.shortcuts import render
from .forms import Contact_form
from .models import CFgmail
import os.path
import sys
sys.path.append('C:/Users/dcrash0veride/PycharmProjects/stegoBE/pkgBE')
import hashBE

# Create your views here.


def contact(request):
    context = {}
    if request.method == 'POST':
        print("post triggered")
        form = Contact_form(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print("form be bvalid")
            fname = form.cleaned_data.get("name")
            email_address = form.cleaned_data.get("email_address")
            content = form.cleaned_data.get("content")
            content_hash = hashBE.hash2to1(email_address, content)
            if CFgmail.objects.filter(content_address_hash=content_hash).exists():
                #This might be an opportunity to fire an alert and block this whole squad
                # alert.generate()
                return render(request, 'contactApp/success.html')
            else:
                contact_obj = CFgmail.objects.create(fname=fname,
                                                     email_address=email_address,
                                                     content=content,
                                                     content_address_hash=content_hash)
            contact_obj.save()
            return render(request, 'contactApp/success.html')
        else:
            form = Contact_form()
    context['form'] = Contact_form()
    return render(request, "contactApp/contact.html", context)

def contactSuccess(request):
    return render(request, 'contactApp/success.html')