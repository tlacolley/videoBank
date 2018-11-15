from django.core.management.base import BaseCommand

from video_bank.models import Movie, Customer

import csv



class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
    	movies = Movie.objects.all()

    	with open('plop.csv', 'wb') as csvfile:
			writer = csv.writer(csvfile)
			models_fields = Movie._meta.fields
			fields_name = []
			for field in models_fields:
				fields_name.append(field.name)
			writer.writerow(fields_name)
			for movie in movies:
				movie_info = []
				for movie_fields in movie._meta.fields:
					field_val = getattr(movie, movie_fields.name)
					if isinstance(field_val,basestring) == True:
						# print field_val
						movie_info.append(field_val.encode('utf-8').strip()) 
					else:
						movie_info.append(field_val) 
						# print field_val
	        		writer.writerow(movie_info)
			