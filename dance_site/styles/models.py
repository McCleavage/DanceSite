from django.db import models

# Available choices for category and star rating
CATEGORIES = (('STD', 'Standard'),
              ('LTN', 'Latin'))

STARS = (('1', '*'),
         ('2', '* *'),
         ('3', '* * *'),
         ('4', '* * * *'),
         ('5', '* * * * *'))


# The Style model stores information about each dance style,
# namely name, category, rating and description
class Style(models.Model):
    name = models.CharField(max_length=140)
    category = models.CharField(max_length=3, choices=CATEGORIES, default='STD')
    rating = models.CharField(max_length=1, choices=STARS, default='5')
    description = models.TextField(default="")
    # For the moment, height and width have no effect and are commented out,
    # however they may be useful in future to inform scaling of low-res images
    # height = models.PositiveIntegerField(default=300)
    # width = models.PositiveIntegerField(default=300)
    image = models.ImageField(upload_to='static/images/',
                              # height_field='height', width_field='width',
                              default='static/images/dance.png')

    def __str__(self):
        return self.name
