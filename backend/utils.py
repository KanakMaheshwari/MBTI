import json
import requests
from ollama import generate


def reading_json():
    with open('C:/code/mbti/backend/q_and_a.json', 'r') as file:
        reading=json.load(file)
    return reading


def interact(prompt):
    try:
        # response = requests.post(
        #     "http://localhost:11434/api/generate",
        #     json={"model": "deepseek-r1:1.5b", "prompt": "What is ur personality"}
        # )
        response = generate('deepseek-r1:1.5b',str(prompt),think=False)

        return response['response']

    except requests.RequestException as e:
        print(e)

def get_mbti_prediction(answers):
    with open('C:/code/mbti/backend/q_and_a.json', 'r') as file:
        reading=json.load(file)
    prompt =  '''You are an expert in MBTI (Myers-Briggs Type Indicator) personality typing.
Based on the answers below, determine the person's MBTI personality type (e.g., ENTP, ISFJ, etc.) 
and provide a short but insightful description (5–7 sentences) of this personality type, focusing on 
their strengths, communication style, and typical behavior patterns.
Here are the questions and selected options:'''




    for ans in answers.quiz:
        for q_and_a in reading['quiz']:
            if q_and_a['id'] == ans.id:
                current_ans = ans.answer
                prompt += f"{q_and_a['question']} : {str(q_and_a['options'])}, Person chose option number {str(ans.answer)}"
                prompt += "\n"
    prompt+='''Please give:
1. The MBTI type (4 letters).
2. A concise description (5–7 sentences) explaining their personality traits, typical behavior, strengths, and possible areas of growth.
return in json format
'''



    return prompt






answers= [{"id": 1, "answer": 0},
    {"id": 2, "answer": 1},
    {"id": 3, "answer": 0},
    {"id": 4, "answer": 1},
    {"id": 5, "answer": 0},
    {"id": 6, "answer": 1},
    {"id": 7, "answer": 0},
    {"id": 8, "answer": 1},
    {"id": 9, "answer": 0},
    {"id": 10, "answer": 1},
    {"id": 11, "answer": 0},
    {"id": 12, "answer": 1},
    {"id": 13, "answer": 0},
    {"id": 14, "answer": 1},
    {"id": 15, "answer": 0}
  ]

# my_promt = get_mbti_prediction(answers=answers)
#
# lol = interact(my_promt)
# print(lol)