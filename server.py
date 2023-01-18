from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')    

@app.route("/<string:page_name>")
def index_page(page_name):
    return render_template(page_name)



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong !!"
        
def write_to_file(data):
    with open('database.txt', 'a') as file:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', 'a') as csv_file:
        
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv.writer
        csv_data = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_data.writerow([email,subject,message])

