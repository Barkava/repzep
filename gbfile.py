from pprint import pprint

cities = {
    'Tbilisi': (41.716667, 44.783333),
    'Batumi': (41.64228, 41.63392),
    'Sokhumi': (43.0, 41.0166666),
    'Kutaisi': (42.26667, 42.6),
    'Asureti': (41.595833, 44.666667),
}

distances = dict()

tbilisi = cities['Tbilisi']
batumi = cities['Batumi']
sokhumi = cities['Sokhumi']
kutaisi = cities['Kutaisi']
asureti = cities['Asureti']

tbilisi_batumi = ((tbilisi[0] - batumi[0])**2 + (tbilisi[1] - batumi[1])**2) ** .5 * 111.32
tbilisi_sokhumi = ((tbilisi[0] - sokhumi[0])**2 + (tbilisi[1] - sokhumi[1])**2) ** .5 * 111.32
tbilisi_kutaisi = ((tbilisi[0] - kutaisi[0])**2 + (tbilisi[1] - kutaisi[1])**2) ** .5 * 111.32
tbilisi_asureti = ((tbilisi[0] - asureti[0])**2 + (tbilisi[1] - asureti[1])**2) ** .5 * 111.32

distances['Tbilisi'] = {}
distances['Tbilisi']['Batumi'] = tbilisi_batumi
distances['Tbilisi']['Sokhumi'] = tbilisi_sokhumi
distances['Tbilisi']['Kutaisi'] = tbilisi_kutaisi
distances['Tbilisi']['Asureti'] = tbilisi_asureti


pprint(distances)
