from flask import Flask, request, jsonify
import trafilatura

app = Flask(__name__)

@app.route('/extract', methods=['POST'])
def extract():
    data = request.json
    if not data or 'inputurl' not in data:
        return jsonify({'error': 'No input URL provided'}), 400

    inputurl = data['inputurl']

    try:
        downloaded = trafilatura.fetch_url(inputurl)
        if downloaded:
            content = trafilatura.extract(downloaded)
            return jsonify({'content': content})
        else:
            return jsonify({'error': 'Failed to fetch URL'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
