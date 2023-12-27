from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        min_length = 2,
        max_length = 50,
        widget = forms.TextInput(
            attrs = {'placeholder': 'Ваше имя', 'class': 'formField', 'autocomplete':'off'}
        )
    )

    email = forms.EmailField(
        widget = forms.EmailInput(
            attrs = {'placeholder': 'E-mail', 'class': 'formField', 'autocomplete':'off'}
        )
    )

    phone_number = forms.CharField(
        min_length=11,
        max_length=15,
        widget = forms.TextInput(
            attrs = {'placeholder': 'Телефон', 'class': 'formField', 'autocomplete':'off'}
        )
    )

    message = forms.CharField(
        min_length = 10,
        max_length = 500,
        widget = forms.Textarea(
            attrs = {'placeholder': 'Текст вашего сообщения', 'class': 'formField', 'autocomplete':'off'}
        )
    )
