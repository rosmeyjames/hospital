from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from doctorapp.forms import departmentform, medicineform, positionform, staffform, scheduleform, labtestform, \
    diaganosisform
from doctorapp.models import medicine, position, staff, registeration, schedule, prescription
from django.contrib.auth import authenticate, login as auth_login

def index(request):
    return  render(request,'doctor/index.html')
def createposition(request):
    if request.method=='POST':
        form=positionform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listposition')

    else:
        form=positionform()
    return render(request,'admin/position.html',{'form':form})
def createschedule(request):
    if request.method=='POST':
        form=scheduleform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'schedule create')
            return redirect('viewschedule')

    else:
        form=scheduleform(request.FILES)
    return render(request,'doctor/docschedule.html',{'form':form})
def viewschedule(request):
    sch = schedule.objects.all()

    return render(request,'doctor/viewschedule.html',{'sch':sch})
def updateschedule(request,schid):
    schd = schedule.objects.get(id=schid)
    if request.method == 'POST':
        form = scheduleform(request.POST,files=request.FILES ,instance=schd)
        if form.is_valid():
            form.save()
            messages.success(request,'success')
            return redirect('viewschedule')
    else:
        form = scheduleform(instance=schd)
    return render(request, 'doctor/updateschedule.html', {'form': form, 'schd': schd})
def deleteschedule(request,schid):
    schd = schedule.objects.get(id=schid)

    if request.method == 'POST':
        schd.delete()
        return redirect('viewschedule')

    return render(request, 'doctor/deleteschedule.html', {'schd': schd})
def positionlist(request):
    meds = position.objects.all()
    return render(request,'admin/positionlist.html',{'meds':meds})
def deleteposition(request,posid):
    meds = position.objects.get(id=posid)
    if request.method=='POST':
        meds.delete()
        return redirect('listposition')

    return render(request,'admin/deleteposition.html',{'meds':meds})
def updateposition(request,posid):
    meds = position.objects.get(id=posid)
    if request.method == 'POST':
        form = positionform(request.POST, instance=meds)
        if form.is_valid():
            form.save()
            return redirect('listposition')
    else:
        form = positionform(instance=meds)
    return render(request, 'admin/updateposition.html', {'form': form, 'meds': meds})
def createdepartment(request):
    if request.method=='POST':
        form=departmentform(request.POST)
        if form.is_valid():
                form.save()
    else:
        form=departmentform()
    return render(request,'admin/department.html',{'form':form})
def createmedicine(request):


    if request.method=='POST':
        form=medicineform(request.POST)
        if form.is_valid():
                form.save()
    else:
        form=medicineform()
    return render(request,'doctor/newmedicine.html',{'form':form})
def medicinelist(request):
    meds = medicine.objects.all()
    return render(request,'doctor/medicinelist.html',{'meds':meds})
def stafflist(request):
    meds = staff.objects.all()
    return render(request,'doctor/stafflist.html',{'meds':meds})
def updatemedicine(request,medid):
    meds = medicine.objects.get(id=medid)
    if request.method=='POST':
        form=medicineform(request.POST,instance=meds)
        if form.is_valid():
            form.save()
            return redirect('medicinelist')
    else:
        form = medicineform(instance=meds)
    return render(request, 'doctor/updatemedicine.html', {'form': form,'meds':meds})
def updatestaff(request,sid):
    s = staff.objects.get(id=sid)
    if request.method=='POST':
        form=staffform(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('stafflist')
    else:
        form = staffform(instance=s)
    return render(request, 'admin/updatestaff.html', {'form': form,'s':s})
def deletestaff(request,sid):
    meds = staff.objects.get(id=sid)
    if request.method=='POST':
        meds.delete()
        return redirect('stafflist')

    return render(request,'doctor/deletestaff.html',{'meds':meds})
def deletemedicine(request,medid):
    meds = medicine.objects.get(id=medid)
    if request.method=='POST':
        meds.delete()
        return redirect('medicinelist')

    return render(request,'doctor/deletemedicine.html',{'meds':meds})
# def addstaff(request):
#     staffpositions = position.objects.all()
#     if request.method == 'POST':
#         username=request.POST.get('username')
#         posn=request.POST.get('posn')
#         id = position.objects.get(job=posn).id
#
#         if staff.objects.filter(username=username).exists():
#             messages.info(request, 'This username already exists')
#         else:
#             acd=staff(username=username,staffposition_id=id)
#             acd.save()
#     return render(request,'admin/addstaff.html',{'staffpositions':staffpositions})
def addstaff(request):
    staffpositions = position.objects.all()

    if request.method == 'POST':
        # form = staffform(request.POST)
        # if form.is_valid():
        #   username = form.cleaned_data['username']
        username = request.POST.get('username')
        # staffposition_id = form.cleaned_data['staffpositions1']
        posn = request.POST.get('staffpositions1')
        if staff.objects.filter(username=username).exists():
            messages.info(request, 'This username already exists')
        else:
            acd = staff(username=username, staffposition_id=posn)
            # acd = staff(username=username, staffposition_id=staffposition_id)
            acd.save()
            messages.success(request, 'Staff member added successfully')
    return render(request,'admin/addstaff.html',{'staffpositions': staffpositions })

    # return render(request, 'admin/addstaff.html', {'form': form, 'staffpositions': staffpositions})

def registerdetails(request):
    if request.method=='POST':
        # user_cart, created = academicdetails.objects.get_or_create(user=request.user)
        name=request.POST.get('name')
        age=request.POST.get('age')
        dob=request.POST.get('dob')
        phno=request.POST.get('phno')
        adrs=request.POST.get('adrs')

        image = request.FILES.get('image')
        username=request.POST.get('username')
        email = request.POST.get('email')
        pwd=request.POST.get('password')

        cpwd=request.POST.get('cpassword')

        if pwd == cpwd :
            print(pwd)
            print(cpwd)

            if staff.objects.filter(username=username).exists():
                if registeration.objects.filter(mail=email).exists():
                    messages.info(request, 'This email already exists')
                    return redirect('registeration')


                else:

                    type1 = staff.objects.get(username=username).staffposition_id
                    print(type1)
                    acd = registeration(name=name, age=age, dob=dob, phonenum=phno, adrs=adrs, image=image,
                                    username=username, mail=email, pwd=pwd, usertype=type1)
                    acd.save()
                    return redirect('login')
            else:
                acd = registeration( name=name, age=age, dob=dob, phonenum=phno, adrs=adrs, image=image,
                                username=username, mail=email, pwd=pwd, usertype='user')
                acd.save()
                return redirect('login')

        else:
            messages.info(request, 'password mismatch')
    return render(request, 'admin/registerationform.html')
# def newlogin(request):
#     if request.method == 'POST':
#          # username = request.POST['username']
#          # password = request.POST
#          username = request.POST.get('username')
#          password = request.POST.get('password')
#          type1 = registeration.objects.get(username=username).usertype
#          # ustype=position.objects.get(id=type1).job
#          # user_exists = logintable.objects.filter(username=username,password=password,usertype='user').exists()
#          user_exists = registeration.objects.filter(username=username, pwd=password, usertype=type1).exists()
#          user_exists1 = staff.objects.filter(username=username).exists()
#          # print(username)
#          # print(password)
#
#          try:
#              if user_exists is not None:
#                  userdetails = registeration.objects.get(username=username, pwd=password)
#                  user_name = userdetails.username
#
#                  # if user_exists1 is not None:
#                  if user_exists1 is True:
#                     userdetails = staff.objects.get(username=username)
#                     user_name=userdetails.username
#                     # usertype=userdetails.usertype
#                     ustype=position.objects.get(id=type1).job
#
#                     # print(password)
#
#                     if ustype == 'doctor':
#                          request.session['username']=user_name
#
#                          return redirect('index')
#                     else:
#                          request.session['username'] = user_name
#                          return redirect('adminindex')
#
#                  else:
#
#                      request.session['username']=user_name
#                      print (request.user)
#                      return redirect('userindex')
#              else:
#                  messages.error(request,"failure")
#
#          except registeration.DoesNotExist:
#
#                 messages.error(request,'invalid')
#                 # return redirect('userindex')
#                 # return render(request,'doctor/login.html')
#     return render(request, 'doctor/login.html')
#
# vi
# from django.contrib import messages
# from django.shortcuts import redirect, render
# from .models import registeration, staff, position
#
# def newlogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         try:
#             user = registeration.objects.get(username=username, pwd=password)
#             if user:
#                 # Manually set the session data
#                 request.session['username'] = user.username
#                 request.session['usertype'] = user.usertype
#                 request.session['user_id'] = user.id  # Add user ID to session
#
#                 # Debugging information
#                 print(f"User authenticated: {user.username}")
#                 print(f"Session data: {request.session.items()}")
#
#                 type1 = user.usertype
#                 user_exists1 = staff.objects.filter(username=username).exists()
#
#                 if user_exists1:
#                     ustype = position.objects.get(id=type1).job
#                     if ustype == 'doctor':
#                         return redirect('index')
#                     else:
#                         return redirect('adminindex')
#                 else:
#                     return redirect('userindex')
#             else:
#                 messages.error(request, "Invalid username or password")
#         except registeration.DoesNotExist:
#             messages.error(request, "Invalid username or password")
#     return render(request, 'doctor/login.html')


from django.contrib import messages, auth
from django.shortcuts import redirect, render
from .models import registeration, staff, position

def newlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            request.session['username'] = user.username
            request.session['usertype'] = user.usertype
            request.session['user_id'] = user.id

            # Debugging information
            print(f"User authenticated: {user.username}")
            print(f"Session data: {request.session.items()}")
            request.session.save()

            # type1 = user.usertype
            user_exists1 = staff.objects.filter(username=username).exists()

            if user_exists1:
                # ustype = position.objects.get(id=type1).
                staff_member = staff.objects.get(username=username)
                ustype = staff_member.staffposition.job
                if ustype == 'doctor':

                    return redirect('index')
                else:
                    return redirect('adminindex')
            else:
                return redirect('userindex')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'doctor/login.html')
def doc_presc(request):
    meds = medicine.objects.all()
    if request.method == 'POST':
        name1=request.POST.get('name')
        id=registeration.objects.get(name=name1).id
        med=request.POST.get('medicine')
        det=request.POST.get('details')
        num=request.POST.get('number')
        item=prescription(presc_name_id = id,presc_med_id=med,presc_det=det,presc_num=num)
        item.save()
        messages.success(request, 'medicine prescribed')
    return render(request,'doctor/prescriptionform.html',{'meds':meds})
def createnewlabtest(request):
    if request.method=='POST':
        form=labtestform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('labtest')

    else:
        form=labtestform()
    return render(request,'doctor/labtest.html',{'form':form})
def usercreatediaganosis(request):
    if request.method=='POST':
        form=diaganosisform(request.POST)
        if form.is_valid():
            form.save()
            messages.succcess(request,'success')
            return redirect('diaganosis')

    else:
        form=diaganosisform()
    return render(request,'doctor/diaganosis.html',{'form':form})