from django import forms


class EndpointForm(forms.Form):
    endpoints = forms.BooleanField(required=False, label='Select your endpoint: All')
    hva = forms.BooleanField(required=False, label='Huis van Alijn')
    dmg = forms.BooleanField(required=False, label='Design Museum Gent')
    stam = forms.BooleanField(required=False, label='STAM')
    im = forms.BooleanField(required=False, label='Industriemuseum')
    ag = forms.BooleanField(required=False, label='Archief Gent')
    title = forms.BooleanField(required=False, label='Title')
    titlefilter = forms.CharField(required=False)
    description = forms.BooleanField(required=False)
    descriptionfilter = forms.CharField(required=False)
    image = forms.BooleanField(required=False)
    limit = forms.IntegerField(required=False, max_value=1000)
    objectname = forms.BooleanField(required=False)
    objectnamefilter = forms.CharField(required=False)
    associatie = forms.BooleanField(required=False)
    associatiefilter = forms.CharField(required=False)
    objectnumber = forms.BooleanField(required=False)
    objectnumberfilter = forms.CharField(required=False)
    vervaardiger = forms.BooleanField(required=False)
    vervaardigerfilter = forms.CharField(required=False)
    distinct = forms.BooleanField(required=False)
    count = forms.BooleanField(required=False)



