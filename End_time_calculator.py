#Lab from cisco
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
added_T = 0
if dura % 60 == 0:
    hour = dura/60

while dura > 60 and dura % 60 != 0:
    dura -= 60
    added_T += 1
    hour += added_T

if dura < 60:
    mins += dura
    
if mins >= 60:
    mins -= 60
    added_T = 1
    hour += added_T

while hour >= 24: 
    hour -=24
    
print("End Time: ", hour, ":", mins, )

