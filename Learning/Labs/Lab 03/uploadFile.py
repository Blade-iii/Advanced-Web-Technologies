from flask import Flask, request  # Import necessary modules from Flask

app = Flask(__name__)  # Create an instance of the Flask class

# Define a route for handling file uploads at "/account/"
@app.route("/", methods=['POST', 'GET'])  # Accept both POST and GET requests
def account():
    if request.method == 'POST':  # If the request method is POST (file upload)
        f = request.files['datafile']  # Retrieve the file from the form using 'datafile' as the field name
        f.save('Lab 03\\static\\uploads\\' + f.filename)  # Using double backslashes
        return "File Uploaded"  # Return a success message after saving the file
    else:  
        page = '''
        <html>
        <body>
            <!-- Form to upload a file -->
            <form action="" method="post" name="form" enctype="multipart/form-data">
                <input type="file" name="datafile" />  <!-- File input field -->
                <input type="submit" name="submit" id="submit"/>  <!-- Submit button to send the file -->
            </form>
        </body>
        </html>
        '''
        return page, 200  # Display the form with HTTP status code 200 (OK)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)  # Run the Flask app with debug mode enabled, accessible on all IP addresses (host='0.0.0.0')
