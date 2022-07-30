from django import forms

class stegoEncoderForm(forms.Form):
    uploadedImage = forms.ImageField()
    uploadedImage.widget.attrs.update({'class': 'specialEncoder'})
    secretMessage = forms.CharField(widget=forms.Textarea)

class stegoDecoderForm(forms.Form):
    imageToDecode = forms.ImageField()
    imageToDecode.widget.attrs.update({'class': 'specialDecoder'})