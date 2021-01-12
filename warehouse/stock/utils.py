from django.core.validators import MinValueValidator, MaxValueValidator

MinInt32 = MinValueValidator(limit_value=-(2**31))
MaxInt32 = MaxValueValidator(limit_value=(2**31))
