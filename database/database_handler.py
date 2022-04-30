import os
import sqlite3
import datetime


class DatabaseHandler:
    def __init__(self, database_name: str):
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{database_name}")
        self.con.row_factory = sqlite3.Row

    def set_tempMute(self, user_id: int, guild_id: int, expiration: datetime.datetime):
        cursor = self.con.cursor()
        query = "INSERT INTO tempMute (user_id, guild_id, expiration) VALUES (?, ?, ?);"
        cursor.execute(query, (user_id, guild_id, expiration))
        cursor.close()
        self.con.commit()

    def verif_tempMute(self, guild_id: int) -> [dict]:
        cursor = self.con.cursor()
        query = f"SELECT * FROM tempMute WHERE guild_id = ? AND mute = 1 AND expiration <?;"
        cursor.execute(query, (guild_id, datetime.datetime.utcnow()))
        result = list(map(dict, cursor.fetchall()))
        cursor.close()
        return result

    def revoke_tempMute(self, tempMute_id: int):
        cursor = self.con.cursor()
        query = f"UPDATE tempMute SET mute = O WHERE id = ?;"
        cursor.execute(query, (tempMute_id,))
        cursor.close()
        self.con.commit()

# ------------------------------------------------------------------------------------------------------------------

    def set_tempBan(self, user_id: int, guild_id: int, expiration: datetime.datetime):
        cursor = self.con.cursor()
        query = ""
        cursor.execute(query, (user_id, guild_id, expiration))
        cursor.close()
        self.con.commit()
