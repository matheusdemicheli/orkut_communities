from django.db import models


class Community(models.Model):
    """
    Represents a community.
    """

    url = models.CharField(max_length=200)

    name = models.CharField(max_length=500, db_index=True)

    description = models.TextField()

    url_image = models.CharField(max_length=1000)

    def __unicode__(self):
        """
        Represents the object by community's name.
        """
        return self.name
