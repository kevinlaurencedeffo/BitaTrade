from django.contrib import admin
from .models import CompteUser,Crypto,Transaction,OrdreMarche,Historique
admin.site.register(CompteUser)
admin.site.register(Crypto)
admin.site.register(Transaction)
admin.site.register(OrdreMarche)
admin.site.register(Historique)
admin.site.site_title="BITA Trade ADMINISTRATION"
admin.site.site_header = "BITA Trade ADMINISTRATION"