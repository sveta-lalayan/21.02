from flask import Flask, send_file
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Read the HTML file
    with open('contacts.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content, 200, {'Content-Type': 'text/html'}

if __name__ == '__main__':
    app.run(debug=True)