import persistance.commands
import persistance.queries

def execute_validation_process():
    for validation in persistance.queries.get_all_validation_info():
        persistance.commands.add_validation(validation.db_name, validation.owner_email, validation.manager_email, validation.classification)
        if validation.is_high_classification():
            persistance.commands.add_pending_email(validation.manager_email, 'Approval required', 'Your approval has been request.')