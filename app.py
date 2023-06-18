from flask import Flask, render_template
import whisper

app = Flask(__name__)

@app.route('/')
def index():
    return 'index page'

@app.route('/whisper')
def transcribe():
    model = whisper.load_model("base")
    result = model.transcribe("audio.mp3")
    print(result["text"])
    return 'whisper'

if __name__ == '__main__':
    app.run()
