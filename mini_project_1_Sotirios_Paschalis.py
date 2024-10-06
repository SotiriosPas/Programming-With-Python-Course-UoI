#Mini-project 1 Sotirios Paschalis
import math

a1 = float(input('a1 = '))

a2 = float(input('a2 = '))

b1 = float(input('b1 = '))

b2 = float(input('b2 = '))

eswteriko_ginomeno = a1*b1 + a2*b2

metro_dian_a = math.sqrt(a1**2 + a2**2)

metro_dian_b = math.sqrt(b1**2 + b2**2)

costh = eswteriko_ginomeno/(metro_dian_a*metro_dian_b) 

print("To sinimitono tis gwnias th einai",costh)

goniath_aktinia = math.acos(costh)

goniath = math.degrees(goniath_aktinia)

print("H gwnia th einai",goniath,"moires.")
