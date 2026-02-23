from src.views.menu import menuPrincipal as principal
from src.logic.etudiants.etuditants import addStudent as add
import json



add()

with open('./src/data/students.json', 'r', encoding='utf8') as f:
    datas = json.load(f)

for data in datas:
    print(data['name'])

# choix = 0

# while choix != 11:
#     choix = principal()

#     match choix :
#         case 1:
#             print('add student')
#         case 2:
#             print('add student')
#         case 3:
#             print('add student')
#         case 4:
#             print('add student')
#         case 5:
#             print('add student')
#         case 6:
#             print('add student')
#         case 7:
#             print('add student')
#         case 8:
#             print('add student')
#         case 9:
#             print('add student')
#         case 10:
#             print('add student')
#         case 11:
#             print('Au revoir')
