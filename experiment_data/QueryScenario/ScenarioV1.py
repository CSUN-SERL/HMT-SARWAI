# coding: utf-8

# q_type
#
# - tagging = 0         --confidence = is it human
# - audio = 1           --confidence = is it human
# - Path = 2            --confidence = confidence in direction
# - Save me = 3         --confidence = how critical it is
# - Tracking = 4        --confidence = confidence in identical human
# - Task = 5            --confidence = which task robot should do
#
#
# Action
#
# - full autonomous = 2
# - semi-autonomous = 1
# - not autonomous = 0

import pandas as pd
import random
import time
query = 0
start = 0
def scenenario():


    def q_static_generator(q_type=random.randint(0, 6),
                           q_conf=random.random(),
                           q_start=time.time()):
        return q_start, q_type, q_conf


    def determine_action(q_type,
                         q_conf,
                         q_start):

        #call things here?
        def action(q_type, q_conf, q_start):
            #do stuff replace if statement
            action = 0
            return action

        #replace
        if q_conf < .33:
            action = 0
            q_service_time = q_start + random.randrange(6, 9)
        elif q_conf < .66:
            action = 1
            q_service_time = q_start + random.randrange(3, 6)
        else:
            action = 2
            q_service_time = q_start + random.randrange(1, 3)
        #replace

        return q_service_time, action

    global query
    global start
    while True:

        #query 0
        if query is 0:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=0, q_conf=.33)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 1
        if query is 1:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=1, q_conf=.45)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 2
        if query is 2:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=0, q_conf=.89)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 3
        if query is 3:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=3, q_conf=.12)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 4
        if query is 4:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=5, q_conf=.99)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 5
        if query is 5:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=4, q_conf=.32)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 6
        if query is 6:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=4, q_conf=.95)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 7
        if query is 7:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=2, q_conf=.93)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 8
        if query is 8:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=5, q_conf=.19)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 9
        if query is 9:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=1, q_conf=.91)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 10
        if query is 10:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=2, q_conf=.03)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 11
        if query is 11:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=3, q_conf=.99)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 12
        if query is 12:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=0, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 13
        if query is 13:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=1, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 14
        if query is 14:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=2, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 15
        if query is 15:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=3, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 16
        if query is 16:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=4, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 17
        if query is 17:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=5, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 18
        if query is 18:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=0, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        #query 19
        if query is 19:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=1, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            query+=1
            start += q_service_time
            yield (round(start - q_service_time,2), round(q_service_time,2), q_type, q_conf, action)

        while True:
            start,  q_type, q_conf = q_static_generator(q_start= start, q_type=1, q_conf=.50)
            q_service_time, action  = determine_action(start,  q_type, q_conf)
            start += q_service_time
            yield (round(start - q_service_time,0), round(q_service_time,2), q_type, q_conf, action)

        print(data)
        break
if __name__ == "__main__":
    for x in range(22):
        print(next(scenenario()))

