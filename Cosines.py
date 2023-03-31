##MICHAEL_BENNETT
##SDEV300_7380
##Professor_Zachery_Fair
##Week2_assignment2_Use_Law_of_Cosines_to_Calculate_the_Leg_of_a_Triangle
##3/28/2023


#importing the math library
import math

#defining the variables
a = 11
b = 8
angleC = 37

#applying the law of cosines
c = math.sqrt(a**2 + b**2 -2*a*b*math.cos(math.radians(angleC)))

#printing the answer
print("The length of the side c is: ", c," units")

#explaining the steps involved
print( 'The law of cosines states that c^2 = a^2 + b^2 -2abcos(C). We were given the length of side a and b and the '
       'angle C, which was 37 degrees. By using the law of cosines, we were able to calculate the length of side c, '
       'which was found to be 11.7 units.' )
