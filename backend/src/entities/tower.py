print("Requesting weather data")

#import weather data
from weather import wind_spd, wind_dir,temp,rain
 #default condition
conditions=safe

if(rain==True and temp<34): #if cold and rainy it is not safe for takeoff
    conditions = unsafe
                
if(wind_spd>28): #if wind speed greater than 28 kts it is not safe for takeoff
    conditions=unsafe
    
print("Conditions are ",conditions,"for takeoff")    

#aircraft take off and land against the wind. Note RW4 = 40degrees, RW22 = 220 degrees
if wind_dir in range(130,309):
    runway=4
else:
    runway=22

print("Active runway is runway ",runway)

