from web import app


@app.route('/')
def home_page():
    return "See me see trouble"