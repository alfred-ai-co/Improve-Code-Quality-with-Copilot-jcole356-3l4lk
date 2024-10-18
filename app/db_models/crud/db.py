from sqlalchemy.orm import Session

class DBInterface():
    def __init__(self, db: Session, model=None):
        self.db = db
        self.model = model
    
    def create(self, item):
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get(self, id: int):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        return self.db.query(self.model).all()

    def update(self, item):
        self.db.commit()
        self.db.refresh(item)
        return item
        

    def delete(self, id: int):
        item = self.get(id)
        self.db.delete(item)
        self.db.commit()
        return item
