from api import API

app = API()


@app.route("/home")
def home(request, response):
    response.text = "Hello from the HOME page"


@app.route("/about")
def about(request, response):
    response.text = "Hello from the ABOUT page"


@app.route("/hello/{person_name}")
def hello(request, response, person_name):
    response.text = f"Hello, {person_name}"
