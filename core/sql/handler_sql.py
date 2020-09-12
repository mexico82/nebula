class Sql_Joke:
    SQL = "SELECT * FROM jokes ORDER BY RAND() LIMIT 1"
class Sql_Badword:
    SQL = "SELECT * FROM bad_words WHERE InStr(%s, word) <> 0 AND id_group = %s"
class Sql_Badword_Select:
    SQL = "SELECT * FROM bad_words WHERE id_group = %s"
class Sql_Welcome:
    SQL = "SELECT welcome_text FROM welcome_table WHERE id_group = %s"
class Sql_Custom_Handler:
    SQL = "SELECT answer_text FROM answers WHERE question_text = %s AND id_group = %s"
class Sql_Super_Ban:
    SQL = "SELECT * FROM superban_table WHERE InStr(%s,user_id) <> 0"
class Sql_SaveUser:
    SQL = "INSERT IGNORE INTO users(user_id, user_nickname) VALUES (%s,%s)"