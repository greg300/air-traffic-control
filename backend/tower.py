import time
from weather import wind_spd, wind_dir, temp, rain

starttime = time.time()

while True:

    conditions=safe

    if(rain==true and temp<34): #if cold and rainy it is not safe for takeoff
        conditions = unsafe
           	 
    if(wind_spd>28): #if wind speed greater than 28 kts it is not safe for takeoff
        conditions=unsafe
    
    time.sleep(5.0 - ((time.time() - starttime) % 5.0))
    print("Conditions are ",conditions,"for takeoff")
