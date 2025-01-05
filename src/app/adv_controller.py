from flask import jsonify, request
from flask.views import MethodView
from pydantic import ValidationError
from db.connection import Session
from db.models import Advertisements
from app.models import AdvertisementSchema
from db.logic import (
    get_adv_by_id, 
    create_adv, 
    delete_adv, 
    update_adv
)



def _validate(data):
        try:
            adv = AdvertisementSchema(**data)
            return adv
        
        except ValidationError as e:
            return None, e.json(), 400

        

    
class AdvertisementView(MethodView):
    

    def get(self, adv_id):
        adv: Advertisements = get_adv_by_id(adv_id, request.session)
        # отдаем только title, owner и description
        serialized_adv = AdvertisementSchema(**adv.dict)
        
        return jsonify(serialized_adv.model_dump())
    
    
    def post(self):
        data = request.json
        validated_data = _validate(data)
        if not isinstance(validated_data, AdvertisementSchema):
            return validated_data[1], validated_data[2]
        
        adv = Advertisements(**data)
        create_adv(adv)
            # отдаем все, что сохранили в БД
        return jsonify(adv.dict), 200
        

    def delete(self, adv_id):
        delete_adv(adv_id, request.session)
        return jsonify({"Message": f"Advertisement {adv_id} was deleted"})
    
    
    def patch(self, adv_id):
        updates = request.json
        adv = update_adv(adv_id, request.session, updates)
        # отдаем все, что сохранили в БД
        return jsonify(adv.dict)