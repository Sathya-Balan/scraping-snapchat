from flask import Flask,request
from soup import scarpe_data

app = Flask(__name__)


@app.route("/getlink")
def get():
    try:
        snapchat_link = request.args.get('link')
        response = scarpe_data(snapchat_link)
        return response
    
    except Exception as ex:
        return ex



if __name__ == "__main__":
    app.run(debug=True)
