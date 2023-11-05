import openai
def gpt_4_vision_outputs():
    ambulance_side_right = [
        "An ambulance is reflected in the vehicle's right side mirror, coming up from the right rear. It is a 2 lane road. Output discrete moves.",
        "In the vehicle's right mirror, an ambulance is seen approaching from the back right side. It is a 2 lane road. Output discrete moves.",
        "The reflection in the right-hand side mirror shows an ambulance approaching from the right. It is a 2 lane road. Output discrete moves.",
        "A vehicle’s right side-view mirror captures an ambulance approaching from the right rear. It is a 2 lane road. Output discrete moves.",
        "The right side-view mirror of the car displays an ambulance advancing from the right. It is a 2 lane road. Output discrete moves.",
        "Approaching from the right, an ambulance is visible in the car's right wing mirror. It is a 2 lane road. Output discrete moves.",
        "An ambulance is seen in the rearview mirror on the right, indicating it's coming from behind on the right. It is a 2 lane road. Output discrete moves.",
        "The car's right mirror shows the reflection of an ambulance coming up on the right side. It is a 2 lane road. Output discrete moves.",
        "An ambulance is approaching from the right side, as reflected in the right-hand side-view mirror. It is a 2 lane road. Output discrete moves.",
        "Through the right-hand side mirror of a vehicle, an ambulance can be seen coming from the right. It is a 2 lane road. Output discrete moves.",
        "The right exterior mirror of a vehicle reflects an approaching ambulance from the right. It is a 2 lane road. Output discrete moves.",
        "Visible in the right side rearview mirror is an ambulance drawing near from the vehicle's right. It is a 2 lane road. Output discrete moves.",
        "An ambulance is detected in the right-hand mirror, signaling its approach from the vehicle’s right rear. It is a 2 lane road. Output discrete moves.",
        "The right mirror of the vehicle reflects an ambulance nearing from the right-hand side. It is a 2 lane road. Output discrete moves.",
        "An ambulance is mirrored in the right side-view mirror, signaling its approach from the right. It is a 2 lane road. Output discrete moves.",
    ]

    ambulance_side_center = [
        "An ambulance is centered directly behind the vehicle in the rearview mirror. It is a 2 lane road. Output discrete moves.",
        "The rearview mirror reflects an ambulance situated directly behind the vehicle. It is a 2 lane road. Output discrete moves.",
        "Directly behind the vehicle, the rearview mirror shows the front of an ambulance. It is a 2 lane road. Output discrete moves.",
        "An ambulance is in full view in the rearview mirror, positioned straight behind. It is a 2 lane road. Output discrete moves.",
        "The vehicle's rearview mirror captures an ambulance directly at the rear, with no side offset. It is a 2 lane road. Output discrete moves.",
        "In the rearview mirror, there is an ambulance aligned centrally behind the vehicle. It is a 2 lane road. Output discrete moves.",
        "Viewed in the rearview mirror, an ambulance is placed squarely behind the car. It is a 2 lane road. Output discrete moves.",
        "An ambulance is trailing straight behind the vehicle, as seen in the rearview mirror. It is a 2 lane road. Output discrete moves.",
        "The rearview mirror presents an ambulance directly behind the vehicle on a two-lane road. It is a 2 lane road. Output discrete moves.",
        "An ambulance follows right behind the vehicle, centered in the rearview mirror's reflection. It is a 2 lane road. Output discrete moves.",
        "The rearview mirror reveals an ambulance directly behind, maintaining a central position. It is a 2 lane road. Output discrete moves.",
        "An ambulance appears directly behind in the center of the rearview mirror image. It is a 2 lane road. Output discrete moves.",
        "The mirror shows an ambulance maintaining a direct path behind the vehicle. It is a 2 lane road. Output discrete moves.",
        "A centrally located ambulance in the rearview mirror is directly behind the vehicle. It is a 2 lane road. Output discrete moves.",
        "In the vehicle's rearview mirror, an ambulance is distinctly visible directly to the rear. It is a 2 lane road. Output discrete moves.",
    ]

    ambulance_side_left = [
        "An emergency vehicle with blue lights is approaching from the left side in the rearview mirror. It is a 2 lane road. Output discrete moves.",
        "The rearview mirror shows an ambulance with flashing lights on the left, coming up from behind. It is a 2 lane road. Output discrete moves.",
        "In the rearview mirror, a blue-lit emergency vehicle is visible on the left, moving closer. It is a 2 lane road. Output discrete moves.",
        "A vehicle with emergency lights is approaching in the left lane behind, seen in the mirror. It is a 2 lane road. Output discrete moves.",
        "The rearview mirror captures an ambulance in the left lane, flashing blue lights, and advancing. It is a 2 lane road. Output discrete moves.",
        "An ambulance with active sirens and lights is spotted in the rearview mirror to the left. It is a 2 lane road. Output discrete moves.",
        "The rearview mirror reflects an emergency vehicle with blue lights on the left, nearing. It is a 2 lane road. Output discrete moves.",
        "A fast-approaching ambulance with blue lights on is seen in the left lane via the rearview mirror. It is a 2 lane road. Output discrete moves.",
        "An emergency response vehicle with flashing lights is advancing on the left, in the mirror's view. It is a 2 lane road. Output discrete moves.",
        "Visible in the rearview mirror is an ambulance on the left, with blue lights flashing, approaching. It is a 2 lane road. Output discrete moves.",
        "The rearview mirror reveals a blue-lit emergency vehicle approaching on the left side. It is a 2 lane road. Output discrete moves.",
        "An emergency vehicle with blue flashing lights is coming up on the left side, reflected in the mirror. It is a 2 lane road. Output discrete moves.",
        "The mirror shows an ambulance with blue emergency lights on the left, moving closer. It is a 2 lane road. Output discrete moves.",
        "Approaching from the left in the rearview mirror is an emergency vehicle with distinctive blue lights. It is a 2 lane road. Output discrete moves.",
        "The rearview mirror displays an ambulance with flashing blue lights in the left lane behind the vehicle. It is a 2 lane road. Output discrete moves.",
    ]
    return ambulance_side_center, ambulance_side_right, ambulance_side_left

