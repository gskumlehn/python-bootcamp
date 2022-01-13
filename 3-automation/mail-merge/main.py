# Opens Letter template
with open('Input\Letters\starting_letter.txt') as file:
    body = file.read()

# Creates a list of names from text file
with open(r'Input\Names\invited_names.txt') as file:
    names = file.readlines()

# Creates a Letter text document for each name, using the Letter template
for name in names:
    name = name.strip()
    new_letter = body.replace("[name]", name)
    with open(f'Output\ReadyToSend\{name}_invitation', 'w') as file:
        file.write(new_letter)