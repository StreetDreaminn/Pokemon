from django.db import models

class Pokemon(models.Model):
    id = models.SmallIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pokedex_no_field = models.SmallIntegerField(db_column='Pokedex No.')  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    name = models.CharField(db_column='Name')  # Field name made lowercase.
    type_1 = models.CharField(db_column='Type 1')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type_2 = models.CharField(db_column='Type 2', null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total = models.SmallIntegerField(db_column='Total')  # Field name made lowercase.
    hp = models.SmallIntegerField(db_column='HP')  # Field name made lowercase.
    attack = models.SmallIntegerField(db_column='Attack')  # Field name made lowercase.
    defense = models.SmallIntegerField(db_column='Defense')  # Field name made lowercase.
    sp_atk = models.SmallIntegerField(db_column='Sp. Atk')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    sp_def = models.SmallIntegerField(db_column='Sp. Def')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    speed = models.SmallIntegerField(db_column='Speed')  # Field name made lowercase.
    generation = models.SmallIntegerField(db_column='Generation')  # Field name made lowercase.
    legendary = models.BooleanField(db_column='Legendary')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pokemon'