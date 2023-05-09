from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_topic')
def add_topic():
    return render_template('add_topic.html')

@app.route('/dashboard')
def dashboard():
    # Fetch user's data...
    user_name = "Placeholder"
    topics = [{"title": "Topic 1", "progress": 50}, {"title": "Topic 2", "progress": 50}]
    checkpoints = ["Checkpoint 1", "Checkpoint 2"]
    return render_template('dashboard.html', user_name=user_name, topics=topics, checkpoints=checkpoints)

@app.route('/notes')
def notes():
    return render_template('notes.html')

if __name__ == "__main__":
    app.run(debug=True)
