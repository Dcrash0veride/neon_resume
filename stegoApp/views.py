import mimetypes
import os.path
import sys
sys.path.append('C:/Users/dcrash0veride/PycharmProjects/stegoBE/pkgBE')
import hashlib
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import FileResponse
from .forms import stegoEncoderForm
from .forms import stegoDecoderForm
from .models import stegoImagesModel, stegoDecodeModel
import stegoBE
import hashBE



# Create your views here.
def stego(request):
    return render(request, 'stego/stego.html')


""" Need to adjust this view, primary key is currently ID, but I would like that to be homogenous
between tables, this will require an updated URL and some changes to dependent function.
Also will need to replicate check if exists from decode success """
def stegoEncoder(request):
    context = {}
    if request.method == "POST":
        form = stegoEncoderForm(request.POST, request.FILES)
        if form.is_valid():
            secretMessage = form.cleaned_data.get("secretMessage")
            img = form.cleaned_data.get("uploadedImage")
            instanceDict = hashBE.hashbytessha256(secretMessage, img)
            whereGoes = "media/upload/" + instanceDict["FileName Hash"]
            file_extension = ".png"
            sendit = whereGoes + file_extension
            stegoBE.encode(img, secretMessage, whereGoes)
            if stegoImagesModel.objects.filter(comboHash=instanceDict["FileName Hash"]).exists():
                obj = stegoImagesModel.objects.get(comboHash=instanceDict["FileName Hash"])
            else:
                obj = stegoImagesModel.objects.create(secretMessage=instanceDict["Message Hash"],
                                                    uploadedImage=instanceDict["Image Hash"],
                                                    comboHash=instanceDict["FileName Hash"],
                                                    webLink=sendit)
            obj.save()
            return redirect('stegoSuccess', obj.pk)
        else:
            form = stegoEncoderForm()
    context['form'] = stegoEncoderForm()
    return render(request, "stego/stegoEncoder.html", context)

def stegoDecoder(request):
    context = {}
    if request.method == "POST":
        form = stegoDecoderForm(request.POST, request.FILES)
        if form.is_valid():
            img_to_decode = form.cleaned_data.get("imageToDecode")
            message_string = stegoBE.decode(img_to_decode)
            instance_dict = hashBE.hashbytessha256(message_string, img_to_decode)
            # Need to check if object already exists and if not create it, if it does then we need to use that
            if stegoDecodeModel.objects.filter(double_hash=instance_dict["FileName Hash"]).exists():
                d_obj = stegoDecodeModel.objects.get(double_hash=instance_dict["FileName Hash"])
            else:
                d_obj = stegoDecodeModel.objects.create(s_message=message_string,
                                                        enc_img_hash=instance_dict["Image Hash"],
                                                        double_hash=instance_dict["FileName Hash"])
                d_obj.save()
            return redirect('decoderSuccess', d_obj.pk)
        else:
            form = stegoDecoderForm()
    context['form'] = stegoDecoderForm()
    return render(request, 'stego/stegoDecoder.html', context)

def decoderSuccess(request, pk):
    db_obj = stegoDecodeModel.objects.get(double_hash=pk)
    message = db_obj.s_message
    return render(request, 'stego/decodesuccess.html', {'message': message})

def stegoSuccessEncoding(request, pk):
    encoded_images = stegoImagesModel.objects.filter(comboHash=pk)
    return render(request, 'stego/success.html', {'encoded_images': encoded_images})

def allStego(request):
    encoded_images = stegoImagesModel.objects.all()
    return render(request, 'stego/allStego.html', {'encoded_images': encoded_images})

def downloadStego(request, pk):
    encoded_images_comboWombo = pk
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_extension = ".png"
    fname = encoded_images_comboWombo + file_extension
    fullUrl = BASE_DIR + "\\media\\upload\\" + fname
    return FileResponse(open(fullUrl, 'rb'), as_attachment=True, content_type='image/png')

