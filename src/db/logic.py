from flask import abort, request
from db.models import Advertisements


def get_adv_by_id(adv_id: int, session):
    "Получение объявления по id"
    adv = session.query(Advertisements).filter_by(id=adv_id).first()
    if not adv:
        abort(404)
    return adv


def create_adv(adv_to_add: Advertisements):
    "Создание обновление объявдения"
    request.session.add(adv_to_add)
    request.session.commit()


def delete_adv(adv_id: int, session):
    adv_to_delete = get_adv_by_id(adv_id, session)
    session.delete(adv_to_delete)
    session.commit()
    

def update_adv(adv_id: id, session, updates: dict):
    adv_to_update = get_adv_by_id(adv_id, session)
    
    for key, value in updates.items():
        setattr(adv_to_update, key, value)
        
    session.commit()
    return get_adv_by_id(adv_id, session)
    