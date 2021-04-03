from flask import Flask
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:test@localhost:5432/interview_db"
from models import db
migrate = Migrate(app, db)


@app.route('/create_users', methods=['POST'])
def create_users():
    """
    creates users as a fixed group, allowing re-use later
    Also allows tracking of group performance over time
    :return: ID of group
    """
    return 1


@app.route('/create_quiz', methods=['POST'])
def create_quiz():
    """
    Creates quiz using group ID
    :return: quiz id
    """
    return 1


@app.route('/answer', methods=['POST'])
def quiz_answer():
    """
    accepts and validates user answers for each question in quiz
    :return: Confirmation of answer/rejection of answeer
    """
    return 1


@app.route('/quiz_scores', methods=['GET'])
def current_scores():
    """
    end point to get current quiz scores
    :return: leaderboard JSON
    """
    return 1


@app.route('/overall_scores', methods=['GET'])
def overall_scores():
    """
    Gets scores over time for a group
    :return: leaderboard over time JSON
    """
    return 1
