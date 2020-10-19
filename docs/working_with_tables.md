---

<!-- toc -->

- [Creating Tables](#Creating-Tables)
  * [Creating Tables in HBase](#Creating-Tables-in-HBase)
  * [Creating Table for Phoenix](#Creating-Table-for-Phoenix)
- [Querying Examples](#Querying-Examples)

<!-- tocstop -->

---

## Creating Tables

### Creating Tables in HBase

From the HBase shell we can create the desired table name and column families:

```shell
> hbase shell 
...
create 'POKEMON_TRAINERS', 'BIO', 'PKM'
```


### Creating Table for Phoenix

We create the table for Phoenix by defining each column and the data type using the syntax: 

`columnFamiliy`.`columnName` `dataType`,

for example:
`PKM.POKEMON_1_ABILITY_2 VARCHAR`

Along with this, we want to specify the `PRIMARY_KEY` which is how HBase will sort the rows. We can use the following statement to create set up the table on Phoenix:

```
CREATE TABLE POKEMON (BIO.ADDRESS VARCHAR, BIO.AGE INTEGER, BIO.BIRTH_DATE VARCHAR, BIO.BIRTH_DAY INTEGER, BIO.BIRTH_MONTH INTEGER, BIO.BIRTH_YEAR INTEGER, BIO.BLOOD_TYPE VARCHAR, BIO.FIRST_NAME VARCHAR, BIO.GENDER VARCHAR, BIO.HOME_STATE VARCHAR, BIO.HOME_ZIP INTEGER, BIO.JOB VARCHAR, BIO.LAST_NAME VARCHAR, BIO.MAIL VARCHAR, BIO.NAME VARCHAR, BIO.POKEMON INTEGER, BIO.SSN VARCHAR, UID VARCHAR NOT NULL PRIMARY KEY, PKM.POKEMON_1_ABILITY_1 VARCHAR, PKM.POKEMON_1_ABILITY_2 VARCHAR, PKM.POKEMON_1_EVOLUTION_CHAIN_ID INTEGER, PKM.POKEMON_1_EVOLVES_FROM_SPECIES_ID INTEGER, PKM.POKEMON_1_EVOLVES_FROM_SPECIES_NAME VARCHAR, PKM.POKEMON_1_EVOLVES_TO_SPECIES_ID INTEGER, PKM.POKEMON_1_EVOLVES_TO_SPECIES_NAME VARCHAR, PKM.POKEMON_1_GENERATION_ID INTEGER, PKM.POKEMON_1_HEIGHT INTEGER, PKM.POKEMON_1_HIDDEN_ABILITY VARCHAR, PKM.POKEMON_1_ID INTEGER, PKM.POKEMON_1_LEVEL INTEGER, PKM.POKEMON_1_MOVE_1 VARCHAR, PKM.POKEMON_1_MOVE_1_PROSE VARCHAR, PKM.POKEMON_1_MOVE_2 VARCHAR, PKM.POKEMON_1_MOVE_2_PROSE VARCHAR, PKM.POKEMON_1_MOVE_3 VARCHAR, PKM.POKEMON_1_MOVE_3_PROSE VARCHAR, PKM.POKEMON_1_MOVE_4 VARCHAR, PKM.POKEMON_1_MOVE_4_PROSE VARCHAR, PKM.POKEMON_1_NAME VARCHAR, PKM.POKEMON_1_NATURE VARCHAR, PKM.POKEMON_1_SPECIES_ID INTEGER, PKM.POKEMON_1_SPECIES_NAME VARCHAR, PKM.POKEMON_1_TYPE_1 VARCHAR, PKM.POKEMON_1_TYPE_2 VARCHAR, PKM.POKEMON_1_WEIGHT INTEGER, PKM.POKEMON_2_ABILITY_1 VARCHAR, PKM.POKEMON_2_ABILITY_2 VARCHAR, PKM.POKEMON_2_EVOLUTION_CHAIN_ID INTEGER, PKM.POKEMON_2_EVOLVES_FROM_SPECIES_ID INTEGER, PKM.POKEMON_2_EVOLVES_FROM_SPECIES_NAME VARCHAR, PKM.POKEMON_2_EVOLVES_TO_SPECIES_ID INTEGER, PKM.POKEMON_2_EVOLVES_TO_SPECIES_NAME VARCHAR, PKM.POKEMON_2_GENERATION_ID INTEGER, PKM.POKEMON_2_HEIGHT INTEGER, PKM.POKEMON_2_HIDDEN_ABILITY VARCHAR, PKM.POKEMON_2_ID INTEGER, PKM.POKEMON_2_LEVEL INTEGER, PKM.POKEMON_2_MOVE_1 VARCHAR, PKM.POKEMON_2_MOVE_1_PROSE VARCHAR, PKM.POKEMON_2_MOVE_2 VARCHAR, PKM.POKEMON_2_MOVE_2_PROSE VARCHAR, PKM.POKEMON_2_MOVE_3 VARCHAR, PKM.POKEMON_2_MOVE_3_PROSE VARCHAR, PKM.POKEMON_2_MOVE_4 VARCHAR, PKM.POKEMON_2_MOVE_4_PROSE VARCHAR, PKM.POKEMON_2_NAME VARCHAR, PKM.POKEMON_2_NATURE VARCHAR, PKM.POKEMON_2_SPECIES_ID INTEGER, PKM.POKEMON_2_SPECIES_NAME VARCHAR, PKM.POKEMON_2_TYPE_1 VARCHAR, PKM.POKEMON_2_TYPE_2 VARCHAR, PKM.POKEMON_2_WEIGHT INTEGER, PKM.POKEMON_3_ABILITY_1 VARCHAR, PKM.POKEMON_3_ABILITY_2 VARCHAR, PKM.POKEMON_3_EVOLUTION_CHAIN_ID INTEGER, PKM.POKEMON_3_EVOLVES_FROM_SPECIES_ID INTEGER, PKM.POKEMON_3_EVOLVES_FROM_SPECIES_NAME VARCHAR, PKM.POKEMON_3_EVOLVES_TO_SPECIES_ID INTEGER, PKM.POKEMON_3_EVOLVES_TO_SPECIES_NAME VARCHAR, PKM.POKEMON_3_GENERATION_ID INTEGER, PKM.POKEMON_3_HEIGHT INTEGER, PKM.POKEMON_3_HIDDEN_ABILITY VARCHAR, PKM.POKEMON_3_ID INTEGER, PKM.POKEMON_3_LEVEL INTEGER, PKM.POKEMON_3_MOVE_1 VARCHAR, PKM.POKEMON_3_MOVE_1_PROSE VARCHAR, PKM.POKEMON_3_MOVE_2 VARCHAR, PKM.POKEMON_3_MOVE_2_PROSE VARCHAR, PKM.POKEMON_3_MOVE_3 VARCHAR, PKM.POKEMON_3_MOVE_3_PROSE VARCHAR, PKM.POKEMON_3_MOVE_4 VARCHAR, PKM.POKEMON_3_MOVE_4_PROSE VARCHAR, PKM.POKEMON_3_NAME VARCHAR, PKM.POKEMON_3_NATURE VARCHAR, PKM.POKEMON_3_SPECIES_ID INTEGER, PKM.POKEMON_3_SPECIES_NAME VARCHAR, PKM.POKEMON_3_TYPE_1 VARCHAR, PKM.POKEMON_3_TYPE_2 VARCHAR, PKM.POKEMON_3_WEIGHT INTEGER, PKM.POKEMON_4_ABILITY_1 VARCHAR, PKM.POKEMON_4_ABILITY_2 VARCHAR, PKM.POKEMON_4_EVOLUTION_CHAIN_ID INTEGER, PKM.POKEMON_4_EVOLVES_FROM_SPECIES_ID INTEGER, PKM.POKEMON_4_EVOLVES_FROM_SPECIES_NAME VARCHAR, PKM.POKEMON_4_EVOLVES_TO_SPECIES_ID INTEGER, PKM.POKEMON_4_EVOLVES_TO_SPECIES_NAME VARCHAR, PKM.POKEMON_4_GENERATION_ID INTEGER, PKM.POKEMON_4_HEIGHT INTEGER, PKM.POKEMON_4_HIDDEN_ABILITY VARCHAR, PKM.POKEMON_4_ID INTEGER, PKM.POKEMON_4_LEVEL INTEGER, PKM.POKEMON_4_MOVE_1 VARCHAR, PKM.POKEMON_4_MOVE_1_PROSE VARCHAR, PKM.POKEMON_4_MOVE_2 VARCHAR, PKM.POKEMON_4_MOVE_2_PROSE VARCHAR, PKM.POKEMON_4_MOVE_3 VARCHAR, PKM.POKEMON_4_MOVE_3_PROSE VARCHAR, PKM.POKEMON_4_MOVE_4 VARCHAR, PKM.POKEMON_4_MOVE_4_PROSE VARCHAR, PKM.POKEMON_4_NAME VARCHAR, PKM.POKEMON_4_NATURE VARCHAR, PKM.POKEMON_4_SPECIES_ID INTEGER, PKM.POKEMON_4_SPECIES_NAME VARCHAR, PKM.POKEMON_4_TYPE_1 VARCHAR, PKM.POKEMON_4_TYPE_2 VARCHAR, PKM.POKEMON_4_WEIGHT INTEGER, PKM.POKEMON_5_ABILITY_1 VARCHAR, PKM.POKEMON_5_ABILITY_2 VARCHAR, PKM.POKEMON_5_EVOLUTION_CHAIN_ID INTEGER, PKM.POKEMON_5_EVOLVES_FROM_SPECIES_ID INTEGER, PKM.POKEMON_5_EVOLVES_FROM_SPECIES_NAME VARCHAR, PKM.POKEMON_5_EVOLVES_TO_SPECIES_ID INTEGER, PKM.POKEMON_5_EVOLVES_TO_SPECIES_NAME VARCHAR, PKM.POKEMON_5_GENERATION_ID INTEGER, PKM.POKEMON_5_HEIGHT INTEGER, PKM.POKEMON_5_HIDDEN_ABILITY VARCHAR, PKM.POKEMON_5_ID INTEGER, PKM.POKEMON_5_LEVEL INTEGER, PKM.POKEMON_5_MOVE_1 VARCHAR, PKM.POKEMON_5_MOVE_1_PROSE VARCHAR, PKM.POKEMON_5_MOVE_2 VARCHAR, PKM.POKEMON_5_MOVE_2_PROSE VARCHAR, PKM.POKEMON_5_MOVE_3 VARCHAR, PKM.POKEMON_5_MOVE_3_PROSE VARCHAR, PKM.POKEMON_5_MOVE_4 VARCHAR, PKM.POKEMON_5_MOVE_4_PROSE VARCHAR, PKM.POKEMON_5_NAME VARCHAR, PKM.POKEMON_5_NATURE VARCHAR, PKM.POKEMON_5_SPECIES_ID INTEGER, PKM.POKEMON_5_SPECIES_NAME VARCHAR, PKM.POKEMON_5_TYPE_1 VARCHAR, PKM.POKEMON_5_TYPE_2 VARCHAR, PKM.POKEMON_5_WEIGHT INTEGER, PKM.POKEMON_6_ABILITY_1 VARCHAR, PKM.POKEMON_6_ABILITY_2 VARCHAR, PKM.POKEMON_6_EVOLUTION_CHAIN_ID INTEGER, PKM.POKEMON_6_EVOLVES_FROM_SPECIES_ID INTEGER, PKM.POKEMON_6_EVOLVES_FROM_SPECIES_NAME VARCHAR, PKM.POKEMON_6_EVOLVES_TO_SPECIES_ID INTEGER, PKM.POKEMON_6_EVOLVES_TO_SPECIES_NAME VARCHAR, PKM.POKEMON_6_GENERATION_ID INTEGER, PKM.POKEMON_6_HEIGHT INTEGER, PKM.POKEMON_6_HIDDEN_ABILITY VARCHAR, PKM.POKEMON_6_ID INTEGER, PKM.POKEMON_6_LEVEL INTEGER, PKM.POKEMON_6_MOVE_1 VARCHAR, PKM.POKEMON_6_MOVE_1_PROSE VARCHAR, PKM.POKEMON_6_MOVE_2 VARCHAR, PKM.POKEMON_6_MOVE_2_PROSE VARCHAR, PKM.POKEMON_6_MOVE_3 VARCHAR, PKM.POKEMON_6_MOVE_3_PROSE VARCHAR, PKM.POKEMON_6_MOVE_4 VARCHAR, PKM.POKEMON_6_MOVE_4_PROSE VARCHAR, PKM.POKEMON_6_NAME VARCHAR, PKM.POKEMON_6_NATURE VARCHAR, PKM.POKEMON_6_SPECIES_ID INTEGER, PKM.POKEMON_6_SPECIES_NAME VARCHAR, PKM.POKEMON_6_TYPE_1 VARCHAR, PKM.POKEMON_6_TYPE_2 VARCHAR, PKM.POKEMON_6_WEIGHT INTEGER);
```

> Additional options are available for things like Salting, Replication, and Indexes. Check the ([Phoenix Doc](https://phoenix.apache.org/)) for more information.

### Creating Tables for Hive
Since we can ingest CSVs into Hive, the following DDL can be used to create a table to ingest Trainer data into Hive:

```
CREATE TABLE `pokemon_trainers` (`bio_address` string,`bio_age` int,`bio_birth_date` string,`bio_birth_day` int,`bio_birth_month` int,`bio_birth_year` int,`bio_blood_type` string,`bio_first_name` string,`bio_gender` string,`bio_home_state` string,`bio_home_zip` int,`bio_job` string,`bio_last_name` string,`bio_mail` string,`bio_name` string,`bio_pokemon` int,`bio_ssn` string,`uid` string,`pkm_pokemon_1_ability_1` string,`pkm_pokemon_1_ability_2` string,`pkm_pokemon_1_evolution_chain_id` int,`pkm_pokemon_1_evolves_from_species_id` int,`pkm_pokemon_1_evolves_from_species_name` string,`pkm_pokemon_1_evolves_to_species_id` int,`pkm_pokemon_1_evolves_to_species_name` string,`pkm_pokemon_1_generation_id` int,`pkm_pokemon_1_height` int,`pkm_pokemon_1_hidden_ability` string,`pkm_pokemon_1_id` int,`pkm_pokemon_1_level` int,`pkm_pokemon_1_move_1` string,`pkm_pokemon_1_move_1_prose` string,`pkm_pokemon_1_move_2` string,`pkm_pokemon_1_move_2_prose` string,`pkm_pokemon_1_move_3` string,`pkm_pokemon_1_move_3_prose` string,`pkm_pokemon_1_move_4` string,`pkm_pokemon_1_move_4_prose` string,`pkm_pokemon_1_name` string,`pkm_pokemon_1_nature` string,`pkm_pokemon_1_species_id` int,`pkm_pokemon_1_species_name` string,`pkm_pokemon_1_type_1` string,`pkm_pokemon_1_type_2` string,`pkm_pokemon_1_weight` int,`pkm_pokemon_2_ability_1` string,`pkm_pokemon_2_ability_2` string,`pkm_pokemon_2_evolution_chain_id` int,`pkm_pokemon_2_evolves_from_species_id` int,`pkm_pokemon_2_evolves_from_species_name` string,`pkm_pokemon_2_evolves_to_species_id` int,`pkm_pokemon_2_evolves_to_species_name` string,`pkm_pokemon_2_generation_id` int,`pkm_pokemon_2_height` int,`pkm_pokemon_2_hidden_ability` string,`pkm_pokemon_2_id` int,`pkm_pokemon_2_level` int,`pkm_pokemon_2_move_1` string,`pkm_pokemon_2_move_1_prose` string,`pkm_pokemon_2_move_2` string,`pkm_pokemon_2_move_2_prose` string,`pkm_pokemon_2_move_3` string,`pkm_pokemon_2_move_3_prose` string,`pkm_pokemon_2_move_4` string,`pkm_pokemon_2_move_4_prose` string,`pkm_pokemon_2_name` string,`pkm_pokemon_2_nature` string,`pkm_pokemon_2_species_id` int,`pkm_pokemon_2_species_name` string,`pkm_pokemon_2_type_1` string,`pkm_pokemon_2_type_2` string,`pkm_pokemon_2_weight` int,`pkm_pokemon_3_ability_1` string,`pkm_pokemon_3_ability_2` string,`pkm_pokemon_3_evolution_chain_id` int,`pkm_pokemon_3_evolves_from_species_id` int,`pkm_pokemon_3_evolves_from_species_name` string,`pkm_pokemon_3_evolves_to_species_id` int,`pkm_pokemon_3_evolves_to_species_name` string,`pkm_pokemon_3_generation_id` int,`pkm_pokemon_3_height` int,`pkm_pokemon_3_hidden_ability` string,`pkm_pokemon_3_id` int,`pkm_pokemon_3_level` int,`pkm_pokemon_3_move_1` string,`pkm_pokemon_3_move_1_prose` string,`pkm_pokemon_3_move_2` string,`pkm_pokemon_3_move_2_prose` string,`pkm_pokemon_3_move_3` string,`pkm_pokemon_3_move_3_prose` string,`pkm_pokemon_3_move_4` string,`pkm_pokemon_3_move_4_prose` string,`pkm_pokemon_3_name` string,`pkm_pokemon_3_nature` string,`pkm_pokemon_3_species_id` int,`pkm_pokemon_3_species_name` string,`pkm_pokemon_3_type_1` string,`pkm_pokemon_3_type_2` string,`pkm_pokemon_3_weight` int,`pkm_pokemon_4_ability_1` string,`pkm_pokemon_4_ability_2` string,`pkm_pokemon_4_evolution_chain_id` int,`pkm_pokemon_4_evolves_from_species_id` int,`pkm_pokemon_4_evolves_from_species_name` string,`pkm_pokemon_4_evolves_to_species_id` int,`pkm_pokemon_4_evolves_to_species_name` string,`pkm_pokemon_4_generation_id` int,`pkm_pokemon_4_height` int,`pkm_pokemon_4_hidden_ability` string,`pkm_pokemon_4_id` int,`pkm_pokemon_4_level` int,`pkm_pokemon_4_move_1` string,`pkm_pokemon_4_move_1_prose` string,`pkm_pokemon_4_move_2` string,`pkm_pokemon_4_move_2_prose` string,`pkm_pokemon_4_move_3` string,`pkm_pokemon_4_move_3_prose` string,`pkm_pokemon_4_move_4` string,`pkm_pokemon_4_move_4_prose` string,`pkm_pokemon_4_name` string,`pkm_pokemon_4_nature` string,`pkm_pokemon_4_species_id` int,`pkm_pokemon_4_species_name` string,`pkm_pokemon_4_type_1` string,`pkm_pokemon_4_type_2` string,`pkm_pokemon_4_weight` int,`pkm_pokemon_5_ability_1` string,`pkm_pokemon_5_ability_2` string,`pkm_pokemon_5_evolution_chain_id` int,`pkm_pokemon_5_evolves_from_species_id` int,`pkm_pokemon_5_evolves_from_species_name` string,`pkm_pokemon_5_evolves_to_species_id` int,`pkm_pokemon_5_evolves_to_species_name` string,`pkm_pokemon_5_generation_id` int,`pkm_pokemon_5_height` int,`pkm_pokemon_5_hidden_ability` string,`pkm_pokemon_5_id` int,`pkm_pokemon_5_level` int,`pkm_pokemon_5_move_1` string,`pkm_pokemon_5_move_1_prose` string,`pkm_pokemon_5_move_2` string,`pkm_pokemon_5_move_2_prose` string,`pkm_pokemon_5_move_3` string,`pkm_pokemon_5_move_3_prose` string,`pkm_pokemon_5_move_4` string,`pkm_pokemon_5_move_4_prose` string,`pkm_pokemon_5_name` string,`pkm_pokemon_5_nature` string,`pkm_pokemon_5_species_id` int,`pkm_pokemon_5_species_name` string,`pkm_pokemon_5_type_1` string,`pkm_pokemon_5_type_2` string,`pkm_pokemon_5_weight` int,`pkm_pokemon_6_ability_1` string,`pkm_pokemon_6_ability_2` string,`pkm_pokemon_6_evolution_chain_id` int,`pkm_pokemon_6_evolves_from_species_id` int,`pkm_pokemon_6_evolves_from_species_name` string,`pkm_pokemon_6_evolves_to_species_id` int,`pkm_pokemon_6_evolves_to_species_name` string,`pkm_pokemon_6_generation_id` int,`pkm_pokemon_6_height` int,`pkm_pokemon_6_hidden_ability` string,`pkm_pokemon_6_id` int,`pkm_pokemon_6_level` int,`pkm_pokemon_6_move_1` string,`pkm_pokemon_6_move_1_prose` string,`pkm_pokemon_6_move_2` string,`pkm_pokemon_6_move_2_prose` string,`pkm_pokemon_6_move_3` string,`pkm_pokemon_6_move_3_prose` string,`pkm_pokemon_6_move_4` string,`pkm_pokemon_6_move_4_prose` string,`pkm_pokemon_6_name` string,`pkm_pokemon_6_nature` string,`pkm_pokemon_6_species_id` int,`pkm_pokemon_6_species_name` string,`pkm_pokemon_6_type_1` string,`pkm_pokemon_6_type_2` string,`pkm_pokemon_6_weight` int);
```

## Querying Examples
More tuning can be done and we are only using two DataTypes (VARCHAR and INT) but here are some queries and results. I currently have 1,219,586 rows:

1: Show me the Name, Age, Name of first pokemon, Name of Second Pokemon, and the number of Pokemon for all Trainers who have a pikachu as their second Pokemon and are 55 years old. 
```
SELECT NAME, AGE, POKEMON_1_NAME, POKEMON_2_NAME, POKEMON from "POKEMON_TRAINERS" WHERE "PKM"."POKEMON_2_NAME" = 'pikachu' AND AGE = 55 ;
72 rows selected (5.535 seconds)
```

2: Show me the NAME, AGE, JOB, and Name of First pokemon of all Trainers who's first pokemon is a Fire type and they live in Florida. 


```
SELECT NAME, AGE, JOB, POKEMON_1_NAME from "POKEMON_TRAINERS_2" WHERE POKEMON_1_TYPE_1 = 'fire' AND HOME_STATE = 'FL';
1,905 rows selected (10.685 seconds)
```

3: Show me the NAME, AGE, JOB, and Name of First pokemon of all Trainers who's first pokemon is an Ice type and they live in Alaska.
```
SELECT NAME, AGE, JOB, POKEMON_1_NAME from "POKEMON_TRAINERS_2" WHERE POKEMON_1_TYPE_1 = 'ice' AND HOME_STATE = 'AK';
350 rows selected (7.153 seconds)
```
