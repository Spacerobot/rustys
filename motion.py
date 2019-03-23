import json


def do_discussion():
    discussion = input("Do I hear any discussion? (y/n)")
    discussion = discussion.lower()
    if discussion == 'y' or discussion == 'yes':
        pass
    elif discussion == 'n' or discussion == 'no':
        pass
    else:
        print("Please enter yes or no")
        do_discussion()


motion_text = input('Motion is: ')

seconded = input("Second?")

do_discussion()

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
