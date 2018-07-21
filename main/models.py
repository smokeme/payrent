from django.db import models

# Create your models here.


class Complex(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Renter(models.Model):
    paci = models.IntegerField()
    floor = models.IntegerField()
    office = models.IntegerField()
    rent = models.PositiveIntegerField()
    complex = models.ForeignKey(
        Complex, related_name="renter", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.paci)


class Payment(models.Model):
    amount = models.IntegerField()
    payer = models.ForeignKey(Renter, related_name="payment", on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "PACI: %d -- Payment: %d -- Status: %s -- Date: %s" % (
            self.payer.paci,
            self.amount,
            self.status,
            self.date,
        )

