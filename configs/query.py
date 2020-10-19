import configs.configuration as config
import sqlite3
import phoenixdb
import phoenixdb.cursor
import happybase


def connect_to_sqlite():
    conn = sqlite3.connect(r'generators/pokemonDB.db')
    return conn


def connect_to_phoenix():

    try:
        db = phoenixdb.connect(url=config.PHOENIX_QUERY_SERVER_URI, max_retries=2, autocommit=True)
    except Exception as e:
        print("PhoenixDB Failure Exception:\n %s" % str(e))
    else:
        return db



def connect_to_hbase():
    connection = happybase.Connection(host=config.HBASE_SERVER, port=int(config.HBASE_SERVER_PORT), autoconnect=False, transport='buffered', protocol='binary')
    connection.open()
    return connection
