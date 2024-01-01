from rest_framework import serializers
from pokemon.models import Pokemon

class PostPokemonSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pokemon
        fields = ['id', 'pokedex_no_field', 'name', 'type_1', 'type_2', 
                  'total', 'hp', 'attack', 'defense', 'sp_atk',
                  'sp_def', 'speed', 'generation', 'legendary']

class PokemonSerializers(serializers.ModelSerializer):
    Pokedex_No = serializers.SerializerMethodField()
    Name = serializers.SerializerMethodField()
    Type_1 = serializers.SerializerMethodField()
    Type_2 = serializers.SerializerMethodField()
    Total_Stat = serializers.SerializerMethodField()
    HP = serializers.SerializerMethodField()
    Attack = serializers.SerializerMethodField()
    Defense = serializers.SerializerMethodField()
    Sp_Attack = serializers.SerializerMethodField()
    Sp_Defense = serializers.SerializerMethodField()
    Speed = serializers.SerializerMethodField()
    Generation = serializers.SerializerMethodField()
    Legendary = serializers.SerializerMethodField()

    class Meta:
        model = Pokemon
        fields = ['Pokedex_No', 'Name', 'Type_1', 'Type_2', 
                  'Total_Stat', 'HP', 'Attack', 'Defense', 'Sp_Attack',
                  'Sp_Defense', 'Speed', 'Generation', 'Legendary']

    def get_Pokedex_No(self, obj):
        return obj.pokedex_no_field
    
    def get_Name(self, obj):
        return obj.name

    def get_Type_1(self, obj):
        return obj.type_1

    def get_Type_2(self, obj):
        return obj.type_2

    def get_Total_Stat(self, obj):
        return obj.total

    def get_HP(self, obj):
        return obj.hp

    def get_Attack(self, obj):
        return obj.attack

    def get_Defense(self, obj):
        return obj.defense

    def get_Sp_Attack(self, obj):
        return obj.sp_atk

    def get_Sp_Defense(self, obj):
        return obj.sp_def

    def get_Speed(self, obj):
        return obj.speed

    def get_Generation(self, obj):
        return obj.generation

    def get_Legendary(self, obj):
        return obj.legendary
    