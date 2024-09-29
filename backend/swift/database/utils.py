import sqlite3

from .record import User, Dialog
from .sqlcom.insert import insert_user_sql, insert_dialog_sql
from .sqlcom.select import select_user_sql, select_dialog_sql
from .password import verify_password


DB_FILE = './swift/database/database.db'
CONN: sqlite3.Connection | None = None
C: sqlite3.Cursor | None = None

def check_db(func):
    def _check_db(*args, **kwargs):
        if CONN is None or C is None:
            init_db()
        return func(*args, **kwargs)
    return _check_db

def init_db():
    global CONN, C
    CONN = sqlite3.connect(DB_FILE)
    C = CONN.cursor()

@check_db
def close_db():
    global CONN, C
    C.close()
    CONN.close()

@check_db
def insert_user(user: User):
    C.execute(insert_user_sql(user))
    CONN.commit()

@check_db
def select_user(userinfo: dict) -> User | None:
    C.execute(select_user_sql(userinfo))
    result = C.fetchone()
    if result is None:
        return None
    user = User(
        uid=result[0],
        username=result[1],
        hashed_password=result[2],
    )
    return user


def authenticate_user(username: str, password: str):
    user: User = select_user({'username': username})
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def register_user(user: User):
    if select_user({'username': user.username}):
        return False
    insert_user(user)
    return True

@check_db
def create_dialog(user: User):
    new_dialog = Dialog(
        uid=int(user.uid),
    )
    C.execute(insert_dialog_sql(new_dialog))
    CONN.commit()
    new_dialog = select_dialog({'uid': user.uid})
    return new_dialog

@check_db
def select_dialog(dialoginfo: dict) -> Dialog | None:
    C.execute(select_dialog_sql(dialoginfo))
    result = C.fetchone()
    if result is None:
        return None
    dialog = Dialog(
        dialogid=result[0],
        uid=result[1],
    )
    return dialog

@check_db
def find_dialogs(uid):
    C.execute(f"""SELECT * FROM dialogs WHERE uid = {uid} ORDER BY dialogid DESC;""")
    return C.fetchall()

@check_db
def find_message_history(dialogid):
    C.execute(f"""SELECT * FROM messages WHERE dialogid = {dialogid} ORDER BY messageid DESC;""")
    return C.fetchall()

@check_db
def insert_message(message):
    C.execute(f"""INSERT INTO messages
        (dialogid, uid, timestamp, role, message_type, message)
        VALUES
        ({int(message.dialogid)}, {int(message.uid)}, '{message.timestamp}', '{message.role}', '{message.message_type}', '{message.message}');
        """)
    CONN.commit()