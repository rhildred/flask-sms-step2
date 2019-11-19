from flask import Flask
from flask import render_template
from flask import Response
from flask import request
from Game import Game
from psutil import process_iter
from signal import SIGTERM # or SIGKILL

app = Flask(__name__)

dictUsers = {}

@app.route("/sms",  methods=['POST'])
def sms():
    nPhone = request.form["from"]
    sMessage = request.form["body"]
    if nPhone not in dictUsers:
        dictUsers[nPhone] = Game()
    aResponse = dictUsers[nPhone].takeTurn(sMessage)
    sResponse = "<Response>"
    for sLine in aResponse:
        sResponse += "<Message>" + sLine + "</Message>"
    sResponse += "</Response>"
    return Response(sResponse, mimetype='text/xml')

# a route where we will display a welcome message via an HTML template
@app.route("/")
def server():
    return render_template('index.html')

if __name__ == '__main__':
    nPort = 8080

    for proc in process_iter():
        for conns in proc.connections(kind='inet'):
            if conns.laddr.port == nPort:
                proc.send_signal(SIGTERM) # or SIGKILL
    app.run(host='0.0.0.0', port=nPort)