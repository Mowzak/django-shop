import random
from .models import checkout
def randomcheck(x):
    try:
        checkout.objects.get(tracing=x)
        return True
    except:
        return False
def randomint():
    x = random.randint(100000,999999)
    if randomcheck(x):
        randomint()
    return x
