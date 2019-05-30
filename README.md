# skripsi
Membuat Aplikasi Peramalan Dengan Django

1. python manage.py runserver
2. python manage.py createsuperuser
3. python manage.py makemigrations
4. python manage.py migrate
5. python manage.py startapp namaApp (jangan lupa tambahkan di bagian setting bagian INSTALLED_APPS)

Membuat Form dengan ContactForm Django

1. Membuat forms.py pada apps
2. Tuliskan code di bawah ini
    from django import forms

    class ContactForm(forms.Form):
      integer_fields = forms.IntegerField(required=false) apabila tidak required dan inputan integer
      decimal_field = forms.DecimalField() inpuan desimal
      float_field = forms.FloatField() inputan float
      boolean_field = forms.BooleanField() inputan boolean
      char_field = forms.CharField()

3. Pada views.py tambahkan 
    form . import forms
    
4. Pada funsi di views.py tambahkan object
    nameObject = forms.contactForm()
