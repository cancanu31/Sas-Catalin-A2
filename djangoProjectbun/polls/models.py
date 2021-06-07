from django.db import models


class Weather(models.Model):
    airTemperature = models.FloatField(default=0)
    pressure = models.FloatField(default=0)
    windDirection = models.FloatField(default=0)
    windSpeed = models.FloatField(default=0)
    visibility = models.FloatField(default=0)
    waterTemperature = models.FloatField(default=0)
    cloudCover = models.FloatField(default=0)

    # def __str__(self):
    #     return self.title
    #returneaza un dic cu toate elem
    def dictionar(self):
        dictionar={
            "airTemperature": self.airTemperature,
            "pressure": self.pressure,
            "windDirection": self.windDirection,
            "windSpeed": self.windSpeed,
            "visibility": self.visibility,
            "waterTemperature": self.waterTemperature,
            "cloudCover": self.cloudCover
        }
        return dictionar

