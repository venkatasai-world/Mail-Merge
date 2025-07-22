# Personalized Letter Generator 📨

This project helps you create personalized letters for many people using one template and a list of names.

---

## 📄 What You Need

1. A letter template file:  
   `Input/Letters/starting_letter.txt`

2. A list of names file:  
   `Input/Names/invited_names.txt`

3. Python script (see below).

---

## ✍️ Example Content

### starting_letter.txt
```
Dear [name],

You are invited to our special event this weekend. Please join us and make the occasion memorable.

Best regards,  
Team Organizers
```

### invited_names.txt
```
Sai
Charn
Riyaz
Amigan
```

---

## ▶️ Python Code

```python
PLACEHOLDER = '[name]'

with open(r"Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open(r'Input/Letters/starting_letter.txt') as letter_file:
    letter_content = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./output/ReadyTosend/Letter_for_{stripped_name}.docx", mode='w') as completed_letter:
            completed_letter.write(new_letter)
```

---

## 📂 Output

After running the script, you will get 4 files in the folder:  
`output/ReadyTosend/`

- Letter_for_Sai.docx  
- Letter_for_Charn.docx  
- Letter_for_Riyaz.docx  
- Letter_for_Amigan.docx  

Each letter will have the name filled in.

---

## ✅ Use Cases

- Invitations for events  
- School/college letters  
- Personalized thank-you notes  
- Certificate message generation  

---

Just write your letter once, add names, and get multiple custom letters automatically. 🚀
