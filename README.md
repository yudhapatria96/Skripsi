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
      integer_fields    = forms.IntegerField(required=false) apabila tidak required dan inputan integer
      decimal_field     = forms.DecimalField(max_length=10) inpuan desimal
      float_field       = forms.FloatField() inputan float
      boolean_field     = forms.BooleanField() inputan boolean
      char_field        = forms.CharField()
      
      email_field       = forms.EmailField()
      regex_field       = forms.RegexField()
      slug_field        = forms.SlugField()
      url_field         = forms.UrlField()
      ip_field          = forms.GenericIPAddressField()
      
      PILIHAN = (
               ('nilai 1', 'pilihan 1'),
               ('nilai 2', 'pilihan 2'),
               ('nilai 3', 'pilihan 3'),
      )
      
      choice_field          = forms.ChoiceField(choices=PILIHAN)
      multi_choice_field    = forms.MultipleChoiceField(choices=PILIHAN)
      multi_typed_field     = forms.TypedMultiChoiceField(choices=PILIHAN)
      null_boolean_field    = forms.NullBooleanField()
      
      date_field            = forms.DateField()
      datetime_field        = forms.DateTimeField()
      duration_field        = forms.DurationField()
      time_field            = forms.TimeField()
      splitdatetime_field   = forms.SplitDateTimeField()
      
      file_field            = forms.FileField()
      image_field           = forms.ImageField()
3. Pada views.py tambahkan 
    form . import forms
    
4. Pada funsi di views.py tambahkan object
    nameObject = forms.contactForm()

referensi lengkap FormsField: https://docs.djangoproject.com/en/2.2/ref/forms/fields/

/home/yudha/Pictures/Screenshot from 2019-05-30 09-54-58.png
