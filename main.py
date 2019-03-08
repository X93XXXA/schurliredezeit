import time

flag = True
counter_total = 0
counter_not_talking = 0

instructions = ("\nPress enter when Schurli stops talking the next time to " +
    "start tracking his talking time.")
instructions += "\n(We know it will take a while.)"
instructions += ("\nFrom then onwards press enter every time Schurli starts " +
    "or stops talking.")
instructions += ("\nWhen (not if) you have grown tired and want to stop " +
    "tracking Schurli's taking time, please type 'stop' and press enter.")
print(instructions)

#high_score.txt must be created and an integer or float with one decimal point
#added
with open("high_score.txt", "r") as score_file:
    best_score = float(score_file.read())
    print("\nSchurli's current high score is a talking time of " +
        str(best_score) + "%.")

press_to_start = input('')
start_time_total = time.time()
start_time_not_talking = time.time()
print("Program feedback: Schurli is currently not talking.")

while flag:
    press_to_switch_state = input('')
    if press_to_switch_state != '':
        flag = False
        break
    print("Program feedback: Schurli is currently talking.")
    end_time_not_talking = time.time()
    counter_not_talking += float(end_time_not_talking -
        start_time_not_talking)
    press_to_switch_state = input('')
    if press_to_switch_state != '':
        flag = False
        break
    print("Program feedback: Schurli is currently not talking.")
    start_time_not_talking = time.time()

end_time_total = time.time()
counter_total = float(end_time_total - start_time_total)

schurli_redezeit = (1 - (counter_not_talking/counter_total)) * 100
if schurli_redezeit > best_score:
    with open("high_score.txt", "w") as score_file:
        score_file.write(str(round(schurli_redezeit, 1)))
    print("\nWow! Schurli just beat his own high score.")

print("\nDuring the observation period, Schurli spent " +
    str(round(schurli_redezeit, 1)) + "% " + "of the time talking.\n")
