from django.db import models

class CompteUser(models.Model):
    id = models.AutoField(primary_key=True)
    iduser = models.IntegerField()
    tel = models.IntegerField()
    solde = models.IntegerField()
    devise = models.CharField(max_length=255)
    libele = models.CharField(max_length=255)
    dateCreation = models.DateField(auto_now=True)
    def __str__(self):
        return f'Compte({self.iduser}, {self.devise}, {self.tel})'

class Crypto(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    prixActuel = models.IntegerField()
    def __str__(self):
        return self.nom

class OrdreMarche(models.Model):
    id = models.AutoField(primary_key=True)
    idcompte = models.ForeignKey(to="CompteUser",on_delete=models.CASCADE)
    idcrypto = models.ForeignKey(to="Crypto",on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    prix = models.IntegerField()
    quantite = models.IntegerField()
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.type
    
class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    frais = models.DecimalField(max_digits=10, decimal_places=2)
    ordredemarche = models.ForeignKey(to="OrdreMarche",on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return f'Transaction({self.amount}, {self.currency}, {self.customer_id})'

class Historique(models.Model):
    id = models.AutoField(primary_key=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    idcompte = models.ForeignKey(to="CompteUser",on_delete=models.CASCADE)
    idcrypto = models.ForeignKey(to="Crypto",on_delete=models.CASCADE)
    idtransaction = models.ForeignKey(to="Transaction",on_delete=models.CASCADE)
    resultat = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.resultat