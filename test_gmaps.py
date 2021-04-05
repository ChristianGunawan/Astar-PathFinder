import gmaps
import smtplib
# working with gmaps
with open('api.txt') as f:
    API_KEY = f.readline()
    f.close
print(API_KEY)

