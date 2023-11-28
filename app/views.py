from django.shortcuts import render

# template folder, dictionary key value pair passing in render method.

def my_view(request):
    my_data = {
        'Name': 'Ganesh',
        'Age': 25,
    }  
    context= {'my_data':my_data}
    return render(request, 'my_template.html', context )


