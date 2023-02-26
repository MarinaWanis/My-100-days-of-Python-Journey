with open("/Users/marin/PycharmProjects/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as file:
    sample_letter = file.read()
letter_list = sample_letter.split()

with open("/Users/marin/PycharmProjects/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file:
    names = file.read()
names_list = names.split()

for each_name in names_list:
    new_letter = sample_letter.replace("[name]", each_name)
    # print(new_letter)
    with open(f"/Users/marin/PycharmProjects/Mail Merge Project Start/Output/ReadyToSend/Ready to send to {each_name}.txt", mode="w") as file:
        file.write(new_letter)
