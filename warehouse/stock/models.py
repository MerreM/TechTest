from django.db import models

import uuid

from .utils import MinInt32, MaxInt32


class Stock(models.Model):
    """
    Quick notes:
    sku - a uuid, can/should work
        not great from a human readability front though.
    name - should be fine.
    quantitiy - validators to ensure it's really an int32
        don't know that you'd really want ~ -2mil as quantity though. uint32?
    price - I've cheated and changed it to a decimal based
         on experience using floats as monetary values.
         YMMV though, maybe you want values to more decimal places.
         and maybe floats are fine?
         512 digits sohuld be *way* more than needed.
    """
    sku = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinInt32, MaxInt32])
    price = models.DecimalField(max_digits=512, decimal_places=2)
    date_modified = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __repr__(self):
        return "{} <Qty: {}>".format(self.name, self.quantity)

    def __str__(self):
        return self.__repr__()
