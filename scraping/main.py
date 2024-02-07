from flask import Flask,request
from soup import scarpe_data

app = Flask(__name__)


@app.route("/getlink")
def get():
    try:
        snapchat_link = request.args.get('link')
        res = scarpe_data(snapchat_link)
        return res
    
    except Exception as ex:
        return ex



if __name__ == "__main__":
    app.run(debug=True)