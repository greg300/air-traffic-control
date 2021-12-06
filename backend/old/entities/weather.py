import random
import numpy as np
import time
import math
from datetime import datetime

mu_wind_spd=15
sigma_wind=7

mu_temp=50
sigma_temp=20

starttime = time.time()

while True:
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    wind_spd=abs(round(np.random.normal(mu_wind_spd, sigma_wind)))
    print("Wind speed is", wind_spd, "kts at",current_time)
    wind_dir=random.randint(0,359)
    print("Wind direction is", wind_dir,"degrees at",current_time)
    temp=round(np.random.normal(mu_temp, sigma_temp))
    print("Air temperature is",temp, "degrees F at",current_time)
    rain=random.choices([True, False], weights=[.20, .8])[0]
    print("Precipitation is",rain,"at",current_time, "\n")      
    time.sleep(300.0 - ((time.time() - starttime) % 300.0))
