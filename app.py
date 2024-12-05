from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    # Get the current time to display a personalized greeting
    current_time = datetime.now()
    current_hour = current_time.hour
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Generate a greeting based on the time of day
    if 5 <= current_hour < 12:
        greeting = "Good morning"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon"
    elif 18 <= current_hour < 22:
        greeting = "Good evening"
    else:
        greeting = "Good night"
    
    # Add extra personalized message
    personalized_message = f"Hello PradeepIT, {greeting}! The current time is {formatted_time}."
    
    # Fun fact or inspirational quote
    fun_fact_or_quote = "Did you know? The Earth travels around the Sun at an average speed of 29.78 km/s!"
    
    # Return both plain text and JSON response
    response = {
        "message": personalized_message,
        "timestamp": formatted_time,
        "fun_fact_or_quote": fun_fact_or_quote
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
