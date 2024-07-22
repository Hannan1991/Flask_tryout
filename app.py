'from flask import Flask\n\napp = Flask(__name__)\n\n@app.route("/")\ndef home():\n    return "<p>Na regen, komt zonneschijn.</p>"\n\nif __name__ == "__main__":\n    app.run(port=5000, debug=True)' 
