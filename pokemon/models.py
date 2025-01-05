from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    id = models.SmallIntegerField(db_column='id', primary_key=True)
    pokedex_no_field = models.SmallIntegerField(db_column='pokedex_no')
    name = models.CharField(db_column='name')
    type_1 = models.CharField(db_column='type_1')
    type_2 = models.CharField(db_column='type_2', null=True)
    total = models.SmallIntegerField(db_column='total')
    hp = models.SmallIntegerField(db_column='hp')
    attack = models.SmallIntegerField(db_column='attack')
    defense = models.SmallIntegerField(db_column='defense')
    sp_atk = models.SmallIntegerField(db_column='sp_atk')
    sp_def = models.SmallIntegerField(db_column='sp_def')
    speed = models.SmallIntegerField(db_column='speed')
    generation = models.SmallIntegerField(db_column='generation')
    legendary = models.BooleanField(db_column='legendary')

    class Meta:
        managed = False
        db_table = 'pokemon'

class Module(models.Model):
    name = models.CharField(max_length=50)

class Permission(models.Model):
    name = models.CharField(max_length=50)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)