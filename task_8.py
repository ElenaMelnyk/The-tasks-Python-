## 8. Volume of a Spherical Shell
## The volume of a spherical shell is the difference between the enclosed volume
## of the outer sphere and the enclosed volume of the inner sphere:
## 
## Create a function that takes r1 and r2 as arguments and returns the volume of
## a spherical shell rounded to the nearest thousandth.
##
## Notes
## The inputs are always positive numbers. r1 could be the inner radius or the
## outer radius, don't return a negative number.


def vol_shell (r1, r2):
    import math 
    R = abs (r1)
    r = abs (r2)
    if R < r:
        R, r = r, R
    v_betw_sph = 4 / 3 * math.pi * (R ** 3 - r ** 3)
    if v_betw_sph >= 0:
        return print ("The volume of a spherical shell is %.3f" %v_betw_sph)
    

r1 = int (input ("Input the radius of outer-sphere "))
r2 = int (input ("Input the radius of inner-sphere "))
print (vol_shell (r1, r2))
