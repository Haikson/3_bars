import sys
import json
import math


def load_data(filepath):
    fd = open(filepath)
    json_data = json.load(fd, encoding="utf-8")
    fd.close()
    return json_data


def get_biggest_bar(json_data):
    print(max((bar['SeatsCount'] for bar in json_data)))


def get_smallest_bar(json_data):
    print(min((bar['SeatsCount'] for bar in json_data)))


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
    print(closest_bar["Name"])
            
if __name__ == '__main__':
    json_data = load_data(filepath="data-2897-2016-11-23.json")
    get_biggest_bar(json_data)
    get_smallest_bar(json_data)

    longitude = input()
    latitude = input()
    get_closest_bar(json_data, float(longitude), float(latitude))
