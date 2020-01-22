from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return{'message': 'Name of Store not found'}, 404
        #GET emthod looks in db to find if store exists

    def Post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "An Store with name '{}' already exists.".format(name)},400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return{'message': "An error has occurred creating the Store."}, 500 # Internal Server Error

        return store.json(), 201

    def delete(self, name):
        store  = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store Deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
