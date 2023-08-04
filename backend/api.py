from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import engine

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/api/recommendation", methods=['GET']) #/api/recommendation?title=The%20Dark%20Knight
def recommendation():
    title = request.args.get('title')
    result = engine.get_recommendation(title)
    if(result == "No Movies Found"):
        return jsonify({"status": "error", "message": "No Movies Found"}), 404
    
    return jsonify( {"movies":result} )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")