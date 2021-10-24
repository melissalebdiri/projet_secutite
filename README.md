# Description du projet :
le projet réalisé est une application  de gestion d’utilisateur, elle permet de créer des utilisateurs et de vérifier l'authentification de ces derniers.
# Mise en place :

- Création d'un Virtual Env Python :

    ```python3 -m venv dir_my_env```
	
- Activation du vertual Env :

    ```source dir_my_env/bin/activate```
- Installations des modules :
 
    ```pip install -r requirements.txt```
- Création de la base de données des utilisateurs :

    ```from __init__import creat_app```
 
    ```from models import db```
 
    ```db.creat_all(app=create_app())```
- Lancement de l'application :

    ```python app_securite.py```
    
![plot](../main/captures/capture_console.png)
- connexion à l'application :
	
	ouvrez votre navigateur et accéder à l'application en utilisant l'Ulr fourni par le terminal 
	
![plot](../main/captures/capture_app.png)
