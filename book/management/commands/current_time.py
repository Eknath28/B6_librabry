from django.core.management.base import BaseCommand
from django.utils import timezone
# from datetime import datetime

class Command(BaseCommand):
    help = 'Display current time'

    def handle(self, *args, **kwargs):
        # time = timezone.now().strftime('%X')
        time = timezone.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        self.stdout.write("Its now %s" % time)

        


# ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
# print(ind_time)