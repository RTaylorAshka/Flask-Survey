from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ohnooo'

questions = surveys.satisfaction_survey.questions
resposes = []



qued = 0

@app.route('/')
def survey_home():

    
    return render_template('homepage.html', title=surveys.satisfaction_survey.title, instructions=surveys.satisfaction_survey.instructions, question_num=qued)

@app.route('/question/<num>')
def get_question(num):
    global qued
    global responses

    if len(resposes) == len(questions):
        flash('Survey already completed!')
        return redirect('/thank-you')
    
    print(num)
    print(qued)

    num = int(num)

    if num != qued:
        qued = len(resposes)
        if num > len(questions):
            flash('Question not found, redirected to last question.')
        else:
            flash('Please answer questions in order.')
        return redirect(f'/question/{qued}')
        
    

    return render_template('question.html', question_num=num, question=questions[qued])

@app.route('/response-handler')
def response_handler():
    global qued
    

    
    
    resposes.append(request.args.get('user-choice'))
    
    
    


    if qued == len(surveys.satisfaction_survey.questions) - 1 or len(resposes) == len(questions):
        return redirect('/thank-you')
    
    qued = qued + 1
    
    return redirect(f'/question/{qued}')

@app.route('/thank-you')
def thank_user():
    return render_template('thanks.html')