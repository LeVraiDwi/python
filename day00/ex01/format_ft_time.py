from datetime import date
import time

today = date.today()

d = today.strftime("%b-%d-%Y")

str = "Seconds since January 1, 1970: {:,.4f} or %.2e in scientific notation".format(time.time()) % (time.time())
print(str)
print(d)
