import motion

motion_text = input("Input Motion: ")
maker = input("Name of Motion Maker: ")

while motion_text != '':
    motion.do_motion(motion_text, maker)
    motion_text = input("Input Motion: ")
    maker = input("Name of Motion Maker: ")
