from django.db import models

from data_sheets import measurements

class GeneralInformation(models.Model):
    communication_protocols = models.CharField(max_length=200)
    range_min = models.DecimalField()
    range_max = models.DecimalField()
    range_unit = models.CharField(choices=measurements.TEMPERATURE)


class SensorRequirements(models.Model):
    sensor_type = models.CharField(max_length=150)
    process_connection = models.CharField(max_length=255)
    insertion_length = models.DecimalField()
    length_units = models.CharField(choices=measurements.LENGTH)
    well_type = models.CharField(max_length=150)


class TransmitterRequirements(models.Model):
    MOUNTS = (
        ('head', 'Head Mounted'),
        ('field', 'Field Mounted'),
        ('panel', 'Panel Mounted')
    )
    transmitter_required = models.BooleanField()
    mount_type = models.CharField(choices=MOUNTS, max_length=15)


class TemperatureApplication(models.Model):
    applicant = models.ForeignKey('users.User', on_delete=models.CASCADE)
    general_information = models.ForeignKey('GeneralInformation', on_delete=models.CASCADE)
    sensor_requirements = models.ForeignKey('SensorRequrements', on_delete=models.CASCADE)
    transmitter_requirements = models.ForeignKey('TransmitterRequirements', on_delete=models.CASCADE)
    submitted = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant} - {self.submitted}"

