from .models import User
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def success(request):
    discord_id = request.POST.get("discordid")
    print(request.POST)
    # users = User.objects.all()
    # if len(users) != 0:
    #     for i in users:
    #         if i.get_nickname() != nickname:
    #             new = User(nickname=nickname, discord=discord_id)
    #             new.add_payment(payment_id)
    #             new.save()
    #         else:
    #             i.add_payment(payment_id)
    # print(nickname, discord_id)
    return HttpResponse("success")


def check(request):
    discords = [i.get_discord() for i in User.objects.all()]
    return HttpResponse('#$#'.join(discords))


def add(request):
    nickname = request.GET.get('nickname')
    discord = request.GET.get('discord')
    new = User(nickname=nickname, discord=discord)
    new.save()
    return HttpResponse('Success!')
