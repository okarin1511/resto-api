from zipapp import create_archive
import requests
import json
import sqlite3
from sqlite3 import Error


def getData(conn):
    cur = conn.cursor()

    response = requests.get(
        "https://random-data-api.com/api/restaurant/random_restaurant"
    )
    data = json.loads(response.text)

    name = data["name"]
    type = data["type"]
    desc = data["description"]
    opening_time_mon = data["hours"]["monday"]["opens_at"][:-3].replace(":", "")
    opening_time_tue = data["hours"]["tuesday"]["opens_at"][:-3].replace(":", "")
    opening_time_wed = data["hours"]["wednesday"]["opens_at"][:-3].replace(":", "")
    opening_time_thu = data["hours"]["thursday"]["opens_at"][:-3].replace(":", "")
    opening_time_fri = data["hours"]["friday"]["opens_at"][:-3].replace(":", "")
    opening_time_sat = data["hours"]["saturday"]["opens_at"][:-3].replace(":", "")
    opening_time_sun = data["hours"]["sunday"]["opens_at"][:-3].replace(":", "")

    closing_time_mon = data["hours"]["monday"]["closes_at"][:-3].replace(":", "")
    closing_time_mon = int(closing_time_mon) + 1200
    closing_time_tue = data["hours"]["tuesday"]["closes_at"][:-3].replace(":", "")
    closing_time_tue = int(closing_time_tue) + 1200
    closing_time_wed = data["hours"]["wednesday"]["closes_at"][:-3].replace(":", "")
    closing_time_wed = int(closing_time_wed) + 1200
    closing_time_thu = data["hours"]["thursday"]["closes_at"][:-3].replace(":", "")
    closing_time_thu = int(closing_time_thu) + 1200
    closing_time_fri = data["hours"]["friday"]["closes_at"][:-3].replace(":", "")
    closing_time_fri = int(closing_time_fri) + 1200
    closing_time_sat = data["hours"]["saturday"]["closes_at"][:-3].replace(":", "")
    closing_time_sat = int(closing_time_sat) + 1200
    closing_time_sun = data["hours"]["sunday"]["closes_at"][:-3].replace(":", "")
    closing_time_sun = int(closing_time_sun) + 1200

    sql = """INSERT INTO api_timings(
            opening_time_mon,
            closing_time_mon,
            opening_time_tue,
            closing_time_tue,
            opening_time_wed,
            closing_time_wed,
            opening_time_thu,
            closing_time_thu,
            opening_time_fri,
            closing_time_fri,
            opening_time_sat,
            closing_time_sat,
            opening_time_sun,
            closing_time_sun
        ) values(
            {0},
            {1},
            {2},
            {3},
            {4},
            {5},
            {6},
            {7},
            {8},
            {9},
            {10},
            {11},
            {12},
            {13}
        )""".format(
        opening_time_mon,
        closing_time_mon,
        opening_time_tue,
        closing_time_tue,
        opening_time_wed,
        closing_time_wed,
        opening_time_thu,
        closing_time_thu,
        opening_time_fri,
        closing_time_fri,
        opening_time_sat,
        closing_time_sat,
        opening_time_sun,
        closing_time_sun,
    )

    cur.execute(sql)
    conn.commit()

    rowid = cur.lastrowid

    print(name)
    print(type)
    print(desc)

    sql2 = """INSERT INTO api_restaurant(
            name,
            type,
            desc,
            timings_id
        ) values (
            '{0}',
            '{1}',
            '{2}',
            '{3}'
        )""".format(
        name, type, desc, rowid
    )

    cur.execute(sql2)
    conn.commit()


def callAPI():

    conn = sqlite3.connect(
        "/home/aseem/Documents/Hackerman/DjangoApp/restoApi/db.sqlite3"
    )
    print("Connected")

    for i in range(100):
        getData(conn)
        print("Entering data")
    # cur.close()


callAPI()
