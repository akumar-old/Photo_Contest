from flask import Flask, render_template,request

app= Flask(__name__)

@app.route('/')
def index():
    return render_template('homepage1.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/prizes')
def prizes():
    return render_template('prizes.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/thankyou')
def thank_you():
    First = request.args.get('First')
    Last = request.args.get('Last')
    return render_template('thankyou.html',First=First,Last=Last)

if __name__=='__main__':
    app.run(debug=True)
