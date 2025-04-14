from flask import Flask, app, request
from uuid import uuid1, UUID

app=Flask(__name__)

@app.route("/health")
def hello():
    return "search server is up"

@app.route("/document", methods=["POST"])
def document()->UUID:
    text= request.get_data().decode("utf-8")
    return f"{uuid1()}:{text}"

if __name__ == "__main__":
    app.run()