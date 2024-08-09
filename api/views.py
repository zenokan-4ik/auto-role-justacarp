from .models import User
from django.http import HttpResponse

def success(request):
    payment_id = request.POST.get("payment_id")
    discord_id = request.POST.get("custom_fields")[0]
    nickname = request.POST.get("customer")
    users = User.objects.all()
    if len(users) != 0:
        for i in users:
            if i.get_nickname() != nickname:
                new = User(nickname=nickname, discord=discord_id)
                new.add_payment(payment_id)
                new.save()
            else:
                i.add_payment(payment_id)

def check(request):
    discords = [i.get_discord() for i in User.objects.all()]
    return HttpResponse('#$#'.join(discords))