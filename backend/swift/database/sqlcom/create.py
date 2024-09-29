create_users_table = """ CREATE TABLE IF NOT EXISTS users (
        uid             INTEGER PRIMARY KEY AUTOINCREMENT,
        username        text             NOT NULL,
        hashed_password text             NOT NULL
    ); """

create_dialogs_table = """ CREATE TABLE IF NOT EXISTS dialogs (
        dialogid        INTEGER PRIMARY KEY AUTOINCREMENT,
        uid             INTEGER NOT NULL
    ); """

create_messages_table = """ CREATE TABLE IF NOT EXISTS messages (
        messageid       INTEGER PRIMARY KEY AUTOINCREMENT,
        dialogid        INTEGER NOT NULL,
        uid             INTEGER NOT NULL,
        timestamp       text NOT NULL,
        role            text NOT NULL,
        message_type    text NOT NULL,
        message         text NOT NULL
    ); """
