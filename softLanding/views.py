from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse

# Create your views here.

def home(request):
    return render(request, 'softLanding/index.html')

def contact(request):
    return render(request, 'contactApp/contact.html')

def resume(request):
    return FileResponse(open(
        '/gda/resumeApp/templates/resume\\resume.pdf', 'rb'),
        as_attachment=False,content_type='application/pdf')

def stego(request):
    return render(request, 'tools/stego.html')

def stegoEncoder(request):
    context = {}
    if request.method == "POST":
        form = stegoEncoderForm(request.POST, request.FILES)
        if form.is_valid():
            secretMessage = form.cleaned_data.get("secretMessage")
            img = form.cleaned_data.get("uploadedImage")
            obj = stegoImagesModel.objects.create(secretMessage=secretMessage, uploadedImage=img)
            obj.save()
            print(obj)
        else:
            form = stegoEncoderForm()
    context['form'] = stegoEncoderForm()
    return render(request, "tools/stegoEncoder.html", context)