from app import app
 
 
@app.route('/')
def home():
    return "Ink says 'Hello world!'"