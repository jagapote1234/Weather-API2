from django import forms
from django.db import models

class CityChoices(models.TextChoices):
    OSAKA = 'osaka', '大阪府',
    HYOGO = 'hyogo', '兵庫県',
    NARA = 'nara', '奈良県',
    WAKAYAMA = 'wakayama', '和歌山県',
    KYOTO = 'kyoto', '京都府',
    SIGA = 'siga', '滋賀県',
    MIE = 'mie', '三重県',

class CityForm(forms.Form):
    regin = forms.fields.ChoiceField(
        choices = CityChoices.choices,
        required = True,
        label = '地域'
    )