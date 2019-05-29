'''
This files contains some example tools to do calculatoins with planets
'''
import numpy as np

# average_density =5.52e12kg/km^3
#Exercise 1:Transfer over the function get_planet_mass_from_dictionary to this python file.

#Hint: you'll need to import numpy or math for pi
#in a subsequent line, print out jupiter's mass

#radii in km
dictionary_of_radii = {'Mercury':2439.7,
                 'Venus':6051.8,'Earth':6378.1,
                 'Mars':3396.2, 'Jupiter':71492,
                 'Saturn':60268,'Uranus':25559, 'Neptune':24764}

def get_planet_mass_from_dictionary(planet, dictionary_of_radii, average_planet_density) :
  ''' Here is the docstring for this function that describes what it does.
  This uses a dictionary of radii whose keys are planet names to calculate a mass estimate of a planet.  
  '''
  radius_of_planet = dictionary_of_radii[planet]
  mass = 4./3 *np.pi*radius_of_planet**3 * average_planet_density 
  return mass

planet=input("Which planet? ")
print(get_planet_mass_from_dictionary(planet,dictionary_of_radii,5.52e12))
