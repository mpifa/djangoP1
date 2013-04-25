from django.contrib import admin

from main.models import Game,Platform,Company,Type,Made,BelongsTo,SupportedBy


admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Company)
admin.site.register(Type)
admin.site.register(Made)
admin.site.register(BelongsTo)
admin.site.register(SupportedBy)
#admin.site.register(Review)
#admin.site.register(Reviews)