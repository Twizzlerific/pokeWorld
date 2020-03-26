**_pokéWorld_** is an [Apache HBase](http://hbase.apache.org/book.html) proof of concept and stress test that generates a large amount of fake data. It uses the [Faker](https://github.com/joke2k/faker) library to generate data for our 'Trainers' and then uses data sourced from [Veekun's Pokedex](https://github.com/veekun/pokedex) dataset to randomly assign each Trainer pokemon.

---

<!-- toc -->

- [Overview](#Overview)
- [Use Cases](#Use-Cases)
- [Implementation](#Implementation)
- [Getting Started](#Getting-Started)
- [Output Formats](#Output-Formats)
- [Next Goals](#Next-Goals)
- [Credits](#Credits)

<!-- tocstop -->

---

## Overview
[Apache HBase](http://hbase.apache.org/book.html) is an open-source distributed big data store. It can be used to store billions of rows with millions of column data points. Our goal is to create meaningful data about 'Trainers' and their Pokemon.

## Use Cases
Beyond being a not to subtle nod to one of my favorite franchies by [Nintendo](https://www.nintendo.com/), I saw this as an opportunity to bring my relevance to the data when learning about HBase. The generation also has the potential for testing a deployment with a large dataset (>1 million rows with over 150 columns). 

>This project is still very much in it's infancy as I still need to test expanding it beyond the first 151 as well as testing the implementation for other languages and geos.

## Implementation
**_pokeWorld_** currently works by using the included SQLite DB to query values about each pokemon up to the configured `MAX_POKEMON_ID`. The default is `151` to capture the first 151 released along with Pokémon Red/Blue back in 1998.

For the most part, I tried to ensure the rest of the script will check for available fields instead of assuming (though there may be some lingering bits from testing)


> For more information see [Fields](docs/fields.md)

## Getting Started
With version 1.0, the process starts by editing the configuration file configs/configuration.py to decide the number of new rows to create under `TRAINER_COUNT` as well as the `OUTPUT_METHOD` to determine how the script will format the data. 

Once the configurations have been set, should be able to kick off the generator script:

`# cd generators/`
`# python generator.py`


To run in the backgroun a nohup can be used with multiple iterations being run using:

`nohup python generator.py &`

The script should randomly generate user data, format the data, and (if specified via the configuration) connect to the necessary servers to upload the data. 

> For more information see [Formatters](docs/formatters.md)

## Output Formats
For my initial goals, I have scripted the code based on the configuration properties `OUTPUT_METHOD` and `OUTPUT_TO_FILE`. 
The property `OUTPUT_METHOD` has a few possible options:
- 'HBASE'
- 'PHOENIX'
- 'CSV' (COMING SOON)
- 'JSON' (COMING SOON)

This property primarily functions within the generator script to determine which output formatter will ingest the data. 

Additionally, the `OUTPUT_TO_FILE` property is a boolean and if set to true will create a local file which can be used for things such as hbase shell scripting or ingestion into other components such as Hive or NiFi.

> For more information see [Output Formats](docs/outputs.md)

## Next Goals

In the future, I have a list of changes I would like to implement to expand this project. Check back as this will undoubtedly grow:
- [ ] Create 'POKEDEX' table to capture all pokemon-specific data
- [ ] Script 'Manipulators' scripts for updating data
- [ ] Learn Python logger to create log files
- [ ] Learn Flask
- [ ] Create Web Front-end with Flask
  - [ ] Allow user login and Trainer Creation
- [ ] Create output formatter for CSV
  - [ ] Can be ingested into Hive
- [ ] Create Output formatter for JSON
  - [ ] Can be used for NiFi Workflow
- [ ] Create Concurrency for quicker performance
- [ ] Introduce PokeBattles
- [ ] Create YARN Service
- [ ] Expand Dataset with 'data' column including JSON of all data

---
## Credits
- [Faker](https://github.com/joke2k/faker)
- [Veekun's Pokedex](https://github.com/veekun/pokedex)
- [Nintendo](https://www.nintendo.com/)

__DISCLAIMER:__
Pokemon is the intellectual property of Nintendo and GAME FREAK. The author assumes no right to this data and the use is purely for education. 