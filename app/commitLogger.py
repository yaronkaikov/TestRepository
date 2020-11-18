#!/usr/bin/env python3

import datetime
from random import randint

import mysql.connector

from config import DB_HOST, DB_NAME, DB_USER, DB_PASS

sqlConnection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME,
)


def insert_commit(commit_id, commit_message, commit_user):
    """
    Insert a row into commits table

    Args:
        commit_id (str): commit hash
        commit_message (str): commit message
        commit_user (str): committer user

    Returns:
        bool: True if row added successfully

    Example:
      insert_commit(
          commit_id="014f06897c1bbb065c98dead0eeb5734b33abd82",
          commit_message="This is a test commit message",
          commit_user="Test User",
      )

    """

    commit_time = datetime.datetime.now().strftime("%Y-%m-%d %X")

    my_cursor = sqlConnection.cursor()

    sql_insert = """
        INSERT INTO commits
        (commit_id, commit_time, commit_message, commit_user)
        VALUES (%s, %s, %s, %s)
        """
    sql_val = (commit_id, commit_time, commit_message, commit_user)
    my_cursor.execute(sql_insert, sql_val)
    if sqlConnection.commit():
        return True


def select_commit():
    """
    Select the latest commit

    """

    my_cursor = sqlConnection.cursor()

    my_cursor.execute("SELECT * FROM commits ORDER BY commit_time DESC LIMIT 1")
    print(my_cursor.fetchone())


if __name__ == "__main__":
    insert_commit(
        commit_id="53746d605c3cf3f0a929bdafbe269d7d1932f2f6",
        commit_message=f"This is a test msg {randint(0, 999999)}",
        commit_user="Test User",
    )

    select_commit()
