from core.sql.db_connect import Connection

class GroupRepository(Connection):
    def getById(self,args=None):
        sql = "SELECT * FROM groups WHERE id_group = %s"
        return self._selectAll(sql, args)