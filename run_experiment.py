import argparse
import openai
import random
from gpt4_vision_outputs import gpt_4_vision_outputs
# Assuming discrete_distill and failure are defined elsewhere
from validation import discrete_distill, failure

def experiment(usa_model, india_model, iterations):
    ambulance_side_center, ambulance_side_right, ambulance_side_left = gpt_4_vision_outputs()
    fms_finetuned = 0
    fms_base = 0

    for i in range(iterations):
        print("Current iteration: ", i)
        car1_side = random.choice(["right", "left"])
        car2_side = random.choice(["right", "left"])
        ambulance_side = ''
        if car1_side==car2_side:
            if car1_side=='left':
                random_list = random.choice([ambulance_side_center, ambulance_side_right])
                if random_list is ambulance_side_center:
                    ambulance_side = 'left'
                elif random_list is ambulance_side_right:
                    ambulance_side = 'right'
            else:
                random_list = random.choice([ambulance_side_center, ambulance_side_left])
                if random_list is ambulance_side_center:
                    ambulance_side = 'right'
                elif random_list is ambulance_side_left:
                    ambulance_side = 'left'
            model_input1 = random.choice(random_list)
            model_input2 = random.choice(random_list)

        else:
            if car1_side =="left":
                random_list_1 = random.choice([ambulance_side_center, ambulance_side_right])
                if random_list_1 is ambulance_side_center:
                    ambulance_side = 'left'
                else:
                    ambulance_side = 'right'
                if ambulance_side=='left':
                    random_list_2 = ambulance_side_left
                if ambulance_side=='right':
                    random_list_2 = ambulance_side_center
            else:
                random_list_1 = random.choice([ambulance_side_center, ambulance_side_left])
                if random_list_1 is ambulance_side_center:
                    ambulance_side = 'right'
                else:
                    ambulance_side = 'left'
                if ambulance_side == 'right':
                    random_list_2 = ambulance_side_right
                if ambulance_side=='left':
                    random_list_2 = ambulance_side_center
            model_input1 = random.choice(random_list_1)
            model_input2 = random.choice(random_list_2)

        content1 = f"You are on the {car1_side}. {model_input1}"
        content2 = f"You are on the {car2_side}. {model_input2}"
        response_usa = openai.ChatCompletion.create(
            model="ft:gpt-3.5-turbo-0613:personal::8HIJ0IZB",
            messages=[
                {"role": "system", "content": "You are a language model that outputs discrete actions to control a car based on information and your country's laws"},
                {"role": "user", "content": content1},
            ]
        )
        usa_action = discrete_distill(response_usa['choices'][0]['message']['content'])
        if usa_action.lower()=="straight":
            usa_action = car1_side

        response_india = openai.ChatCompletion.create(
            model="ft:gpt-3.5-turbo-0613:personal::8HOVOV4Y",
            messages=[
                {"role": "system", "content": "You are a language model that outputs discrete actions to control a car based on information and your country's laws"},
                {"role": "user", "content": content2},
            ]
        )
        india_action = discrete_distill(response_india['choices'][0]['message']['content'])
        if india_action.lower()=="straight":
            india_action = car2_side

        response_base1 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a language model that outputs discrete actions to control a car based on information and your country's laws. Output very concise action to take."},
                {"role": "user", "content": content1},
            ]
        )
        ogoutput1 = response_base1['choices'][0]['message']['content']
        basemodel1_action = discrete_distill(response_base1['choices'][0]['message']['content'])
        hold1 = basemodel1_action
        if basemodel1_action.lower()=="straight":
            basemodel1_action = car1_side
        if basemodel1_action.lower()=='left':
            print("ERROR content 1 is ", content1)
            print("OG output", ogoutput1)
            print("Distilled output", hold1)



        response_base2 = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a language model that outputs discrete actions to control a car based on information and your country's laws. Output very concise action to take."},
                {"role": "user", "content": content2},
            ]
        )


        ogoutput = response_base2['choices'][0]['message']['content']
        basemodel2_action = discrete_distill(response_base2['choices'][0]['message']['content'])
        hold = basemodel2_action
        if basemodel2_action.lower()=="straight":
            basemodel2_action = car2_side
        if basemodel2_action.lower()=='left':
            print("ERROR content 2 is ", content2)
            print("OG output", ogoutput)
            print("Distilled output", hold)


        if failure(usa_action.lower(), india_action.lower(), ambulance_side.lower()):
            fms_finetuned +=1
        if failure(basemodel1_action.lower(), basemodel2_action.lower(), ambulance_side.lower()):
            fms_base+=1
            print("BASE MODEL CONTENT 1: ", content1)
            print("BASE MODEL CAR 1: ", car1_side)
            print("BASE MODEL OUTPUT 1: ", basemodel1_action)
            print("BASE MODEL CONTENT 2: ", content2)      
            print("BASE MODEL CAR 2: ", car2_side)
            print("BASE MODEL OUTPUT 2: ", basemodel2_action)     
            print("AMBULANCE lane: ", ambulance_side) 
    return fms_finetuned, fms_base

def main():
    parser = argparse.ArgumentParser(description="Run the fine-tuning experiment")
    parser.add_argument("usa_model", help="The name of the fine-tuned model for USA")
    parser.add_argument("india_model", help="The name of the fine-tuned model for India")
    parser.add_argument("--iterations", type=int, default=20, help="Number of iterations to run the experiment")
    args = parser.parse_args()
    fms_finetuned, fms_base = experiment(args.usa_model, args.india_model, args.iterations)
    print(f"Fine-tuned model failures: {fms_finetuned}")
    print(f"Base model failures: {fms_base}")

if __name__ == "__main__":
    main()



"""
USAGE
python run_experiment.py "ft:gpt-3.5-turbo-0613:personal::8HIJ0IZB" "ft:gpt-3.5-turbo-0613:personal::8HOVOV4Y" --iterations 100
where you give the two model ids after fine tuning them
Remember to do export OPENAI_API_KEY='your-api-key-here'
"""