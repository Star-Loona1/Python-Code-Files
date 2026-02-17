'''First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest.'''

student_data = {'id1' : {'name' : 'Sarah', 'class' : 'v', 'subject_integration': 'english, maths, science'},
 'id2' : {'name' : 'David', 'class' : 'v', 'subject_integration': 'english, maths, science'},
 'id3' : {'name' : 'Sarah', 'class' : 'v', 'subject_integration': 'english, maths, science'},
 'id4' : {'name' : 'Surya', 'class' : 'v', 'subject_integration': 'english, maths, science'}}

result = {}
seen = set()

for student_id, details in student_data.items():
    unique_key = (details['name'], details['class'], details['subject_integration'])
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ':', v)