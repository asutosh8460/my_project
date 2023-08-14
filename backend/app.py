from flask import Flask, request, jsonify, send_from_directory, render_template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/videos'
app.config['SUBTITLES_FOLDER'] = 'static/subtitles'


def allowed_video(filename):
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/api/endpoint', methods=['POST'])
def handle_frontend_data():
    data = request.json  # Get the JSON data sent from the frontend

    # Process the data and perform backend operations

    response_data = {'message': 'Data received and processed'}
    return jsonify(response_data)


@app.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video part'})

    video_file = request.files['video']
    if video_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if video_file and allowed_video(video_file.filename):
        filename = secure_filename(video_file.filename)
        video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        video_file.save(video_path)
        return jsonify({'message': 'Video uploaded successfully'})

    return jsonify({'error': 'Invalid video format'})


@app.route('/upload_subtitles', methods=['POST'])
def upload_subtitles():
    video_id = request.form.get('video_id')
    subtitles_text = request.form.get('subtitles_text')

    if not video_id or not subtitles_text:
        return jsonify({'error': 'Missing video_id or subtitles_text'})

    subtitles_filename = f"{video_id}.srt"
    subtitles_path = os.path.join(
        app.config['SUBTITLES_FOLDER'], subtitles_filename)

    with open(subtitles_path, 'w') as subtitles_file:
        subtitles_file.write(subtitles_text)

    return jsonify({'message': 'Subtitles uploaded successfully'})


@app.route('/get_subtitles/<video_id>', methods=['GET'])
def get_subtitles(video_id):
    subtitles_filename = f"{video_id}.srt"
    subtitles_path = os.path.join(
        app.config['SUBTITLES_FOLDER'], subtitles_filename)

    if os.path.exists(subtitles_path):
        with open(subtitles_path, 'r') as subtitles_file:
            subtitles_text = subtitles_file.read()
            return jsonify({'subtitles_text': subtitles_text})
    else:
        return jsonify({'error': 'Subtitles not found'})


@app.route('/video/<filename>', methods=['GET'])
def get_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
