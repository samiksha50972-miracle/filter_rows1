from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return str(self.pk)  #returns string only  to return other field need to typecast it into string



class Webpage(models.Model):
    topic_name=models.ForeignKey('Topic',on_delete=models.CASCADE)
    name=models.CharField()
    url=models.URLField()
    email=models.EmailField()
    def __str__(self):
        return str(self.pk)

    





class AccessRecords(models.Model):
    name=models.ForeignKey('Webpage',on_delete=models.CASCADE)
    author=models.CharField()
    date=models.DateField()    

    def __str__(self):
        return self.author