import logging
import traceback
from contextlib import redirect_stderr
from logging import Logger

from book.models import Book, Employee
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render

logger = logging.getLogger("first") 

# Create your views here.

# There are 2 types of view function based and class based
# (base url:http://127.0.0.1:8000/)

#this function is for homepage, request is a default arg.
def homepage(request):
    logger.info("In Homepage View")
    print(request.method)
    # print(request.GET)
    # print(request.POST)

    name = request.POST.get("bname")
    price = request.POST.get("bprice")
    qty = request.POST.get("bqty")

    if request.method == "POST":
        if not request.POST.get("bid"):     #This is for add new data 
            book_name = name
            book_price = price
            book_qty = qty
            # print(book_name, book_price, book_qty,type(book_price))
            Book.objects.create(name=book_name, price=book_price, qty=book_qty, Is_active=True)
            return redirect("homepage")
        
        else:
            logger.info(request.POST)
            bid = request.POST.get("bid")          #If id exist then we will edit the data
            try:
                book_obj = Book.objects.get(id=bid)
            # except Book.DoesNotExist as err_msg:
            #     print(err_msg) 
            except Exception as msg:
                logger.error(f"In Exceptin {msg}")

            book_obj.name = name
            book_obj.price = price
            book_obj.qty = qty
            book_obj.Is_active = True
            book_obj.save()
            return redirect("show_all_books")    
            

    elif request.method == "GET":
        # print(request.build_absolute_uri())
        
        return render(request, template_name="home.html")    
        # return HttpResponse("<h2><i>Site under maintainance<i></h2>")

def show_all_books(request):  #This function show all books (read all operation, first crud operation Read)
    all_books = Book.objects.all()   #we are fetching all data
    logger.info(all_books)
    data = {"books": all_books}
    return render(request,"show_books.html", context=data)


def edit_data(request, id):   #function to edit data
    book = Book.objects.get(id=id)
    return render(request, template_name="home.html", context={"single_book": book})

# delete single data permenantaly
def delete_data(request, id):
    if request.method == "POST":
        try:                              #handlining error if id not present.                              
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()        #Here we are displaying detail error msg
            return HttpResponse(f"Book does not exist gor given ID {id}..!!!!")   
        else:    
            book.delete()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request Method : {request.method} not allowed. only POST method is allowed")    

#Here we are deleting data but in backend we are just deactive it
def soft_delete_data(request,id):
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()
            return HttpResponse(f"Book does not exist!!!!")    
        else:
            book.Is_active = False
            book.save()
        # return redirect("show_all_books")
        return redirect('show_soft_del_books')
    else:
        return HttpResponse(f"Request Method : {request.method} not allowed. only POST method is allowed")  

#this function is for restore soft deleted data.
def restore_data(request, id):
    if request.method == "POST":
        try:
            book = Book.objects.get(id=id)   
        except Book.DoesNotExist as err_msg:
            traceback.print_exc()
            return HttpResponse(f"Book does not found")
        else:
            book.Is_active = True
            book.save()
        return redirect("show_all_books")
    else:
        return HttpResponse(f"Request Method : {request.method} not allowed. only POST method is allowed")                              

#when we will deactivate any book this function we show all soft deleted data
def show_soft_del_books(request):  #This function show all books (read all operation first crud operation Read)
    all_soft_del_books = Book.objects.all().filter(Is_active=False)
    data = {"books": all_soft_del_books}
    return render(request,"deleted_books.html", context=data)

#this function will delete all data permenantly
def delete_all(request):
    Book.objects.all().delete()
    return redirect("homepage")

  
#Home page is for addding books
#Show all Books will show all books active book soft delete button is visible inactive books disable
#Deleted books page will show all deleted book with restore button

# from django.shortcuts import render



from book.forms import AddressForm, BookForm


def form_home(request):     #This is function based viewe
    if request.method == "POST":
        print("In POST request")
        form = BookForm(request.POST)
        # print(form.isValid())
        
        if form.is_valid():
            print(form.cleaned_data["name"])
            form.save()
            messages.success(request, 'Data saved successfully!!!!!') 
            messages.info(request, 'Go to home page') 
        else:
            messages.error(request, 'Invalide data pls provide valid data')    
        return redirect("form_home")    
        

    elif request.method == "GET":
        print("In GET rquest")
        context = {"form": BookForm()}    #for address we can pass AddressForm 
        return render(request, "form_home.html", context=context)

    else:
        return HttpResponse("Invalid HTTP Method", status=405)
    


    #Different HTTP methods and purpose
    # GET :is used to retrieve or get the information from the given server using a given URL(Read)
    # POST: Post is used for sending data
    # PUT :update(send all data)
    # PATCH: partial data
    # DELETE:used to delete a resource specified     

from django.views import View


class Homepage(View):
    def get(self, request):
        print("In get request")
        return HttpResponse("In GET")

    def post(self, request):
        print(request.POST)
        print("In post ")
        return HttpResponse("In POST", status=201)

    def delete(self, request):
        print("In delete")
        return HttpResponse("In Delete")

    def patch(self, request):
        print("In patch")
        return HttpResponse("In patch")

    def put(self, request):
        print("In put")
        return HttpResponse("in put")



from django.views.generic.base import RedirectView, TemplateView


class CBVTemplateView(RedirectView):
    url = "homepage"

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import UpdateView 
from django.views.generic.edit import DeleteView 
from django.urls import reverse, reverse_lazy 

# CRUD operations
# Steps:Create Model-Database-migrations-Modelform-view-url-template

class EmployeeCreate(CreateView):  
    model = Employee  
    # success_url = "http://127.0.0.1:8000/emp-gcreate/"
    success_url = reverse_lazy("EmployeeCreate") #For dynamic ineraction we will use reverse lazy
  
    fields = '__all__' 

  
class EmployeeRetrieve(ListView):  
    model = Employee  
  
class EmployeeDetail(DetailView):  
    model = Employee     
 
class EmployeeUpdate(UpdateView):  
    model = Employee     
    success_url = "http://127.0.0.1:8000/emp-retr/"
    fields = '__all__'   

   
class EmployeeDelete(DeleteView):  
    model = Employee   
    success_url = "http://127.0.0.1:8000/emp-retr/"      