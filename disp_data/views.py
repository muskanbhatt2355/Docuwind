from django.shortcuts import render
from django.http import HttpResponse
from disp_data.models import Student3
from . import script1
#from script1 import first_name,start_time,phone_no,res_id

# Create your views here.
def button(request):
    return render(request,'button.html')



'''def disp_home(request):
    data = Student.objects.all()

    stu = {
        "student_number": data
    }

    return render(request, 'disp_data/data.html', context = stu)
    #return render_to_response("login/profile.html", stu)

from django.shortcuts import render
from .models import Student    # Student is the model class defined in models.py'''

# Assuming the data to be entered is presnet in these lists
'''stud_name = ['Aman', 'Vijay']
stud_age = [13, 12]
stud_marks = [20, 22]

first_name =[]
start_time = []
phone_no = []
res_id = []'''

def my_view(request, *args, **kwargs):

    # Iterate through all the data items
    test_result = Student3.objects.all();
    if len(test_result)==0:
        for i in range(len(script1.first_name)):
        # Insert in the database
            Student3.objects.create(firstname = script1.first_name[i], start_time = script1.start_time[i], phone_no = script1.phone_no[i], res_id = script1.res_id[i])


    # Getting all the stuff from database
    query_results = Student3.objects.all();

    # Creating a dictionary to pass as an argument
    context = { 'query_results' : query_results }

    # Returning the rendered html
    return render(request, "disp_data/data.html", context)
