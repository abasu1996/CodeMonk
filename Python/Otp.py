import os
import math
import random
import smtplib
import time
# generating random OTP
digits = "0123456789"
OTP = ""


for i in range(6):
    ##OTP += digits[math.floor(random.random() * 10)]
    OTP += digits[random.randrange(0,7)]
otp = OTP + " is your OTP"
msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("anim.bose17@gmail.com", "tmkyojyvlbytzwok")

print("--- OTP verification using GMail account ---")


# getting mail id to send OTP
emailid = "animbose17@gmail.com"
s.sendmail('&&&&&&&', emailid, msg)
tic =  time.process_time()
# verifying OTP
def otp_send():
    rslt = 0
    while (rslt != 1):
        
        a = input("Enter Your OTP >>: ")
                        
        if a == OTP:
            #print("OTP Verified")
            rslt = 1
            
        else:
            print("Please Check your OTP & try again")
            rslt = 0
   
otp_send()
tac = time.process_time()
time_taken = tac - tic
if time_taken < 20:
    print("OTP Verified")
else:
    print("Time's Up")



            
