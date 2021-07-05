from django.db import models

# Create your models here.
EVOLUTION_TYPES = [
    ('PE', 'Preevolution'),
    ('EV', 'Evolution')
]


class Pokemon(models.Model):
    name = models.CharField(
        max_length=255
    )
    height = models.IntegerField()
    weight = models.IntegerField()
    child = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='parent',
        on_delete=models.CASCADE
    )


class Stat(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        related_name='stats',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=127
    )
    base_stat = models.IntegerField()