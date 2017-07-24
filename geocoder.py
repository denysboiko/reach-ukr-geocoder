#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv, json, urllib2

def parse_yandex_response(url):
    hi_web = urllib2.urlopen(url)
    geoObject = json.loads(hi_web.read())['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    return geoObject['Point']['pos']


def fetchCoordinates(source_file, fields, output_file):
    reader = csv.DictReader(open(source_file), delimiter='\t')
    input = list(reader)
    data = []
    total = len(input)
    counter = 1

    for row in input:

        column = fields[0]

        print('Retrieving geoobject ' + str(counter) + ' of ' + str(total) + ': ' +row[column])

        urls = map(lambda x: 'https://geocode-maps.yandex.ru/1.x/?format=json&geocode='+row[x], fields)

        geopoint = parse_yandex_response(urls[0])
        geopoint_street = parse_yandex_response(urls[1])
        geopoint_settlement = parse_yandex_response(urls[2])


        item = {}
        item['id'] = row['id']
        item['descr'] = row[column].decode('utf-8')

        item['pos'] = geopoint.split()[1] + ' ' + geopoint.split()[0]
        item['pos_street'] = geopoint_street.split()[1] + ' ' + geopoint_street.split()[0]
        item['pos_settlement'] = geopoint_settlement.split()[1] + ' ' + geopoint_settlement.split()[0]


        data.append(item)
        # print('Object ' + str(counter) + ' is retrieved successfully.')
        counter += 1

    with open(output_file, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(
            [
                'id',
                'address',
                'geopoint',
                'geopoint_street',
                'geopoint_settlement'
            ]
        )
        for item in data:
            spamwriter.writerow(
                [
                    item['id'],
                    item['descr'].encode('utf-8'),
                    item['pos'],
                    item['pos_street'],
                    item['pos_settlement']
                ]
            )



fetchCoordinates(
    'input\example_input_data.txt',
    ['Address_updated', 'Address_street', 'Address_city'],
    'output\example_output_data.csv'
)



