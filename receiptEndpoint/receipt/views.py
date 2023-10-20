from django.core.cache import cache
from django.views import View
from django.http import JsonResponse
import json, uuid
from . import ReceiptUtil

class ReceiptView(View):

    def post(self, request):
        global_dict = cache.get('Receipt_global_dict')
        
        if global_dict is None:
            global_dict = {}

        try:
            data = request.body.decode()
            data_dict = json.loads(data)

            point = ReceiptUtil.process(data_dict)
            receipt_id = str(uuid.uuid4())
            
            receipt_dict = data_dict
            receipt_dict["id"] = receipt_id
            receipt_dict["point"] = point
            
            global_dict[receipt_id] = receipt_dict

            cache.set('Receipt_global_dict', global_dict)

            return JsonResponse({"id": receipt_id})
        except Exception as e:
            print(e)
            return JsonResponse({"error": "The receipt is invalid"}, status=400)
        
    
    def get(self, request, id):
        global_dict = cache.get('Receipt_global_dict')

        if global_dict is None:
            return JsonResponse({"error": "Receipt dictionary not initailzed"}, status=500)

        receipt = global_dict.get(id)

        if receipt is None: 
            return JsonResponse({"error": "No receipt found for that id"}, status=404)
        
        point = receipt.get("point")

        return JsonResponse({"point": point})
