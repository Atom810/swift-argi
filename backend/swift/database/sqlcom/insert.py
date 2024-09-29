from swift.database.record import User, Dialog

def insert_user_sql(user: User):
    insert_user_sql = f"""
        INSERT INTO users
        (username, hashed_password)
        VALUES ('{user.username}', '{user.hashed_password}');
        """
    return insert_user_sql

def insert_dialog_sql(dialog: Dialog):
    insert_dialog_sql = f"""
        INSERT INTO dialogs
        (uid)
        VALUES ('{dialog.uid}');
        """
    return insert_dialog_sql