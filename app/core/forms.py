from django import forms

from .models import Bus


class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = [
            "bus_number",
            "brand",
            "no_of_seats",
            "trip",
            "duration",
            "conductor",
            "driver"
        ]
        widgets = {
            'bus_number': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter Bus Number"
                }
            ),
            'brand': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter The Brand"
                }
            ),
            'no_of_seats': forms.NumberInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter Number Of Seats"
                }
            ),
            'trip': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter Trip Name"
                }
            ),
            'duration':forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter Trip Duration (HH:MM:SS)"
                }
            ),
            'conductor': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter Conductor Name"
                }
            ),
            'driver': forms.TextInput(
                attrs={
                    'class': "form-control",
                    'placeholder': "Enter Driver Name"
                }
            ),
        }