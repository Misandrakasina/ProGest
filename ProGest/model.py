import mysql.connector

#PROJECTS
class Project:
    def __init__(self, nomProjet,description, objectifs, DateDeb,DateFin):
        self.nomProjet = nomProjet
        self.description = description
        self.objectifs = objectifs
        self.DateDeb = DateDeb
        self.DateFin = DateFin


def get_name_project_by_id(id):
    database = mysql.connector.connect(host="localhost",user="root",password="",database="progest")
    cursor = database.cursor()
    query = "SELECT * FROM projet WHERE nomProjet=%s"
    cursor.execute(query,(id,))
    project_row = cursor.fetchone()
    return project_row


def delete_project_by_id(id_proj):
    try:
        # Connexion à la base de données
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="progest"
        )

        # Création d'un curseur pour exécuter les requêtes
        cursor = database.cursor()

        # Requête SQL pour supprimer le projet
        # Assurez-vous que 'id_projet' est le bon champ pour identifier un projet unique
        query = "DELETE FROM `projet` WHERE `projet`.`nomProjet` = %s"
        cursor.execute(query, (id_proj,))

        # Confirmation des modifications
        database.commit()

        print("Le projet a été supprimé avec succès.")

    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression du projet : {err}")
    finally:
        if database.is_connected():
            cursor.close()
            database.close()


def addNewProject(nomProjet,description,objectifs,DateDeb,DateFin) :
    try:
        database = mysql.connector.connect(host="localhost", user="root", password="", database="progest")
        cursor = database.cursor()
        cursor.execute("INSERT INTO projet VALUES (%s,%s,%s,%s,%s)", (nomProjet,
                                                                      description,
                                                                      objectifs,
                                                                      DateDeb,
                                                                      DateFin))
        database.commit()
        database.close()
        return True
    except:#erreur
        return False

def getNameProjects():
    database = mysql.connector.connect(host="localhost",user="root",password="",database="progest")
    cursor = database.cursor()
    cursor.execute("SELECT nomProjet FROM projet")
    nomProjet = cursor.fetchall()
    return nomProjet


def getAllProjects():
    database = mysql.connector.connect(host="localhost",user="root",password="",database="progest")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM projet")
    projets = cursor.fetchall()
    return projets

#USERS
def addNewUser(mail,mdp,username):
    try:
        database = mysql.connector.connect(host="localhost", user="root", password="", database="progest")
        cursor = database.cursor()
        cursor.execute("INSERT INTO utilisateur VALUES (%s,%s,%s)",(mail,mdp,username))
        database.commit()
        database.close()
        return True
    except:
        return False

def getUser():
    database = mysql.connector.connect(host="localhost",user="root",password="",database="progest")
    cursor = database.cursor()
    cursor.execute("SELECT username FROM utilisateur")
    users = cursor.fetchall()
    return users

def addNewTache(nomTache, statut, priorite,collab):
    try:
        database = mysql.connector.connect(host="localhost", user="root", password="", database="progest")
        cursor = database.cursor()
        cursor.execute("INSERT INTO taches VALUES (%s,%s,%s,%s)",(nomTache,statut,priorite,collab))
        database.commit()
        database.close()
        return True
    except:
        return False

def getAllTache():
    database = mysql.connector.connect(host="localhost",user="root",password="",database="progest")
    cursor = database.cursor()
    cursor.execute("SELECT * FROM taches")
    tache = cursor.fetchall()
    return tache
