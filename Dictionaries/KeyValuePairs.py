# Dictionaries: Key-Value pairs, Unordered, Mutable

miles_davis = {
    "name": "Miles Davis",
    "instrument": "trumpet",
    "years_active": "1944 - 1991"
}
john_coltrane = {
    "name": "John Coltrane",
    "instrument": "tenor saxophone",
    "years_active": "1945 - 1967"
}
red_garland = {
    "name": "Red Garland",
    "instrument": "piano",
    "years_active": "1940 - 1984"
}
paul_chambers = {
    "name": "Paul Chambers",
    "instrument": "bass",
    "years_active": "1954 - 1969"
}
philly_joe_jones = {
    "name": "Philly Joe Jones",
    "instrument": "drums",
    "years_active": "1947 - 1979"
}
cannonball_adderley = {
    "name": "Cannonball Adderley",
    "instrument": "alto saxophone",
    "years_active": "1955 - 1975"
}
wayne_shorter = dict(
    zip(["name", "instrument", "years active"],
        ["Wayne Shorter", "soprano saxophone", "1958 - 2021"])
)
herbie_hancock = dict(name="Herbie Hancock", instrument="piano", years_active="1961 - Present")
ron_carter = dict([("name", "Ron Carter"), ("instrument", "bass"), ("years_active", "1960 - Present")])
tony_williams = dict({"name": "Tony Williams", "instrument": "drums"}, years_active="1961 - 1997")

miles_first_quintet_1955 = {
    "band_leader": miles_davis,
    "band_member_01": john_coltrane,
    "band_member_02": red_garland,
    "band_member_03": paul_chambers,
    "band_member_04": philly_joe_jones,
    "band_member_05": cannonball_adderley
}

miles_second_quintet_1964 = dict(
    band_leader=miles_davis,
    band_member06=wayne_shorter,
    band_member07=herbie_hancock,
    band_member08=ron_carter,
    band_member09=tony_williams
)

print(miles_first_quintet_1955)
print(miles_second_quintet_1964)

for key in miles_first_quintet_1955:
    print("Key: " + str(key))

for i in miles_first_quintet_1955:
    print(miles_first_quintet_1955[i])

if "band_leader" in miles_second_quintet_1964:
    print("Band Leader: " + str(miles_second_quintet_1964["band_leader"]["name"]))


print("------ Example ------")
squared_number_dictionary_99 = {x: x*x for x in range(1, 100)}
print(squared_number_dictionary_99)

