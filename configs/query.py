import config
import sqlite3
import phoenixdb
import phoenixdb.cursor
import happybase


def connect_to_sqlite():
    conn = sqlite3.connect(r'./pokemonDB.db')
    return conn


def connect_to_phoenix():
    db = phoenixdb.connect(config.PHOENIX_QUERY_SERVER, max_retries=2, autocommit=True)
    return db


def connect_to_hbase():
    connection = happybase.Connection(host=config.HBASE_SERVER, port=int(config.HBASE_SERVER_PORT), autoconnect=False)
    connection.open()

    return connection
