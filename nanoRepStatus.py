from flask import Flask
from flask import render_template
#import requests

app = Flask(__name__)

#curl -g -d '{ "action": "version" }' 

context_root = "/"
title = 'Stunts\' Nano Node'
rpc_address = '[::1]:7076'
account = 'xrb_1stuntsgoycyqjdzszzzkqj3nzyj44kgtxt7prf6sapo37tb7znp3h7usw7w'
#payload = open("request.json")
#headers = {'content-type': 'application/json'}
#r = requests.post(url, data=payload, headers=headers)

@app.route(context_root)
def page():
    return render_template('template.html', root=context_root, title=title, account=account)

if __name__ == '__main__':
    app.run(debug=True,port=7575)