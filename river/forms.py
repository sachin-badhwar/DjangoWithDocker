from django import forms
class HolidayTimeForm(forms.Form):
    CheckIn = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker',
                                    'placeholder':'Check In'
                                }))
    CheckOut = forms.DateField(widget=forms.TextInput(attrs=
                                {
                                    'class':'datepicker',
                                    'placeholder':'Check Out'
                                }))                            
    Children = forms.IntegerField(widget=forms.TextInput(attrs = {
        'placeholder':'Children'
    }))
    Room = forms.IntegerField(widget=forms.TextInput(attrs = {
        'placeholder':'Room'
    })) 