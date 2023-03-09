from django.shortcuts import render
from django.http import HttpResponse
from emp.forms import empform,leaveform,holidayform

# Create your views here.
def emp(Request):
    form = empform()
    if Request.method == 'POST':
       form = empform(Request.POST)
       if form.is_valid():
           form.save(commit=True)
           return HttpResponse("<h1> Record Inserted Successfully</h1>")
       else:
           print("Error form Invalid")
    return render(Request, 'emp/emp.html', {'form': form})


def leave(Request):
    form = leaveform()
    if Request.method == 'POST':
       form = leaveform(Request.POST)
       if form.is_valid():
           form.save(commit=True)
           return HttpResponse("<h1> Record Inserted Successfully</h1>")
       else:
           print("Error form Invalid")
    return render(Request, 'emp/emp_leave.html', {'form': form})



def holiday(Request):
    form = holidayform()
    if Request.method == 'POST':
       form = holidayform(Request.POST)
       if form.is_valid():
           form.save(commit=True)
           return HttpResponse("<h1> Record Inserted Successfully</h1>")
       else:
           print("Error form Invalid")
    return render(Request, 'emp/holiday.html', {'form': form})
