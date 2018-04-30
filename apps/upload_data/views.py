from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class UploadDataView(TemplateView):
    template_name = "upload_data.html"

    def post(self, request, *args, **kwargs):
        import pdb;pdb.set_trace()
