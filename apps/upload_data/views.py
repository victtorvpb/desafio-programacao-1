from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import pandas as pd
from django.db import transaction
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

from .models import Invoices



@method_decorator(csrf_exempt, name='dispatch')
class UploadDataView(TemplateView):
    template_name = "upload_data.html"

    @transaction.atomic
    def post(self, request, *args, **kwargs):

        file_upload = request.FILES.get('upload')

        try:
            file_data_frame = pd.read_csv(
                file_upload,
                delimiter='\t',
            )

            for index, row in file_data_frame.iterrows():
                Invoices.objects.create(
                    purchaser_name=row.get('purchaser name'),
                    item_description=row.get('item description'),
                    item_price=row.get('item price'),
                    purchase_count=row.get('purchase count'),
                    merchant_address=row.get('merchant address'),
                    merchant_name=row.get('merchant name'),
                )

            messages.success(request, 'Arquivo importado com sucesso')
        except:

            messages.error(request, 'Arquivo é inválido')

        return redirect(reverse('upload_data:upload'))

