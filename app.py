from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Hi, This is the template repo and testing"

if __name__ == "__main__":
    app.run()
