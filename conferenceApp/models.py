from django.db import models
# Create your models here.
class Role(models.Model):
    choix=[
        ("USER","USER")
        ,("ADMIN","ADMIN")
        ,("GEST","GEST")
        ]
    role=models.CharField(max_length=5,choices=choix,unique=True,default='USER')
    def __str__(self):
        return self.role

class User1(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    name=models.CharField(max_length=100)
    prenom=models.CharField(max_length=10)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    estIntervenant=models.BooleanField(default=False)
    def __str__(self):
        return self.email
class Conference(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    nom=models.CharField(max_length=100)
    lieu=models.CharField(max_length=100)
    them=models.TextField()
    dateDebut=models.DateField()
    dateFin=models.DateField()
    user=models.ManyToManyField(User1)

    
    def __str__(self):
        return self.nom

class Session(models.Model):
    id =models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100)
    date=models.DateField()
    heureDebut=models.TimeField()
    heureFin=models.TimeField()
    description=models.TextField()
    conference=models.ForeignKey(Conference,on_delete=models.CASCADE,related_name='conference')
    def  __str__(self):
         return self.titre
class SessionIntervenant(models.Model):
    id=models.AutoField(unique=True,primary_key=True)
    session=models.ForeignKey(Session,on_delete=models.CASCADE)
    intervenant=models.ForeignKey(User1,on_delete=models.CASCADE,related_name='intervenant',unique=True)



