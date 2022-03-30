from django.shortcuts import render

# Create your views here.
def count(request):
    text = request.POST.get('text', '')
    if text=='':
        text='글자를 입력해보세요'
    total_len = len(text)
    no_blank_len = len(text.replace(' ', '').replace('\n', '').replace('\t', ''))
    NOWords = text.count(' ')+text.count('\n')+text.count('\t')+1
    return render(request, 'count.html', {'text': text, 'total_len': total_len, 'no_blank_len': no_blank_len, 'NOWords': NOWords})