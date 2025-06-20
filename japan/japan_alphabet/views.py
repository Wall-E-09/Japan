from django.shortcuts import render

from .models import JapanAlphabet

# Create your views here.
def alphabet (request):
    katakana = JapanAlphabet.objects.all()
    return render(request, 'japan_alphabet/alphabet.html', {'katakana': katakana})