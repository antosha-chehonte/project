from bs4 import BeautifulSoup
from datetime import date
import mammoth
from django.shortcuts import render


def order(request):
    today = date.today()
    # output_filename = 'C:/py/sitedir/templates/include/order/result.html'

    if request.method == 'POST':

        input_docx_file = request.FILES['file'].file
        result = mammoth.convert_to_html(input_docx_file)
        # text = result.value
        text = ' '.join(result.value.split())
        soup = BeautifulSoup(text, "html.parser")
        cels = soup.find_all('td')

        if cels:
            cel1 = cels[0]
            cel2 = cels[1]
        else:
            cel1 = "cel1 отсутствует"
            cel2 = "cel2 отсутствует"

        with open('C:/py/project/templates/include/order/result.html', 'w', encoding='utf-8') as text_file:
            text_file.write(text)

        context = {
            'today': today,
            'table': cels,
            'cel1': cel1,
            'cel2': cel2,
        }
        return render(request, template_name="order/order_upload_success.html", context=context)

    context = {
        'today': today,
    }
    return render(request, template_name="order/order_upload.html", context=context)
