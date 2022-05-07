
with open("../MailMerge/Input/Letters/starting_letter.txt") as letter:
    x = letter.read()
with open("../MailMerge/Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        new_name = name.strip()
        written_letter = x.replace("[name]", f"{new_name}")
        with open(f"../MailMerge/Output/ReadyToSend/{new_name}", mode="w") as wwe:
            wwe.write(written_letter)











    
