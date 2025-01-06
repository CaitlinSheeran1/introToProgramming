'''
Accessor methods: These allow us access to the instance variable. Also, these are frequently called getters as they typically begin with
the word get

the line self._name = name creates an instance variable named _name
and assigns it to the object being created (that's what self does). The value
of _name will be wahtever is passed by name

'''
import math

class Planet:
    def __init__(self, name, mass, radius, distance):
        self._name = name
        self._mass = mass
        self._radius = radius
        self._distance = distance

    def get_name(self):
        return self._name
    
    def get_mass(self):
        return self._mass
    
    def get_radius(self):
        return self._radius
    
    def get_distance(self):
        return self._distance

    def get_volume(self):
        volume = 4 / 3 * math.pi * self._radius ** 3
        return volume
    
    def get_density(self):
        density = self._mass / self.get_volume()
        return density

    
planet1 = Planet('x25', 35, 18, 100)
planet2 = Planet('zr23', 45, 15, 10)

print(planet1.get_name())
print(planet1.get_mass())
print(planet1.get_radius())
print(planet1.get_density())


'''
In Python, there is a special method called __str__ whoch is what the print function prints. By default, __str__ prints class name
and memory location. We can change this using a procedure called overloading

To do this, we define a method named __str__ and give it a new implantation
'''

class Star:
    def __init__(self, name):

        self.name = name











class PlanetarySystem:
    '''
    It should take a star as a argument
    It should start with no planets, but should have the ability to
    add planets itself
    '''


    def __init__(self, star):
        self._star = star
        self._planets = []


    def add_planet(self, planet):
        self._planets.append(planet)

    def show_planets(self):
        '''
        print the names of all the planets in the list of planets
        '''
        for planet in self._planets:
            print(planet.get_name())

    def star_planetary_orbit(self):
        pass

    def change_name_of_star(self, new_name):
        self._star.set_name(new_name)


solar_system = PlanetarySystem(Star('Sun'))






mercury = Planet('Mercury', 1, 1, 1)
solar_system.add_planet(mercury)

venus = Planet('Venus', 1, 1, 1)
solar_system.add_planet(venus)

earth = Planet('Earth', 1, 1, 1)
solar_system.add_planet(earth)

mars = Planet('Mar', 1, 1, 1)
solar_system.add_planet(mars)


solar_system.show_planets()