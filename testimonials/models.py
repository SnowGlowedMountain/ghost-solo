from django.db import models

class Testimonial(models.Model):
    testimonial_first_name = models.CharField(max_length=100, verbose_name='First Name')
    testimonial_last_name = models.CharField(max_length=100, verbose_name='Last Name')
    testimonial_title = models.CharField(max_length=200, verbose_name='Testimonial Title')
    testimonial_body = models.TextField(verbose_name='Testimonial Body')

    def __str__(self):
        return self.testimonial_title
