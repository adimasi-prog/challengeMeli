class DatabaseInfo:
    def __init__(self, name, classification, owner, time_stamp):  
        self.name = name
        self.classification = classification
        self.owner = owner
        self.time_stamp = time_stamp

class DatabaseClassification:
    def __init__(self, confidentiality, integrity, availability):  
        self.confidentiality = confidentiality
        self.integrity = integrity
        self.availability = availability

class DatabaseOwner:
    def __init__(self, name, uid, email):  
        self.name = name
        self.uid = uid
        self.email = email
