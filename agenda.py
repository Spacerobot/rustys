import motion
import json

motion_text = input("Input Motion: ")
maker = input("Name of Motion Maker: ")

minutes = []

while motion_text != '':
    minutes.append(motion.do_motion(motion_text, maker))
    motion_text = input("Input Motion: ")
    maker = input("Name of Motion Maker: ")

minutes_file = open('minutes.json', 'w')

minutes_object = {"minutes": minutes}

minutes_string = json.dumps(minutes_object)

minutes_file.write(minutes_string)
