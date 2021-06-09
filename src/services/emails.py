import persistance.queries
import persistance.commands

def send_email(to, subject, body):
    print(f'Email sent.\n\tTo: {to}\n\tSubject: {subject}\n\tBody: {body}')

def send_pending_emails():
    pending_emails = persistance.queries.get_all_email_pending()
    for pending_email in pending_emails:
        send_email(pending_email.to, pending_email.subject, pending_email.body)
        persistance.commands.set_email_to_sent(pending_email.row_id)