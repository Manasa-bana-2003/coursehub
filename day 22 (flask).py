from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/register">Register Here</a>'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        return render_template_string('''
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
                <title>Registration Success</title>
              </head>
              <body>
                <div class="container mt-5">
                  <div class="alert alert-success" role="alert">
                    User {{ username }} with email {{ email }} registered successfully!
                  </div>
                  <a href="/register" class="btn btn-primary">Register Another User</a>
                </div>
              </body>
            </html>
        ''', username=username, email=email)
    else:
        return render_template_string('''
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
                <title>Register</title>
              </head>
              <body>
                <div class="container mt-5">
                  <h1 class="mb-4">Register</h1>
                  <form method="post">
                    <div class="form-group">
                      <label for="username">Username</label>
                      <input type="text" class="form-control" id="username" name="username" placeholder="Enter Username">
                    </div>
                    <div class="form-group">
                      <label for="email">Email</label>
                      <input type="email" class="form-control" id="email" name="email" placeholder="Enter Email">
                    </div>
                    <button type="submit" class="btn btn-primary">Register</button>
                  </form>
                </div>
                <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
                <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
              </body>
            </html>
        ''')

if __name__ == "__main__":
    app.run(debug=True)
