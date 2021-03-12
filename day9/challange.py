travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country, visits, cities):
        new_c = {}
        new_c["country"] = country
        new_c["visits"] = visits
        new_c["cities"] = cities
        travel_log.append(new_c)    


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
