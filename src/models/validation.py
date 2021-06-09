class Validation:
    def __init__(self, db_name, owner_email, manager_email, classification):
        self.db_name = db_name
        self.owner_email = owner_email
        self.manager_email = manager_email
        self.classification = classification

    def is_high_classification(self):
        return self.classification == 'high'
