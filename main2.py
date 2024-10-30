from flask import Flask, request, render_template
import yt_dlp

app = Flask(__name__)

# Home page with search form
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling search
@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    ydl_opts = {
        'quiet': True,
        'extract_flat': 'in_playlist',
        'skip_download': True,
    }
    
    # Use yt-dlp to search for videos
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        search_results = ydl.extract_info(f"ytsearch20:{query}", download=False)['entries']
    
    return render_template('search_results.html', results=search_results)


@app.route('/stream')
def stream_audio():
    query = request.args.get('q')
    url = query
    ydl_opts = {
        'format': 'bestaudio',
        'quiet': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']  # URL for streaming the audio
    
    return render_template('stream.html', audio_url=audio_url)

if __name__ == '__main__':
    app.run(debug=True)
