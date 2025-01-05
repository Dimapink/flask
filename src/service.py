from flask import Flask
from flask import Response, request

from db.connection import Session
from app.adv_controller import AdvertisementView


app = Flask("adv")

@app.before_request
def before_request():
    session = Session()
    request.session = session
    
    
@app.after_request
def after_request(response: Response):
    request.session.close()
    return response

@app.errorhandler(404)
def record_not_found(e):
    return {"Error": "Not found"}, 404



adv_view = AdvertisementView.as_view("adv")

app.add_url_rule("/adv/<int:adv_id>", view_func=adv_view, methods=["GET", "DELETE", "PATCH"])
app.add_url_rule("/adv", view_func=adv_view, methods=["POST"])

app.run(host="0.0.0.0", port=8080, debug=True)