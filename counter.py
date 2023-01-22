import counter_app
from counter_app import home_page, app, show, db


@app.route('/')
def home():
    return 'raushan '


app.run(host='0.0.0.0', port=81)


