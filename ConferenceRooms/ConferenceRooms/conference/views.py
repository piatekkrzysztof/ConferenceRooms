from datetime import datetime

from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from conference.models import Room,Reservation


# Create your views here.
def homepage(request):
    return render(request, 'home.html')

class AddNewRoom(View):

    def get(self, request):
        return render(request, 'NewRoom.html')

    def post(self, request):
        name = request.POST['name']
        cap = request.POST['cap']
        proj = request.POST['projector']
        try:
            Room.objects.create(name=name, capacity=cap, projector=proj)
            return redirect('/')
        except IntegrityError:
            error = "Sala o takiej nazwie już istnieje!"
            return render(request, 'NewRoomError.html',{'error':error})
        except ValueError:
            return render(request, 'NewRoomError.html')

class ShowRooms(View):
    def get(self, request):
        rooms=Room.objects.all()
        return render(request, 'allrooms.html',{'rooms':rooms})

class DeleteRoom(View):
    def get(self,request,id):
        room=Room.objects.get(id=id)
        room.delete()
        return redirect('/room/all/')

class EditRoom(View):

    def get(self,request,id):
        room=Room.objects.get(id=id)
        return render(request,'editroom.html',{'room':room})

    def post(self, request, id):
        name = request.POST['name']
        cap = request.POST['cap']
        proj = request.POST['projector']
        try:
            room=Room.objects.get(id=id)
            room.name=name
            room.capacity=cap
            room.projector=proj
            room.save()
            return redirect('/room/all/')
        except IntegrityError:
            error = "Sala o takiej nazwie już istnieje!"
            return render(request, 'NewRoomError.html',{'error':error})
        except ValueError:
            return render(request, 'NewRoomError.html')


class RoomReserve(View):
    def get(self,request,id):
        room = Room.objects.get(id=id)
        reservation = room.reservation_set.all()
        return render(request, 'NewReservation.html',{'reservation':reservation})

    def post(self,request,id):
        date = request.POST['date']
        com = request.POST['com']
        try:
            Reservation.objects.create(data=date, comment=com, room_id=Room.objects.get(id=id))
            return redirect('/room/all')
        except IntegrityError:
            error = "Sala o takiej nazwie już istnieje!"
            return render(request, 'Reservationerror.html',{'error':error})
        except ValueError:
            error = "Bledne dane!"
            return render(request, 'Reservationerror.html',{'error':error})

class RoomView(View):
    def get(self,request,id):
        room=Room.objects.get(id=id)
        reservation = room.reservation_set.all()
        return render(request, 'room.html', {'room': room, 'reservation':reservation})


class SearchRoom(View):
    def get(self, request):
        return render(request, 'search.html')

    def post(self,request):
        name = request.POST['name']
        cap = request.POST['cap']
        proj = request.POST['projector']
        try:
            rooms=Room.objects.filter(Q(name=name) | Q(capacity__gt=cap) | Q(projector=proj))
            return render(request, 'allrooms.html',{'rooms':rooms})
        except Exception:
            pass



class ShowRooms2(View):
    def get(self, request):
        rooms=Room.objects.all()
        return render(request, 'tabletest.html',{'rooms':rooms})










