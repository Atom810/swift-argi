def select_user_sql(userinfo: dict):
    select_user_sql = "SELECT * FROM users"
    if len(userinfo) > 0:
        select_user_sql += " WHERE"
        for key, value in userinfo.items():
            select_user_sql += f" {key} = '{value}' AND"
        select_user_sql = select_user_sql[:-4]
    return select_user_sql

def select_dialog_sql(dialoginfo: dict):
    select_dialog_sql = "SELECT * FROM dialogs"
    if len(dialoginfo) > 0:
        select_dialog_sql += " WHERE"
        for key, value in dialoginfo.items():
            select_dialog_sql += f" {key} = '{value}' AND"
        select_dialog_sql = select_dialog_sql[:-4]
    return select_dialog_sql