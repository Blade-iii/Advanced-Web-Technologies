from flask import Flask
app = Flask =(__name__)

@app.route("/") # THis is the landing route
def hello():
    return
"""
    <h1>Quiz Example</h1>
    
    <h2>Welcome</h2>
    <p>Welcome to our simple quiz! Get ready to test your knowledge with some fun and easy questions. Whether you're here for a quick challenge or just to have a bit of fun, this quiz is designed to be lighthearted and enjoyable for everyone. No pressure—just do your best and have a great time! Let's see how many you can get right. Good luck!</p>
    <b> Do you want to play a game? </b>
    
    <a href="/q1/">Damm right i want to play a game!</a>
    
"""

@app.route("/q1/")
def q1():
    return
"""
    <h1> Question one</h1>
    <p> Which is the best university in Edinburgh?</p>
    <ul>
        <li><a href="/q2/">Edinburgh Napier</a></li>
        <li><a href="/q1w/">University of Edinburgh</a></li>
        <li><a href="/q2/">Herriot Watt</a></li>
        <li><a href="/q2/">Queen Margaret/a></li>
    </ul>

"""