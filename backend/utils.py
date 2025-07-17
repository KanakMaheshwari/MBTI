import json
def reading_json():
    with open('C:/code/mbti/backend/q_and_a.json', 'r') as file:
        reading=json.load(file)
    return reading
# print(reading_json())