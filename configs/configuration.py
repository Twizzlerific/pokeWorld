# For Future expansion on output Method : HBASE, PHOENIX, CSV, JSON
OUTPUT_METHOD = 'HBASE'
OUTPUT_TO_FILE = True
OUTPUT_FILE_NAME = 'pokeWorldOutput'  # Do not append file format (done by generator)

# HBASE Configs for hbase thrift connections
HBASE_TABLE_NAME = 'POKEMON_TRAINERS'
HBASE_SERVER = 'hbase.server.example.com'  # hbase.server.example.com
HBASE_SERVER_PORT = '1337'  # default is 9090

# Phoenix Configs for Phoenix Query Server
# Query Server URI Syntax: http://PHOENIX_QUERY_SERVER:PHOENIX_QUERY_SERVER_PORT
PHOENIX_QUERY_SERVER = 'hbase.server.example.com'
PHOENIX_QUERY_SERVER_PORT = '8765'
PHOENIX_QUERY_SERVER_URI = 'http://' + PHOENIX_QUERY_SERVER + ':' + PHOENIX_QUERY_SERVER_PORT

# TRAINER CONFIGS
MAX_TRAINER_POKEMON_LEVEL = 60  # Max level for random Pokemon
TRAINER_COUNT = 1  # Number of trainers to create

# POKEMON CONFIGS
MAX_POKEMON_ID = 151  # 151 would be gen1 of red/blue
LOCAL_LANGUAGE_ID = 9  # English
VERSION_GROUP_ID = 1  # First generation (Red/Blue)
