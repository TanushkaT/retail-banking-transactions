from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This is where your SQL data will eventually go
    user_data = {"name": "Tanushka", "balance": 5000} 
    return render_template('index.html', user=user_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
