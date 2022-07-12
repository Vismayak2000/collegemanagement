from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *


# Create your views here.

def Index(request):
    return render(request,"user/index.html")


def Admin_Home(request):
    if not request.user.is_staff:
        return redirect('LoginSignUp_Page')
    return render(request,'admin/adminhome.html')


def Course_Page(request):
    return render(request,'admin/addcourse.html')


def AddCourse(request):
    if request.method == 'POST':
        coursename=request.POST['coursename']
        coursefees=request.POST['coursefees']
        data = CourseModel(Course_Name=coursename,Course_Fees=coursefees)
        data.save()
        return redirect('Index')

def LoginSignUp_Page(request):
    courses=CourseModel.objects.all()
    context={'course':courses}
    return render(request,'user/login&signup.html',context)


def Teacher_SignUp(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        username=request.POST['username']
        address=request.POST['address']
        email=request.POST['email']
        gender=request.POST['gender']
        course=request.POST['select']
        age=request.POST['age']
        password=request.POST['password']
        confirm_password=request.POST['confirmpassword']
        photo=request.FILES.get('photo')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'This Username Already Exists!')
                return redirect('LoginSignUp_Page')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'This Email Already Exists!')
                return redirect('LoginSignUp_Page')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=username,password=password)
                user.save()
                messages.success(request, 'SuccessFully Registered')
                print("Successed...")

                data=User.objects.get(id=user.id)
                crsdata=CourseModel.objects.get(id=course)
                user_data=Usermember(Tr_Address=address,Tr_gender=gender,Tr_Age=age,Tr_image=photo,Teacher=data,Course=crsdata)
                user_data.save()
                messages.success(request, 'SuccessFully Registered')
                print('success..')
                return redirect('LoginSignUp_Page')

 
        else:
            print("Password is not Matching.. ") 
            return redirect('LoginSignUp_Page') 
    else:
        return render(request,'login&signup.html')


def Teacher_Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('Admin_Home')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('Index')
        else: 
            return redirect('Teacher_Login')
    else:
        return redirect('Admin_Home')
        

def Teacher_LogOut(request):           
    if request.user.is_authenticated:    
        auth.logout(request)
    return redirect('Index')


def Student_Page(request):
    courses=CourseModel.objects.all()
    context={'courses':courses}
    return render(request,'admin/addstudent.html',context)


def Add_Student(request):
    if request.method=='POST':
        stdname=request.POST['stdname']
        stdaddress=request.POST['stdaddress']
        stdage=request.POST['stdage']
        select=request.POST['select']
        course=CourseModel.objects.get(id=select)
        data = StudentModel(Stud_Name=stdname,Stud_Address=stdaddress,Stud_Age=stdage,Course=course)
        data.save()
        return redirect('Index')


def Student_Details(request):
    if not request.user.is_staff:
        return redirect('LoginSignUp_Page')
    student_detail = StudentModel.objects.all()
    return render(request,'admin/studentdeatil.html',{'student':student_detail})


def Course_Details(request):
    if not request.user.is_staff:
        return redirect('LoginSignUp_Page')
    course=CourseModel.objects.all()
    return render(request,'admin/coursedetails.html',{'crsdata':course,})



def Teacher_Details(request):
    if not request.user.is_staff:
        return redirect('LoginSignUp_Page')
    teacher_detail = Usermember.objects.all()
    return render(request,'admin/teacherdetails.html',{'teacher':teacher_detail})

def Delete_Teacher(request,id):
    if not request.user.is_staff:
        return redirect('LoginSignUp_Page')
    tchr = Usermember.objects.get(id=id)
    tchr.delete()
    return redirect('Teacher_Details')

def Profile(request):
    users=Usermember.objects.get(Teacher=request.user)
    context={"user":users}
    return render(request,'user/profile.html',context)


def Edit_Page(request):
    teacher=Usermember.objects.get(Teacher=request.user)
    return render(request,"user/editprofile.html",{'edit':teacher})

def Edit_Profile(request):
    if request.method=='POST':
        tcrdata = Usermember.objects.get(Teacher=request.user)
        tcrdata.first_name = request.POST.get('firstname')
        tcrdata.last_name = request.POST.get('lastname')
        tcrdata.username = request.POST.get('username')
        tcrdata.email = request.POST.get('email')
        tcrdata.Teacher_Address = request.POST.get('address')
        tcrdata.Teacher_Gender = request.POST.get('gender')
        tcrdata.Teacher_age = request.POST.get('age')
        tcrdata.Teacher_Photo =request.POST.get('photo')
        tcrdata.save()
        return redirect('Profile')
    return render(request, 'user/editprofile.html')


















# to edit teacher personal profile
# def Edit_Profile(request,pk):
#     if request.method=='POST':
#         tdata = TeacherModel.objects.all(id=pk)
#         tdata.first_name = request.POST.get('firstname')
#         tdata.last_name = request.POST.get('lastname')
#         tdata.username = request.POST.get('username')
#         tdata.email = request.POST.get('email')
#         tdata.Teacher_Address = request.POST.get('address')
#         tdata.Teacher_Gender = request.POST.get('gender')
#         tdata.Teacher_age = request.POST.get('age')
#         tdata.Teacher_Photo =request.POST.get('photo')
#         tdata.save()
#         return redirect('Profile')
#     return render(request, 'user/editprofile.html')

# # to load teacher profile edit
# def Edit_Profile(request,pk):
#     details=TeacherModel.objects.get(id=pk)
#     return render(request,'user/editprofile.html',{'details':details})


























    #     else:
    #         return redirect('Teacher_Login_SignUp_Page')
    #     return redirect('')  
    # else:
    #     return redirect('Teacher_Login_SignUp_Page')
    
    # return render(request,"user/login&signup.html")











  
