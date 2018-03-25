from flask import Flask, render_template, jsonify, Blueprint
import nano

####################################### CONFIG ########################################

#(optional) Enter different root path (ex. /nano-node-status)
root='/'
#(optional) Enter different port number
port=7575
#(optional) Enter different title for the page
title = 'Nano Node Monitor'

#Enter RPC address for your node (keep the same if it is hosted on the same server)
rpc = nano.rpc.Client('http://ip6-localhost:7076')
#Enter your representative address
acc = 'xrb_1stuntsgoycyqjdzszzzkqj3nzyj44kgtxt7prf6sapo37tb7znp3h7usw7w'

#Add any additional links you would like to show who you are
#Simply add a comma to the last line, then copy the format and fill in accordingly
#Only the name is displayed and link will open if clicked
owner_info = [
    {"name":"Stunts", "link":""},
    {"name":"Reddit", "link":"https://www.reddit.com/user/quiteCryptic/overview"}
]

################################# END CONFIG ########################################

bp = Blueprint('node', __name__, template_folder='templates', static_folder='static')
app = Flask(__name__)
app.register_blueprint(bp, url_prefix=root)

@app.route(root)
def load_page():
    return render_template('template.html', title=title, account=acc, owner_info=owner_info, root=root)

@app.route(root+"info")
def get_info():
	try:
		version = rpc.version()["node_vendor"].split()[1]
		acc_info = rpc.account_info(acc, True, True, True)
		peers = len(rpc.peers())
		blocks = rpc.block_count()
		return jsonify(
			account=acc,
			representative=acc_info["representative"],
			balance=acc_info["balance"],
			weight=acc_info["weight"],
			peers=peers,
			blocks=blocks["count"],
			unchecked=blocks["unchecked"],
			version=version,
			status="ONLINE"
		)
	except Exception:
		return jsonify (
			status="OFFLINE"
		)  

if __name__ == '__main__':
    app.run(port=port)

