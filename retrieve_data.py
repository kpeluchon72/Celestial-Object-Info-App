import requests


def get_body_data(body):
    url = 'https://api.le-systeme-solaire.net/rest/bodies/'

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()['bodies']

        for i in data:
            if (i['englishName']).lower() == body.lower():
                return i

    else:
        print(f"error: {response.status_code}")


class ExtractData:
    def __init__(self, body_data):
        self.body_data = body_data

    def english_name(self):
        return self.body_data['englishName']

    def body_mass(self):   # kg
        return self.body_data['mass']

    def body_density(self):    # g/cm3
        return self.body_data['density']

    def body_volume(self):  # km3
        return self.body_data['vol']

    def body_gravity(self):    # m/s-2
        return self.body_data['gravity']

    def body_history(self):
        return [self.body_data['discoveredBy'], self.body_data['discoveryDate']]

    def body_average_temperature(self): # Kelvin
        return self.body_data['avgTemp']

    def body_type(self):
        return self.body_data['bodyType']

    def body_time_orbit(self):     # orbit in earth day, rotation in hour
        return [self.body_data['sideralOrbit'], self.body_data['sideralRotation']]

    def body_orbit(self):
        # tilt in degrees, inclination (ecliptic plane) degrees,
        # orbital eccentricity (0-1 0 = circular, 1 = elliptical)
        body_orbit = None
        orbit_ranges = {"Circular": (0, .99),
                        "Elliptical": (.1, 1)
                        }

        for orbit_type, (start, end) in orbit_ranges.items():
            if start <= self.body_data['eccentricity'] < end:
                body_orbit = orbit_type

        return [(self.body_data['axialTilt']), (self.body_data['inclination']), (self.body_data['eccentricity'])], body_orbit

    def body_perihelion_aphelion(self):    # perihelion in km, aphelion in km
        return [self.body_data['perihelion'], self.body_data['aphelion']]

    def body_radis(self):  # meanradius, equatorial radius (center to equator), polar radius all in km
        return [self.body_data['meanRadius'], self.body_data['equaRadius'], self.body_data['polarRadius']]
