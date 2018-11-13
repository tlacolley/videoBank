from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from video_bank.models import MovieRent, Customer
from django.core.mail import EmailMessage

class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        movie_rent = MovieRent.objects.all()
        for movie in movie_rent:
            # return_date = movie.return_date
            now = timezone.now()
            checkout_date = movie.checkout_date
            estimate_rent_date = checkout_date + datetime.timedelta(days=7)
            movie_title = movie.movie
            if estimate_rent_date > now:
                customer = movie.customer
                customer_mail = customer.user.email
                customer_l_name =  customer.user.last_name
                customer_f_name = customer.user.first_name
                message = "Bonjour Madame/Monsieur %s %s the rent time for your movie %s is now finish. Please return this movie in quickly delay" %(customer_f_name, customer_l_name, movie_title)
                to_emails = [str(customer_mail)]
                subject = "Movie to return" + customer_f_name + customer_l_name
                email = EmailMessage(subject, message, from_email='thomaslacolley@gmail.com', to=to_emails)

                email.encoding = 'us-ascii'
                email.send()



            else :
                print "Ok all customers have times"
            # print estimate_rent_date
