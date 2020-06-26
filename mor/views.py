from django.shortcuts import render, get_object_or_404
from .models import Morpheme
from django.utils import timezone
from .forms import MorForm
from django.shortcuts import redirect

def important_words(request):

    mor = get_object_or_404(Morpheme, pk=1)

    if request.method == "POST":
        #form = MorForm(request.POST, instance=pytest)
        form = MorForm()
    else:
        form = MorForm()

    input_text = request.POST.get('input_text')
    if input_text is None:
        input_text = ""

    words = input_text.split()
    word_index = {k:v for v, k in enumerate(words)}

    positive_checkbox_words = request.POST.getlist('positive_checkbox_words')
    negative_checkbox_words = request.POST.getlist('negative_checkbox_words')
    checkbox_words = list(dict.fromkeys(positive_checkbox_words + negative_checkbox_words))
    checkbox_words.sort(key=lambda x: word_index[x])

    if 'submit_split' in request.POST:
        None

    is_saved = None
    if 'submit_save' in request.POST:
        mor = Morpheme()
        mor.text = input_text
        mor.words = ','.join(checkbox_words)
        mor.positive_words = ','.join(positive_checkbox_words)
        mor.negative_words = ','.join(negative_checkbox_words)
        mor.save()
        input_text = ''
        words = ''
        is_saved = True


    return render(request, 'mor/important_words.html', {'mor':mor, 'form':form, 'input_text':input_text, 'words':words, 'is_saved':is_saved})