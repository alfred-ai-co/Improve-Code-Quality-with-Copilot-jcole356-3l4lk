class ItemNotFoundException(Exception):
    def __init__(self, item_id):
        self.message = f"Item with id {item_id} not found."
        super().__init__(self.message)

class DatabaseException(Exception):
    def __init__(self, message="A database error occurred."):
        self.message = message
        super().__init__(self.message)
