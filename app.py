from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
    <h1>Welcome to CI/CD Pipeline Demo</h1>
    <a href="/deploy">Click here</a>
    '''

@app.route("/deploy")
def deploy():
    return "deployment successful GitHub ->Jenkins ->Test ->Docker Build ->Browser"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)