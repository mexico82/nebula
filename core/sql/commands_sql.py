class Sql_Insert_BW:
    SQL = "INSERT INTO bad_words (word, id_group) VALUES(%s,%s)"
class Sql_Insert_CH:
    SQL_1 = "SELECT * FROM answers WHERE answer_text = %s AND id_group = %s"
    SQL_2 = "INSERT INTO answers (question_text, answer_text, id_group) VALUES (%s, %s, %s)"
class Sql_Insert_J:
    SQL_1 = "SELECT * FROM jokes WHERE joke_text = %s"
    SQL_2 = "INSERT INTO jokes (joke_text) VALUES(%s)"
class Sql_Insert_W:
    SQL = "INSERT IGNORE INTO welcome_table(id_group, welcome_text, b_options) VALUES(%s,%s,%s)"
class Sql_Update_W:
    SQL = "UPDATE welcome_table SET welcome_text = %s WHERE id_group = %s"
class Sql_Pin:
    SQL = "SELECT content FROM fixed_default WHERE id_group = %s ORDER BY created_at DESC LIMIT 1"
    SQL_SET = "INSERT INTO fixed_default (content, id_group) VALUES(%s,%s)"
class Sql_Add_Buttons:
    SQL = "INSERT INTO urls (text, url, id_group) VALUES (%s, %s, %s)"
class Sql_Buttons:
    SQL_1 = "SELECT * FROM urls WHERE id_group = %s"
    SQL_2 = "DELETE FROM urls WHERE id=(%s) AND id_group = %s"
class Sql_Superban:
    SQL = "INSERT IGNORE INTO ban_table(user_id, motivation_text, user_date) VALUES (%s,%s,%s)"
class Sql_Rules:
    SQL = "SELECT rules_text FROM rules_table WHERE id_group = %s"
class Sql_Insert_Rules:
    SQL = "INSERT INTO rules_table(rules_text, id_group) VALUES (%s,%s)"