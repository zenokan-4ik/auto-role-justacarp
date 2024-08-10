from django.db import models


class User(models.Model):
    nickname = models.CharField(name='nickname', max_length=64)
    discord = models.CharField(name='discord', max_length=128)
    payments = models.JSONField(name='payments', default={'0': '0'})

    def __str__(self):
        return self.nickname

    def add_payment(self, payment):
        last_payment_id = max(list(map(int, self.payments.keys()))) if len(
            self.payments.keys()) != 0 else 0
        self.payments.update({str(int(last_payment_id) + 1): payment})

    def get_discord(self):
        """
        :return: discord id with @
        """
        return str(self.discord) if self.discord[0] == '@' else '@' + str(
            self.discord)

    def get_nickname(self):
        """
        :return: nickname
        """
        return self.nickname
