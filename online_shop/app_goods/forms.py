from app_users.models import UserProfile
from django import forms

DELIVERY_METHODS = [('1', 'Обычная доставка'), ('2', 'Экспресс доставка')]
PAYMENT_METHODS = [('1', 'Онлайн картой'), ('2', 'Онлайн со случайного чужого счета')]


class OrderForm(forms.Form):
    full_name = forms.CharField(disabled=True, max_length=100, required=False, label='ФИО')
    email = forms.EmailField(disabled=True, label='E-mail')
    phone_number = forms.CharField(disabled=True, label='Номер телефона', max_length=13)
    city = forms.CharField(required=True, label='Город', max_length=36)
    address = forms.CharField(required=True, label='Адрес', max_length=150)
    delivery_method = forms.ChoiceField(widget=forms.RadioSelect, choices=DELIVERY_METHODS, required=True)
    payment_method = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_METHODS, required=True)

    def __init__(self, post=None, *args, **kwargs):
        userprofile: UserProfile = kwargs['userprofile']
        self.base_fields['full_name'].initial = userprofile.get_full_name()
        self.base_fields['email'].initial = userprofile.user.email
        self.base_fields['phone_number'].initial = userprofile.phone_number
        if post is not None:
            self.base_fields['delivery_method'].initial = DELIVERY_METHODS[int(post['delivery_method']) - 1]
            self.base_fields['payment_method'].initial = PAYMENT_METHODS[int(post['payment_method']) - 1]
            self.base_fields['city'].initial = post['city']
            self.base_fields['address'].initial = post['address']
        else:
            self.base_fields['delivery_method'].initial = DELIVERY_METHODS[0]
            self.base_fields['payment_method'].initial = PAYMENT_METHODS[0]
            self.base_fields['city'].initial = ''
            self.base_fields['address'].initial = ''
        super(OrderForm, self).__init__()

    def save(self):
        pass

    def is_valid(self):
        # TODO: сделать логику валидации формы в зависимости от шага
        super(OrderForm, self).is_valid()