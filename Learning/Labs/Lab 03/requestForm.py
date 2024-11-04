from flask import Flask, url_for, request  # Import necessary modules from Flask

app = Flask(__name__)  # Create an instance of the Flask class

# Define a route for the root URL "/"
@app.route("/", methods=['GET', 'POST'])  # The route can accept both GET and POST requests
def account():
    # Check if the request method is POST (i.e., the form has been submitted)
    if request.method == 'POST':
        print(request.form)  # Print the form data to the console for debugging purposes
        name = request.form['name']  # Get the value of the 'name' field from the form data
        return "Hello %s" % name  # Return a greeting message with the name entered in the form
    else:
        # If the request method is GET, display the HTML form to the user
        page = '''
        <html>
        <body>
            <!-- A simple HTML form that sends a POST request back to the same URL -->
            <form action="" method="post" name="form"> 
            <label for="name">Name:</label>  <!-- Label for the input field -->
            <input type = "text" name="name" id="name"/>  <!-- Input field for the user's name -->
            <input type="submit" name="submit" id="submit"/>  <!-- Submit button to send the form -->
            </form>
        </body>
        </html>
        '''
    return page  # Return the HTML page if the request is not a POST

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # Run the Flask app with debug mode enabled, accessible on all IP addresses (host='0.0.0.0')
