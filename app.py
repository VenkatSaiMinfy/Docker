from flask import Flask, request, render_template_string

app = Flask(__name__)

form_html = '''
    <h1>Welcome to My Website!</h1>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template_string(form_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)