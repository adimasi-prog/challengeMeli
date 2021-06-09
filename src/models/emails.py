class Email:
    def __init__(self, row_id, to, subject, body, sent):
        self.row_id = row_id
        self.to = to
        self.subject = subject
        self.body = body
        self.sent = sent