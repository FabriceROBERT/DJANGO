

# Pour un fetch depuis Firebase RealTime Database avec templates index.html

# Definition de la base de données

# config = {
#   "apiKey": "AIzaSyD79gD_10Ov5WoXxQj3apjjw9YFv3lFHFQ",
#   "authDomain": "api-project-1ab36.firebaseapp.com",
#   "databaseURL": "https://api-project-1ab36-default-rtdb.firebaseio.com",
#   "projectId": "api-project-1ab36",
#   "storageBucket": "api-project-1ab36.appspot.com",
#   "messagingSenderId": "949544521826",
#   "appId": "1:949544521826:web:f99cebde00fde7492b813b",
#   "measurementId": "G-N6GVN3CD3V"
# }

# Initialisation

# firebase=pyrebase.initialize_app(config)
# authe = firebase.auth()
# database=firebase.database()

# def index(request):
      # Acceder à la base de données 'allusers'
#     all_users = database.child('allusers').get()

#     # Conversion
#     all_users_dict = all_users.val()

#     # Liste vide pour stocker les informations
#     user_info_list = []

#     # Looping through each user and retrieving 'Nom' and 'Prenom' values
#     for user_key, user_data in all_users_dict.items():
#         nom = user_data.get('Nom', '')
#         prenom = user_data.get('Prenom', '')

#     # Definir nom et prenom de chaque utilisateurs
#         user_info = {'Nom': nom, 'Prenom': prenom}
#         user_info_list.append(user_info)

#     # Definir la variable 
#     context = {
#         'user_info_list': user_info_list,
#     }

      # Redirection vers templates/index.html
#     return render(request, 'index.html', context)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pyrebase

# Pour un fetch depuis Firebase RealTime Database avec REST API

# Definition de la base de données
config = {
  "apiKey": "AIzaSyD79gD_10Ov5WoXxQj3apjjw9YFv3lFHFQ",
  "authDomain": "api-project-1ab36.firebaseapp.com",
  "databaseURL": "https://api-project-1ab36-default-rtdb.firebaseio.com",
  "projectId": "api-project-1ab36",
  "storageBucket": "api-project-1ab36.appspot.com",
  "messagingSenderId": "949544521826",
  "appId": "1:949544521826:web:f99cebde00fde7492b813b",
  "measurementId": "G-N6GVN3CD3V"
}

#J'initialise 
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# UserListView va utiliser APIVIew pour utiliser Django REST

class UserListView(APIView):
    
    def get(self, request):
        # Acceder à la base de données 'allusers'
        all_users = database.child('allusers').get().val()
        # Liste vide pour stocker les informations
        user_info_list = []

        for user_key, user_data in all_users.items():
            # Acceder au champs 'Nom' et 'Prenom' de 'allusers'
            nom = user_data.get('Nom', '')
            prenom = user_data.get('Prenom', '')

            # Nouveau dictionnaire pour stocker {nom, prenom}
            user_info = {'Nom': nom, 'Prenom': prenom}
            # Construit les informations dans {user_info_list}
            user_info_list.append(user_info)
            # Renvoie une réponse HTTP avec les informations des utilisateurs sous forme de liste
        return Response(user_info_list, status=status.HTTP_200_OK)