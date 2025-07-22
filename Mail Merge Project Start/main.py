PLACEHOLDER='[name]'

with open(r"Input\Names\invited_names.txt") as names_file:
    names=names_file.readlines()

with open(r'Input\Letters\starting_letter.txt') as letter_file:
    letter_content=letter_file.read()

    for name in names:
        stripped_name=name.strip()
        new_letter=letter_content.replace(PLACEHOLDER,stripped_name)
        with open(f"./output/ReadyTosend/Letter_for_{stripped_name}.docx",mode='w') as completed_letter:
            completed_letter.write(new_letter)