import openai
def discrete_distill(model_ouputs):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You output in one word, which direction does the car first take: right, left, or straight"},
            {"role": "user", "content": model_ouputs},
        ]
    )
    return response['choices'][0]['message']['content']

def failure(car1, car2, ambulance):
    if car1!=car2:
        return True
    elif car1==car2 and car1==ambulance and car1=="right":
        return False
    elif car1==car2 and car1==ambulance:
        return True
    else:
        return False