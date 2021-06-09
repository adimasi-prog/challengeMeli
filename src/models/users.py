class User:
    def __init__(self, row_id, id, manager):  
        self.row_id = row_id
        self.id = id
        self.manager = manager

class UserManager:
    def __init__(self, row_id, uid, state, manager):  
        self.row_id = row_id
        self.uid = uid
        self.state = state
        self.manager = manager