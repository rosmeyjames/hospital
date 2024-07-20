from django import forms
from .models import *
from .models import department

class departmentform(forms.ModelForm):
    class Meta:
        model=department
        fields='__all__'
class medicineform(forms.ModelForm):
    class Meta:
        model=medicine
        fields='__all__'
class positionform(forms.ModelForm):
    class Meta:
        model=position
        fields='__all__'
class staffform(forms.ModelForm):
    class Meta:
        model=staff
        fields='__all__'
    # staffposition = forms.ModelChoiceField(queryset=position.objects.all())

class scheduleform(forms.ModelForm):
    class Meta:
        model = schedule
        fields ='__all__'
class labtestform(forms.ModelForm):
    class Meta:
        model = labtest
        fields = '__all__'
class diaganosisform(forms.ModelForm):
    class Meta:
        model = userdiaganosis
        fields = '__all__'