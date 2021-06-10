from datetime import date
import mammoth
from django.shortcuts import render
from order.models import Order


def order(request):

    date_now = date.today()

    if request.method == 'POST':
        input_docx_file = request.FILES['file'].file
        result = mammoth.convert_to_html(input_docx_file)

        order_text = Order(text=result.value, date=date_now, number='номер приказа', title='название приказа')
        order_text.save()
        text = Order.objects.all()

        context = {
            'text': text,
                    }
        return render(request, template_name="order/order_upload_success.html", context=context)
    else:
        text = 'текста нет'
        context = {
            'text': text,
        }
        return render(request, template_name="order/order_upload.html", context=context)
