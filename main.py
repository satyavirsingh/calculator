from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():   
    return render_template('app.html') 

@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        #start pulling data from the form input
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

    #calculation IF statement
    if operation == 'add':
        sum = float(num1) + float(num2)
        return render_template('app.html', sum=sum)    

    elif operation == 'subtract':
        sum = float(num1) - float(num2)
        return render_template('app.html', sum=sum)

    elif operation == 'multiply':
        sum = float(num1) * float(num2)
        return render_template('app.html', sum=sum)

    elif operation == 'divide':
        sum = float(num1) / float(num2)
        return render_template('app.html', sum=sum)
        
    else:
        return render_template('app.html')    
       

app.run(debug=True)      