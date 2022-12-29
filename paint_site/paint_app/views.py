from django.shortcuts import render
from django.views import View

from paint_app.forms import ColorPickerForm
# Create your views here.

class ColorPickerView(View):
    def get(self, request):
        color_form = ColorPickerForm()

        red_value = 255
        green_value = 255
        blue_value = 255 

    
        html_data = {
            'form': color_form,
            'red': red_value,
            'green': green_value,
            'blue': blue_value,
        }

        return render(
            request=request, 
            template_name='color_picker.html', 
            context=html_data,
        )

    def post(self, request):
        color_form = ColorPickerForm()

        red_value = int(request.POST['red_amount'])
        green_value = int(request.POST['green_amount'])
        blue_value = int(request.POST['blue_amount'])

# The dictionary below is the meta-data being sent to the html file (coming from form)
        html_data = {
            'form': color_form,
            'red': red_value,
            'green': green_value,
            'blue': blue_value,    
        }

        return render(
            request=request, 
            template_name='color_picker.html', 
            context=html_data,
        )




        