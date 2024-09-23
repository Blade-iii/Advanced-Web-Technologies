from flask import Flask
app = Flask (__name__)

@app.route("/")  # This is the landing route
def hello():
    return """
    <h1>Quiz Example</h1>
    
    <h2>Welcome</h2>
    <p>Welcome to our simple quiz! Get ready to test your knowledge with some fun and easy questions. Whether you're here for a quick challenge or just to have a bit of fun, this quiz is designed to be lighthearted and enjoyable for everyone. No pressure—just do your best and have a great time! Let's see how many you can get right. Good luck!</p>
    <b>Do you want to play a game?</b>
    
    <a href="/q1/">Damn right, I want to play a game!</a>
    """

@app.route("/q1/")
def q1():
    return """
    <h1>Question One</h1>
    <p>Which is the best university in Edinburgh?</p>
    <ul>
        <li><a href="/q2/">Edinburgh Napier</a></li>
        <li><a href="/q1w/">University of Edinburgh</a></li>
        <li><a href="/q1w/">Herriot Watt</a></li>
        <li><a href="/q1w/">Queen Margaret</a></li>
    </ul>
    """
    
@app.route("/q1w/")
def q1w():
    return """
    <h1> Wrong answer!</h1>
    <a href="/q1/">Do you want to try again?</a>
    """
    
@app.route("/q2/")
def q2():
    return """"
    <h1>Question 2</h1>
    <p>Which is the best university in Scotland</p>
      <ul>
        <li><a href="/q3/">Edinburgh Napier</a></li>
        <li><a href="/q2w/">University of Edinburgh</a></li>
        <li><a href="/q2w/">Herriot Watt</a></li>
        <li><a href="/q2w/">Queen Margaret</a></li>
    </ul>
"""

@app.route("/q2w/")
def q2w():
    return """
    <h1> Wrong answer!</h1>
    <a href="/q2/">Do you want to try again?</a>
    """
    
@app.route("/q3/")
def q3():
    return """"
    <h1>Question 3</h1>
    <p>Which is the best university in the UK</p>
      <ul>
        <li><a href="/success/">Edinburgh Napier</a></li>
        <li><a href="/q3w/">University of Edinburgh</a></li>
        <li><a href="/q3w/">Herriot Watt</a></li>
        <li><a href="/q3w/">Queen Margaret</a></li>
    </ul>
"""

@app.route("/q3w/")
def q3w():
    return """
    <h1> Wrong answer!</h1>
    <a href="/q3/">Do you want to try again?</a>
    """
    
@app.route("/success/")
def success():
    return """
    <h1> You answered all the questions correctly!</h1>
    <a href="/">Do you want to go back to the start?</a>
    """
    
