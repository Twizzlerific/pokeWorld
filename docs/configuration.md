# Configuring the PokeWorld Generator
---

<!-- toc -->

- [Output Configs](#Output-Configs)
- [HBase Configs](#HBase-Configs)
- [PQS Configs](#PQS-Configs)
- [Pokemon Configs](#Pokemon-Configs)
- [Trainer Configs](#Trainer-Configs)
- [Faker Configs](#Faker-Configs)
- [Output Formats](#Output-Formats)

<!-- tocstop -->

---


## Output Configs
| Config | Purpose | Example |
| ------ | ------- | ------- |
|OUTPUT_METHOD | Which Formatter to use | 'HBASE' |
|OUTPUT_TO_FILE | output to file boolean | True |
|OUTPUT_FILE_DIR | Output Directory | 'output/' |
|OUTPUT_FILE_NAME | Output File Prefix | "pokeWorld_Output" |
> See [Output Formats](#Output-Formats) below for more information.



## HBase Configs
| Config | Purpose | Example |
| ------ | ------- | ------- |
|HBASE_TABLE_NAME | Table on HBase | 'POKEMON_TRAINERS' |
|HBASE_SERVER | Server FQDN | 'hbase.server.example.com'|
|HBASE_SERVER_PORT | Server Port | '9090' |


## PQS Configs
| Config | Purpose | Example |
| ------ | ------- | ------- |
|PHOENIX_QUERY_SERVER | PQS Server FQDN | 'hbase.server.example.com' |
|PHOENIX_QUERY_SERVER_PORT | PQS Server Port | '8765' |
|PHOENIX_QUERY_SERVER_URI | PQS Server URI | 'http://' + PHOENIX_QUERY_SERVER + ':' + PHOENIX_QUERY_SERVER_PORT |

## Pokemon Configs
| Config | Purpose | Example |
| ------ | ------- | ------- |
|MAX_POKEMON_ID | Highest ID of Pokemon to use when randomizing | 151 |
|LOCAL_LANGUAGE_ID | Used for querying | 9 |
|VERSION_GROUP_ID | Version Group ID (Red/Blue is First Gen with id: 1) | 1   |


## Trainer Configs
| Config | Purpose | Example |
| ------ | ------- | ------- |
|MAX_TRAINER_POKEMON_LEVEL | Highest level of Randomized Pokemon | 60 |
|TRAINER_COUNT | Number of Trainers to generate on each run | 3 |

## Faker Configs
| Config | Purpose | Example |
| ------ | ------- | ------- |
|FAKER_SEED_ENABLED | Boolean to use Faker Seed | False |
|FAKER_SEED_VALUE | Value of Seed for Faker Generation | 1337 |

## Output Formats
For my initial goals, I have scripted the code based on the configuration properties `OUTPUT_METHOD` and `OUTPUT_TO_FILE`. 
The property `OUTPUT_METHOD` has a few possible options:

| Formatter | OUTPUT_TO_FILE=TRUE | OUTPUT_TO_FILE=FALSE|
| -------- | -------- | -------- |
|HBase|Creates file for `hbase shell`| Connects to HBase Thrift Server|
|Phoenix|Creates CSV File for `psql`| Connects to Phoenix Query Server|
|CSV|Creates CSV file| Prints to console|
|JSON|Creates JSON file | Prints to console|


This property primarily functions within the generator script to determine which output formatter will ingest the data. 

Additionally, the `OUTPUT_TO_FILE` property is a boolean and if set to true will create a local file which can be used for things such as hbase shell scripting or ingestion into other components such as Hive or NiFi.
> For more information see [Formatters](formatters.md)