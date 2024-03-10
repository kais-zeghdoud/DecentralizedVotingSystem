from App import app, ganache
import threading

def run_flask_app():
    app.run(port=3000, debug=True)

if __name__ == "__main__":
    blockchain = threading.Thread(target=ganache.launch_blockchain)
    blockchain.start()

    app.run(port=3000, debug=True)

    '''flask_app = threading.Thread(target=run_flask_app)
    flask_app.start()'''

