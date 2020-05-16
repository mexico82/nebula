from core.sql.db_connect import Connection

class DatabaseAccessor:

    def exec(self, query, args=None):
        print("Exec database connection with query: %s" % query)
        connection = Connection()
        connection.cur.execute(query, args)
        return connection.cur

    def getUserIdFrom(self, username=None):
        SQL = "SELECT * FROM users WHERE %s"

        if username:
            SQL = SQL % ("user_nickname = '%s'" % username)
        
        return self.exec(SQL)