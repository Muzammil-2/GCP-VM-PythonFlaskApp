from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Template with a form
HTML_PAGE = """
<!doctype html>
<html>
  <head>
    <title>Greeting App</title>
  </head>
  <body>
    <h2>Enter Your Name</h2>
    <form method="post">
      <input type="text" name="username" placeholder="Your name">
      <input type="submit" value="Greet Me">
    </form>
    {% if name %}
      <h3>Hello, {{ name }}! Welcome to Flask App.</h3>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def greet():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(HTML_PAGE, name=name)

if __name__ == "__main__":
    app.run(debug=True)
