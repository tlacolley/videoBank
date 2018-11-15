from django.core.management.base import BaseCommand
from django.utils import timezone
import datetime
from video_bank.models import MovieRent, Customer
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string



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

                text_content = render_to_string('video_bank/mails/resend_customer.txt', {'movie_rent':movie})
                html_content = render_to_string('video_bank/mails/resend_customer.html', {'movie_rent':movie})
                to_emails = [str(customer_mail)]
                subject = "Movie to return:" + customer_f_name +" "+ customer_l_name
                
                email = EmailMultiAlternatives(subject, text_content, from_email='thomaslacolley@gmail.com', to=('thomaslacolley@gmail.com',))

                email.attach_alternative(html_content, "text/html")
                email.send()


            else :
                print "Ok all customers have times"
