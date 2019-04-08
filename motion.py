import json

def yes_no_query():
    result = input("y/n | yes/no")
    result = result.lower()
    if result == 'y' or result == 'yes':
        return True
    elif result == 'n' or result == 'no':
        return False
    else:
        print("Please Enter yes or no")
        return yes_no_query()


def do_discussion():
    discussion = input("Do I hear any discussion? (y/n)")
    discussion = discussion.lower()
    if discussion == 'y' or discussion == 'yes':
        # todo: implement speaking stack
        pass
    elif discussion == 'n' or discussion == 'no':
        return
    else:
        print("Please enter yes or no")
        do_discussion()


def do_motion(motion_text, motion_maker):
    print(f"Motion is {motion_text}")
    print("[confirm summary of motion is correct with motion maker and note taker]")
    input("Press any key to continue...")
    print("Do I have a second?")
    seconded = yes_no_query()
    if not seconded:
        return {
            "motion text": motion_text,
            "motion maker": motion_maker,
            "seconded": seconded
        }

    do_discussion()

    # todo: add handling for motion to table
    # todo: add handling for call to question

    yay = input("Those in favor: ")
    nay = input("Those opposed: ")
    abstain = input("Those abstaining: ")

    output_text = json.dumps({
        "motion text": motion_text,
        "motion maker": motion_maker,
        "seconded": seconded,
        "result": (yay, nay, abstain)
    })

    return output_text
