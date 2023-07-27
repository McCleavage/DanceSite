from django.db import models

# Available choices for category and star rating
CATEGORIES = (('STD', 'Standard'),
              ('LTN', 'Latin'))

STARS = (('1', '*'),
         ('2', '* *'),
         ('3', '* * *'),
         ('4', '* * * *'),
         ('5', '* * * * *'))


class Style(models.Model):
    """This class stores the model details of each style

        :param CharField name: The name of the dance
        :param CharField category: Two choices for the style category
        :param CharField rating: Five choices for the dance's rating 1 star to 5 stars
        :param TextField description: Text description of the dance;
                                      contains the html describing the main body of the webpage
        :param ImageField image: Image field storing an image of the dance
        :returns: The rendered index page

        :rtype: HttpResponse
    """

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
