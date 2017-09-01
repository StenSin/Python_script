# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys
#import collections
from pick import pick
print (sys.version)


profile = []
        

id = input("What is the Profile ID?")
id=int(id)
profile.append(hex(id))

sequence = input("What is the Profile Sequence?")
sequence=int(sequence)
profile.append(hex(sequence))

profile.append(hex(0xFE))


days=input("What days will it be working? (ho,m,tu,w,th,f,sa,su) ?").lower()

week=0

if ("ho" in days)==True:
   week=week+1    
if ("m" in days)==True:
    week=week+2
if ("tu" in days)==True:
    week=week+4
if ("w" in days)==True:
    week=week+8
if ("th" in days)==True:
    week=week+16
if ("f" in days)==True:
    week=week+32
if ("sa" in days)==True:
    week=week+64
if ("su" in days)==True:
    week=week+128

hex_week=hex(week)
profile.append(hex_week)
time_list=[0]
i1=0
while i1<10:
     input1=input("Do you want to add a step and dim time (y/n) ?\n")     
     if input1=="y":
         time=input("What is the step time (hhmm) ?")
         time_ctrl=int(time)
         time_list.append(time_ctrl)
         if len(time)<4:
             print ("Too short step time")
             break
         elif (time_ctrl<time_list[len(time_list)-2]):
             print("Step time earlier than previous step time")
             break
         else: 
             time1= 6* int (time[:2])
             time2=int(time[2])
             time=hex(time1+time2)
             profile.append(time)
             dim_time=input("What is the dimming(0-100)?")
             if int(dim_time)<0:
                 dim_time=0;
                 profile.append(hex(int(dim_time)))
             elif int(dim_time)>100:
                 dim_time=100
                 profile.append(hex(int(dim_time)))
             else :
                 dim_time1=hex(int(dim_time))
                 profile.append(dim_time1)
     else: 
         break
     i1+=1
     
def print_all (file):
     for i in profile:
         print(i[2:],end="")
i2=0
print (profile)
print ("08",end="")
print_all(profile)