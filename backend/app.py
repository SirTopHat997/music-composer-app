from flask import Flask, request, jsonify
from model.music_generator import generate_music
from utils.feedback_processor import update_preferences

app = Flask(__name__)

@app.route('/generate', methods=['GET'])
def generate():
    user_id = request.args.get('user_id')
    track_url = generate_music(user_id)
    return jsonify({'track_url': track_url})

@app.route('/feedback', methods=['POST'])
def feedback():
    data = request.get_json()
    user_id = data['user_id']
    track_features = data['track_features']
    feedback = data['feedback']
    update_preferences(user_id, track_features, feedback)
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
