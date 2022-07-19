from django.http import JsonResponse
from django.shortcuts import render
from django.core import serializers
from .models import Family, Invitee
from .forms import InviteeForm


def invitee_confirmation(request):
    families = Family.objects.all()
    guests = Invitee.objects.all()
    form = InviteeForm()

    context = {
        'families': families,
        'guests': guests,
        'form': form,
    }

    return render(request, "guest.html", context)


def getMembers(request):
    # request should be ajax and method should be GET.
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        family_id = request.GET.get("family", None)
        # check for the nick name in the database.
        if family_id != "blank":
            if Family.objects.filter(id=family_id).exists():
                # if nick_name found return not valid new friend
                member_results = list(Invitee.objects.filter(family=family_id).values("id", "name", "surname"))

                return JsonResponse({"member_results": member_results}, status=200)
            else:
                # if nick_name not found, then user can create a new friend.
                return JsonResponse({"valid": False}, status=200)

    return JsonResponse({}, status=400)

def getMemberInfo(request):
    if request.is_ajax and request.method == "GET":
        # get the nick name from the client side.
        member_id = request.GET.get("member", None)
        # check for the nick name in the database.
        if member_id != "blank":
            if Invitee.objects.filter(id=member_id).exists():
                # if nick_name found return not valid new friend
                member_info = list(Invitee.objects.filter(id=member_id).values("email", "language"))

                return JsonResponse({"member_info": member_info}, status=200)
            else:
                # if nick_name not found, then user can create a new friend.
                return JsonResponse({"valid": False}, status=200)

    return JsonResponse({}, status=400)

def postGuest(request):
    # request should be ajax and method should be GET.
    if request.method == 'POST':
        form = InviteeForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = InviteeForm()

    return render(request, 'guest.html', {'form': form})
