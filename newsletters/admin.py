from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SingUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__str__", "email", "timestamp", "updated"]
    form = SingUpForm
  #  class meta:
  #      model = SignUp


admin.site.register(SignUp, SignUpAdmin)
