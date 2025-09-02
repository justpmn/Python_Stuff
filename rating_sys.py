# Write code below 💖
while True: #loop to ensure ratings are within bounds. Float to allow decimal ratings.
  rating = float(input("Rate the restaurant from 0 to 5: "))
  if (0 <= rating <= 5):
    break
  else:
    print("Rating out of bounds")
if(rating >= 4.5):
  print("Extraordinary")

elif(rating >= 4):
    print("Excellent")
elif(rating >= 3):
    print("Good")
elif(rating >= 2):
    print("Fair")
else:
    print("Poor")
