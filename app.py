from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def greet():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(HTML_PAGE, name=name)

if __name__ == "__main__":
    app.run(debug=True)
