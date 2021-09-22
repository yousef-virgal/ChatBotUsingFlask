from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from bot import bot
from utlities import database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Game(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    description =  db.Column(db.String(10000))
    score = db.Column(db.Integer)
    backgroundImage = db.Column(db.String(600))
    playtime = db.Column(db.Integer)

    def __init__(self,id,name,description,score,backgroundImage,playtime) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.score = score 
        self.backgroundImage = backgroundImage
        self.playtime = playtime
    def __repr__(self):
        return '<game %r>' % self.id
    @classmethod
    def format(cls, game):
        return Game(game['id'],game['name'],game['description'],game['metacritic'],game['background_image'],game['playtime'])

@app.route('/')
@app.route('/home')
def index():
    return render_template('mainmenu.html')

@app.route('/chat',methods=['GET','POST'])
def chatBot(showChat=False,botAnswer=""):
    myShowChat = showChat
    myBotAnswer = botAnswer 
    if request.method == 'POST':
        myShowChat = True
        res = request.form['input']
        status,response =bot.chat(res)
        if status == 0:
            myBotAnswer = response
        else:
            myBotAnswer = 'Sorry I don\'t Know how to respond'
    return render_template('chatMenu.html',showChat=myShowChat,botAnswer=myBotAnswer)

@app.route('/liked_games')
def likedGames():
    items = database.queryData(Game)
    return render_template('likedGames.html',items=items)

@app.route('/delete/<int:id>')
def delete(id):
    return database.deleteData(Game,db,id)
    

if __name__ == "__main__":
    app.run(debug=True)