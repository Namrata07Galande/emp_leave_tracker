from django import forms
from .models import employee,emp_leave,holiday

class empform(forms.ModelForm):
   class Meta:
      model=employee
      fields="__all__"

class leaveform(forms.ModelForm):
   class Meta:
      model=emp_leave
      fields="__all__"

class holidayform(forms.ModelForm):
   class Meta:
      model=holiday
      fields="__all__"