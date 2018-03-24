from flask import Flask
from flask import render_template
import nano

app = Flask(__name__)

title = 'Stunts\' Nano Node'
rpc = nano.rpc.Client('http://ip6-localhost:7076')
acc = 'xrb_1stuntsgoycyqjdzszzzkqj3nzyj44kgtxt7prf6sapo37tb7znp3h7usw7w'

@app.route("/")
def load_page():
    return render_template('template.html', title=title, account=acc)

@app.route("/info")
def get_info():
    version = (rpc.version()["node_vendor"])
    acc_info = rpc.account_info(acc, True, True, True)
    peers = len(rpc.peers())
    blocks = rpc.block_count()
    response = {
        "account":acc,
        "representative":acc_info["representative"],
        "balance":acc_info["balance"],
        "weight":acc_info["weight"],
        "peers":peers,
        "blocks":blocks["count"],
        "unchecked":blocks["unchecked"],
        "version":version
    }
    return response

if __name__ == '__main__':
    app.run(port=7575)