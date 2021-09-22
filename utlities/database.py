from flask_sqlalchemy import SQLAlchemy
from flask import redirect
lastGameId = -1
def deleteData(Game,db,id):
    task_to_delete = Game.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/liked_games')
    except:
        return 'There was a problem deleting that task'
def queryData(Game):
    return Game.query.all()
def addEntry(game,db):
    try:
        db.session.add(game)
        db.session.commit()
        return 'Success'
    except:
        return 'Faliure' 

def deleteEntry(game,db):
    try:
        db.session.delete(game)
        db.session.commit()
        return 'Sucess'
    except:
        return 'Faluire'

