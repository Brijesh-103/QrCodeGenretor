from django.shortcuts import render
from django.http import HttpResponse
import qrcode
from io import BytesIO
import base64

def generate_qr_code(request):
    qr_image = None
    if request.method == 'POST':
        qr_text = request.POST.get('qr_text', '')
        if qr_text:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_text)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            
            # Create a BytesIO object to store the image
            buffer = BytesIO()
            img.save(buffer, format='PNG')
            
            # Convert the image to base64 string
            qr_image = base64.b64encode(buffer.getvalue()).decode()
    
    return render(request, 'index.html', {'qr_image': qr_image})