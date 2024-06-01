from django.db import models


class Categories(models.Model):
    category = models.CharField(max_length=250)

    class Meta:
        db_table = "Categories"

    def __str__(self):
        return self.category


class Signs(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    audio = models.FileField(upload_to='audios/', blank=True, null=True)
    docs = models.FileField(upload_to='docs/', blank=True, null=True)

    class Meta:
        db_table = 'Signs'

    def __str__(self):
        return self.name
