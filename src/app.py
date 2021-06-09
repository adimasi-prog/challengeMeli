import persistance.commands
import services.databases
import services.emails
import services.users
import services.validation_engine

# Importing
persistance.commands.create_schema()
services.databases.import_and_store_databases()
services.users.import_and_store_user_managers()

# Processing
services.validation_engine.execute_validation_process()

# Email sending
services.emails.send_pending_emails()