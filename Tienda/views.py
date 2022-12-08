from django.shortcuts import redirect, render
from django.views.generic import View
from Inventario.models import Producto,Queja
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.hashers import make_password


class HomeView(View):
    def get(self,request,*args, **kwargs):
        productos = Producto.objects.all()
        return render(request, "index.html",{"productos":productos})

class QuejaView(View):
    def get(self,request,*args, **kwargs):
        return render(request, "crear-sug.html")

    def post(self,request,*args, **kwargs):
        x = Queja.objects.create(asunto=request.POST["asunto"],queja=request.POST["queja"],usuario=request.POST['usuario'])
        x.save()
        return redirect("/")
        

# class CrearUsuario(View):
#     def get(self,request,*args, **kwargs):
#         usuarios = Usuario.objects.all()

#         lista_users = []
#         for i in usuarios:
#             lista_users.append(i.username)
#         return render(request, "crear-usuario.html",{'lista_users':lista_users})

#     def post(self,request,*args, **kwargs):
#         usuarios = Usuario.objects.all()
#         lista_users = []
#         for i in usuarios:
#             lista_users.append(i.username)

#         if request.POST["usuario"] in lista_users:
#             return render(request,"crear-usuario.html",{'msg':"El nombre de usuario ya existe"})

#         else:
#             nombre = request.POST["nombre"]
#             apellidos = request.POST["apellidos"]
#             usuario = request.POST["usuario"]
#             telefono=request.POST["telefono"]
#             clave=request.POST["clave"]
#             new_usuario = Usuario.objects.create(first_name=nombre,last_name=apellidos,username=usuario,telefono=telefono,password=clave)
#             new_usuario.save()
#             new_usuario.password = make_password(new_usuario.password)
#             new_usuario.save()

#             return redirect("/",{"usuarios":usuarios})

# def EliminarUsuario(request,pk):
#     usuarios = Usuario.objects.all()
#     usuario = Usuario.objects.get(pk=pk)
#     usuario.delete()
#     return redirect("/",{"usuarios":usuarios})

# class EditarUsuario(View):
#     def get(self,request,pk,*args, **kwargs):
#         usuario = Usuario.objects.get(pk=pk)
#         return render(request, "editar-usuario.html",{'usuario':usuario})

#     def post(self,request,pk,*args, **kwargs):
#         usuarios = Usuario.objects.all()
#         usuario = Usuario.objects.get(pk=pk)
#         lista_users = []
#         for i in usuarios:
#             if i != usuario:
#                 lista_users.append(i.username)

#         if request.POST["usuario"] in lista_users:
#             return render(request,"editar-usuario.html",{'msg':"El nombre de usuario ya existe","usuarios":usuario})

#         else:
#             nombre = request.POST["nombre"]
#             apellidos = request.POST["apellidos"]
#             username = request.POST["usuario"]
#             telefono=request.POST["telefono"]
#             clave=request.POST["clave"]
#             usuario = Usuario.objects.get(pk=pk)
#             usuario.first_name=nombre
#             usuario.last_name=apellidos
#             usuario.telefono=telefono
#             usuario.username=username
#             usuario.password=clave
#             usuario.password = make_password(usuario.password)
#             usuario.save()

#             return redirect("/",{"usuarios":usuario})

# class Ventas(View):
#     def get(self,request,*args, **kwargs):
#         ventas = Venta.objects.all
#         return render(request,"ventas.html",{"ventas":ventas})

# class CrearVenta(View):
#     def get(self,request,*args, **kwargs):
#         return render(request, "crear-venta.html")

#     def post(self,request,*args, **kwargs):
#         nombre = request.POST['nombre']
#         cantidad = request.POST['cantidad']
#         importe = request.POST['importe']
#         venta = Venta.objects.create(nombre_producto=nombre,cantidad=cantidad,importe=importe)
#         venta.save()
#         return redirect("/ventas")

# def EliminarVenta(request,pk):
#     venta = Venta.objects.get(pk=pk)
#     venta.delete()
#     return redirect("/ventas")

# class EditarVenta(View):
#     def get(self,request,pk,*args, **kwargs):
#         venta = Venta.objects.get(pk=pk)
#         return render(request, "editar-venta.html",{"venta":venta})

#     def post(self,request,pk,*args, **kwargs):
#         venta = Venta.objects.get(pk=pk)
#         nombre = request.POST['nombre']
#         cantidad = request.POST['cantidad']
#         importe = request.POST['importe']
#         venta.nombre_producto=nombre
#         venta.cantidad=cantidad
#         venta.importe=importe
#         venta.save()
#         return redirect("/ventas")

