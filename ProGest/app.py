from flask import Flask, render_template, request
from model import addNewProject, addNewUser, getNameProjects, get_name_project_by_id,delete_project_by_id, getAllTache,addNewTache

app = Flask(__name__)


@app.route("/")
def index():  # afficher formulaire de connexion
    return render_template("index.html")


@app.route('/traitement', methods=['POST'])
def traitement():
    username = request.form.get('username')
    mdp = request.form.get('mdp')
    mail = request.form.get('mail')

    if username == 'admin':
        donnees = request.form
        nomProjet = donnees.get('nomProjet')
        description = donnees.get('description')
        objectifs = donnees.get('objectifs')
        DateDeb = donnees.get('DateDeb')
        DateFin = donnees.get('DateFin')
        addNewProject(nomProjet, description, objectifs, DateDeb, DateFin)

        nomProjet = getNameProjects(),
        return render_template("home.html", nomProjet=nomProjet)

    else:
        return render_template("alert.html")


@app.route("/addProject", methods=['GET'])
def projet():  # accéder au formulaire pour créer un projet
    return render_template("addProject.html")


@app.route("/app", methods=['POST'])
def creer():  # créer un projet
    donnees = request.form
    nomProjet = donnees.get('nomProjet')
    description = donnees.get('description')
    objectifs = donnees.get('objectifs')
    DateDeb = donnees.get('DateDeb')
    DateFin = donnees.get('DateFin')
    addNewProject(nomProjet, description, objectifs, DateDeb, DateFin)

    nomProjet = getNameProjects(),
    return render_template("home.html", nomProjet=nomProjet)


@app.route("/home", methods=['GET'])
def home():
    return render_template("home.html")
@app.route("/taches",methods=['GET'])
def tache():
    return render_template("taches.html")


@app.route("/creerTache", methods=['POST'] )
def creerTache():  # créer une tache
    donnees = request.form
    nomTache = donnees.get('nomTache')
    statut = donnees.get('statut')
    priorite = donnees.get('priorite')
    collab = donnees.get('collab')
    addNewTache(nomTache, statut, priorite, collab)

    tache=getAllTache()
    return render_template("taches.html",tache=tache)


@app.route("/addTache")
def addTache():
    return render_template("addTache.html")


@app.route("/Project/<string:id>")
def project(id):
    donnees = request.form
    nomProjet = donnees.get('nomProjet')
    description = donnees.get('description')
    objectifs = donnees.get('objectifs')
    DateDeb = donnees.get('DateDeb')
    DateFin = donnees.get('DateFin')
    addNewProject(nomProjet, description, objectifs, DateDeb, DateFin)

    projet = get_name_project_by_id(id)
    return render_template("Project.html",projet=projet)



@app.route("/delete")
def delete():
    donnees = request.form
    nomProjet = donnees.get('nomProjet')
    description = donnees.get('description')
    objectifs = donnees.get('objectifs')
    DateDeb = donnees.get('DateDeb')
    DateFin = donnees.get('DateFin')

    projet= delete_project_by_id(id)
    return render_template("Project.html",projet=projet)


if __name__ == '__main__':
    app.run(debug=True)

app.run()
