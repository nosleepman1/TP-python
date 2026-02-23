import json
from pathlib import Path


def addStudent():
    name = input('saisir le nom complet:  ')
    notes_input = input('saisir note(s) (séparées par des virgules) : ')
    notes = [float(n.strip()) for n in notes_input.split(',') if n.strip()]
    age = int(input('saisir age:  '))
    major = input('major:  ')

    data = {
        "name": name,
        "notes": notes,
        "age": age,
        "major": major
    }

    file_path = Path(__file__).parent.parent.parent / 'data' / 'students.json'
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        with open(file_path, 'r', encoding='utf8') as f:
            try:
                students = json.load(f)
                if not isinstance(students, list):
                    students = []
            except json.JSONDecodeError:
                students = []
    else:
        students = []

    last_id = max((s.get('id', 0) for s in students), default=0)
    data['id'] = last_id + 1

    students.append(data)

    with open(file_path, 'w', encoding='utf8') as f:
        json.dump(students, f, indent=4, ensure_ascii=False)
