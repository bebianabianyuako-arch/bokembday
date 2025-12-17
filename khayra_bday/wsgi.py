import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'khayra_bday.settings')

application = get_wsgi_application()
app = application  # <--- TAMBAHKAN BARIS INI