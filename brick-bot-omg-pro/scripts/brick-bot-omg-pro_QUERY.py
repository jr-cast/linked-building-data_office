from rdflib import RDF, RDFS, OWL, Namespace, Graph
from rdflib.term import BNode

g = Graph()
g.parse("./compiled-brick-bot-omg-pro.ttl", format="ttl")

# semantic model with sensors linked to virtual zones

# Query 1, retrieve temperature sensors
sensors = g.query(
    """SELECT ?sensor WHERE {
    ?sensor a brick:Temperature_Sensor .
}
""")
for row in sensors:
    print(row)

# Query 2, retrieve humidity sensors 
hum_sen = g.query(
    """SELECT ?hs WHERE {
    ?hs a brick:Zone_Air_Humidity_Sensor .
}"""
)
for row in hum_sen:
    print(row)

# Query 3, retrieve brick zones (physical) and their bot (virtual) representation
zones = g.query(
    """SELECT DISTINCT ?brick ?bot WHERE{
    ?brick a brick:HVAC_zone .
    ?bot a bot:Zone .
    }
    """
)
for row in zones:
    print(row)

# Query4, lets fetch the associated sensors with each virtual office rooms
office_sen = g.query("""
SELECT DISTINCT ?of ?hs ?ts WHERE{
    ?of a bot:Zone .
    ?of brick:hasPoint ?hs .
    ?hs a brick:Zone_Air_Humidity_Sensor .
    ?ts a brick:Temperature_Sensor .
}"""
)
for row in office_sen:
    print(row)

# Query 5, retrieve universally unique identifier (UUID) associated with temperature sensor and units: 
qres = g.query("""
SELECT ?ts ?tsid WHERE {
    ?ts a brick:Temperature_Sensor  .
    ?ts brick:timeseries/brick:hasTimeseriesId ?tsid .
}""")
for row in qres:
    print(row)

# Query 6, select sensor and its associated uuid
for point, ts_id in g.query("""
    SELECT ?point ?ts_id WHERE {
        ?point brick:timeseries/brick:hasTimeseriesId ?ts_id .
    }
"""):
    print(point, ts_id)

for sensors in g.query("""
SELECT ?s WHERE {
    ?s a brick:Sensor .
}
"""):
    print(sensors)