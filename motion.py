import json


def discussion():
    disucssion = input("Do I hear any discussion? (y/n)")
    disucssion = disucssion.lower()
    if disucssion == 'y' or disucssion == 'yes':
        pass
    elif disucssion == 'n' or disucssion == 'no':
        pass
    else:
        print("Please enter yes or no")
        discussion()


motion_text = input('Motion is: ')

seconded = input("Second?")

discussion()

yay = input("Those in favor: ")
nay = input("Those opposed: ")
abstain = input("Those abstaining: ")

output_text = json.dumps({
    "motion text": motion_text,
    "seconded": seconded,
    "result": (yay, nay, abstain)
})

output_file = open(f"{motion_text}.json", 'a')

output_file.write(output_text)
