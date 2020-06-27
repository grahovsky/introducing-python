import json

menu = \
    {
    "breakfast": {
            "hours": "7-11",
            "items": {
                    "breakfast burritos": "$6.00",
                    "pancakes": "$4.00"
                    }
            },
    "lunch" : {
            "hours": "11-3",
            "items": {
                    "hamburger": "$5.00"
                    }
            },
    "dinner": {
            "hours": "3-10",
            "items": {
                    "spaghetti": "$8.00"
                    }
            }
    }

print(menu)

menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

import datetime
now = datetime.datetime.utcnow()
print(now)
# json.dumps(now)
# TypeError: Object of type datetime is not JSON serializable

now_str = str(now)
print(json.dumps(now_str))

datetime_json = json.dumps(now, default=str)
print(datetime_json)