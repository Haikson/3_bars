import sys
import json
import math
import operator


def get_seats_sorted(json_data, reverse=False):
    return sorted(json_data, key=lambda k: k.get('SeatsCount', 0), reverse=reverse)

def load_data(filepath):
    with open(filepath, "r") as fd:
        json_data = json.load(fd, encoding="utf-8")
    return json_data


def get_biggest_bar(json_data):
    bars = get_seats_sorted(json_data, reverse=True)
    print("{}: количество мест {}".format(bars[0]["Name"], bars[0]["SeatsCount"]))


def get_smallest_bar(json_data):
    bars = get_seats_sorted(json_data)
    print("{}: количество мест {}".format(bars[0]["Name"], bars[0]["SeatsCount"]))


def distance(longitude, latitude, bar):
    coordinates = bar["geoData"]["coordinates"]
    return math.sqrt(pow((coordinates[0]-longitude), 2)+pow((coordinates[1]-latitude), 2))


def get_closest_bar(json_data, longitude, latitude):
    min_distance = distance(longitude, latitude, json_data[0])
    closest_bar = json_data[0]
    for bar in json_data:
        dist = distance(longitude, latitude, bar)
        if dist < min_distance:
            min_distance = dist
            closest_bar = bar
    print("Ближайший бар: {}".format(closest_bar["Name"]))
            
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(u"Не указан путь к файлу данных.")
    else:
        json_data = load_data(filepath=sys.argv[1])
        get_biggest_bar(json_data)
        get_smallest_bar(json_data)
    
        longitude = input(u"Введите долготу: ")
        latitude = input(u"Введите широту: ")
        get_closest_bar(json_data, float(longitude), float(latitude))
