from django.contrib import admin
from .models import Tailor
from .models import User
from .models import Request

admin.site.register(Request)
admin.site.register(Tailor)
admin.site.register(User)
# Register your models here.
