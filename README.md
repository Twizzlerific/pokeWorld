**_pokéWorld_** is an [Apache HBase](http://hbase.apache.org/book.html) proof of concept and stress test that generates a large amount of fake data. It uses the [Faker](https://github.com/joke2k/faker) library to generate data for our 'Trainers' and then uses data sourced from [Veekun's Pokedex](https://github.com/veekun/pokedex) dataset to randomly assign each Trainer pokemon.

![pokeworld](docs/assets/pokeworld.png)

---

<!-- toc -->

- [Overview](#Overview)
- [Implementation](#Implementation)
- [Getting Started](#Getting-Started)
- [Output Formats](#Output-Formats)
- [Use Cases](#Use-Cases)
- [Next Goals](#Next-Goals)
- [Credits](#Credits)

<!-- tocstop -->

---

## Overview
[Apache HBase](http://hbase.apache.org/book.html) is an open-source distributed big data store. It can be used to store billions of rows with millions of column data points. Our goal is to create meaningful data about 'Trainers' and their Pokemon that can be ingested into HBase or exported into other formats (such as CSVs and JSONs) for other components.

## Implementation

Each row represents a 'Trainer' which has been randomly assigned between 1-6 pokemon. Each row has two column families: BIO and PKM. The 'BIO' column family contains keys for things such as the 'NAME', 'AGE', 'ADDRESS', and 'SSN' while the 'PKM' family will contain the stats for each Pokemon such as the 'HP', 'TYPE', 'ABILITY', and four 'MOVES' randomly selected from the available moves for the Pokemon at that level.

>**_pokeWorld_** currently works by using the included SQLite DB to query values about each pokemon up to the configured `MAX_POKEMON_ID`. The default is `151` to capture the first 151 released along with Pokémon Red/Blue back in 1998. 

For a row key, I used the first two letters of the randomly generated FIRSTNAME and LASTNAME followed by the last four digits of the randomly generated SSN. For example: 

```
FIRST_NAME: James
LAST_NAME: Flynn
SSN: 533-58-6030
ROWKEY: JAFL6030
```


> For more information see [Fields](docs/fields.md)

## Getting Started
With version 1.0, the process starts by editing the configuration file configs/configuration.py to decide the number of new rows to create under `TRAINER_COUNT` as well as the `OUTPUT_METHOD` to determine how the script will format the data and where it will send the records. 

Once the configurations have been set, we will need to create the tables. 
> See the CREATE statement in the [Tables Guide](docs/working_with_tables.md).


Once the tables are created should be able to kick off the generator script. 

> Note: You can install the dependencies on your system or use the virtualenv 

System Install:
```bash
# pip install -r requirements.txt
# python generators/generator.py
```

Virtual Environment:
```bash
# source venv/bin/activate
# venv/bin/python generators/generator.py
```

To run in the background, `nohup` can be used. To run multiple generators at a time run using:

`nohup python generator.py &`

The script should randomly generate user data, format the data, and (if specified via the configuration) connect to the necessary servers to upload the data. 


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
> For more information see [Formatters](docs/formatters.md)

## Use Cases
Beyond being a not to subtle nod to one of my favorite franchies by [Nintendo](https://www.nintendo.com/), I saw this as an opportunity to bring my relevance to the data when learning about HBase. The generation also has the potential for testing a deployment with a large dataset (>1 million rows with over 150 columns). 

>This project is still very much in it's infancy as I still need to test expanding it beyond the first 151 as well as testing the implementation for other languages and geos.

## Next Goals

In the future, I have a list of changes I would like to implement to expand this project. Check back as this will undoubtedly grow:
- [ ] Create 'POKEDEX' table to capture all pokemon-specific data
- [ ] Script 'Manipulators' scripts for updating data
- [ ] Learn Python logger to create log files
- [ ] Learn Flask
- [ ] Create Web Front-end with Flask
  - [ ] Allow user login
  - [ ] Trainer Creation w/ Pokemon Selection
- [ ] Create Concurrency for quicker performance
- [ ] Introduce PokeBattles
- [ ] Create YARN Service
- [ ] Expand Data set with 'data' column including JSON of all data

For the most part, I tried to ensure the rest of the script will check for available fields instead of assuming (though there may be some lingering bits from testing)


---
## Credits
- [Faker](https://github.com/joke2k/faker)
- [Veekun's Pokedex](https://github.com/veekun/pokedex)
- [Nintendo](https://www.nintendo.com/)

__DISCLAIMER:__
Pokemon is the intellectual property of Nintendo and GAME FREAK. The author assumes no right to this data and the use is purely for education. 