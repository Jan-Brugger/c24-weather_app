from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import DateField, FloatField, IntegerField, Model


class WeatherRecord(Model):
    date: DateField = DateField(primary_key=True)
    temperature: FloatField = FloatField()


class ImportRequest(Model):
    latitude: FloatField = FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    longitude: FloatField = FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    year: IntegerField = IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(date.today().year)])
    hour_of_the_day: IntegerField = IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])

    class Meta:
        managed = False
