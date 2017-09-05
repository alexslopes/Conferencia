from django.contrib import admin
from .models import Atividade
from .models import Type
from .models import Tags
from .models import Apresentadores
from .models import Sala


admin.site.register(Atividade)
admin.site.register(Type)
admin.site.register(Tags)
admin.site.register(Apresentadores)
admin.site.register(Sala)
