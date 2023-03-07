from django.shortcuts import render


def about(request):
    return render(request, 'about.html')


def blog(request):
    return render(request, 'blog.html')


def contact(request):
    return render(request, 'contact.html')


def detail(request):
    return render(request, 'detail.html')


def feature(request):
    return render(request, 'feature.html')


def index(request):
    return render(request, 'index.html')


def service(request):
    return render(request, 'service.html')


def team(request):
    return render(request, 'team.html')


def testimonial(request):
    return render(request, 'testimonial.html')

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        query = Student(name=name, email=email, age=age, gender=gender, country=country, city=city)
        query.save()
        return redirect("/")

        return render(request, 'index.html')

def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        update_info = Student.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.country = country
        update_info.city = city
        update_info.gender = gender
        update_info.save()

        return redirect("/")

    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)
