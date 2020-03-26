Brief explanation fo the various fields as well as an example of the data.

---

<!-- toc -->

- [Fields](#Fields)
- [Example Data](#Example-Data)

<!-- tocstop -->

---


## Fields
|field_name | data_type|Description|
|---|---|---|
|ADDRESS | VARCHAR| Full address for random person
|AGE | INTEGER | Calculated at time of creation based on Birthdate and current date.
|BIRTH_DATE | VARCHAR | Randomized Date of Birth
|BIRTH_DAY | INTEGER | Numeric day
|BIRTH_MONTH | INTEGER | Numeric month
|BIRTH_YEAR | INTEGER | Numeric year
|BLOOD_TYPE | VARCHAR | Randomized Blood type
|FIRST_NAME | VARCHAR
|GENDER | VARCHAR | Randomized gender
|HOME_STATE | VARCHAR | Two-letter state parsed from Address 
|HOME_ZIP | INTEGER | Numeric Zip based on State
|JOB | VARCHAR | Randomized Profession
|LAST_NAME | VARCHAR 
|MAIL | VARCHAR | Random schema based on Name and random domain.
|NAME | VARCHAR
|POKEMON | INTEGER | Representing number of pokemon
|SSN | VARCHAR | Randomized Social Security Number
|UID | VARCHAR | First letter of the first/last name followed by last 4 numbers of Social: `str(first_name[1] + last_name[1] + self.ssn[-4:]).upper()`
|POKEMON_N_ABILITY_1 | VARCHAR | Name of Ability
|POKEMON_N_ABILITY_2 | VARCHAR | (Optional) Secondary Ability
|POKEMON_N_EVOLUTION_CHAIN_ID | INTEGER | Numeric assignment for Pokemon that evolve to and from.
|POKEMON_N_EVOLVES_FROM_SPECIES_ID | INTEGER
|POKEMON_N_EVOLVES_FROM_SPECIES_NAME | VARCHAR
|POKEMON_N_EVOLVES_TO_SPECIES_ID | INTEGER
|POKEMON_N_EVOLVES_TO_SPECIES_NAME | VARCHAR
|POKEMON_N_GENERATION_ID | INTEGER
|POKEMON_N_HEIGHT | INTEGER
|POKEMON_N_HIDDEN_ABILITY | VARCHAR
|POKEMON_N_ID | INTEGER
|POKEMON_N_LEVEL | INTEGER
|POKEMON_N_MOVE_1 | VARCHAR
|POKEMON_N_MOVE_1_PROSE | VARCHAR
|POKEMON_N_MOVE_2 | VARCHAR
|POKEMON_N_MOVE_2_PROSE | VARCHAR
|POKEMON_N_MOVE_3 | VARCHAR
|POKEMON_N_MOVE_3_PROSE | VARCHAR
|POKEMON_N_MOVE_4 | VARCHAR
|POKEMON_N_MOVE_4_PROSE | VARCHAR
|POKEMON_N_NAME | VARCHAR
|POKEMON_N_NATURE | VARCHAR
|POKEMON_N_SPECIES_ID | INTEGER
|POKEMON_N_SPECIES_NAME | VARCHAR
|POKEMON_N_TYPE_1 | VARCHAR
|POKEMON_N_TYPE_2 | VARCHAR
|POKEMON_N_WEIGHT | INTEGER

## Example Data
Example of data prior to the formatters:
```JSON
{
    "IA3831": {
        "BIO": {
            "ADDRESS": "8994 Hicks Divide Apt. 477, OH 44350",
            "AGE": 37,
            "BIRTH_DATE": "1982-08-03",
            "BIRTH_DAY": 3,
            "BIRTH_MONTH": 8,
            "BIRTH_YEAR": 1982,
            "BLOOD_TYPE": "B+",
            "FIRST_NAME": "Virginia",
            "GENDER": "F",
            "HOME_STATE": "OH",
            "HOME_ZIP": 44350,
            "JOB": "Engineer, petroleum",
            "LAST_NAME": "Carter",
            "MAIL": "v.carter@gmail.com",
            "NAME": "Virginia Carter",
            "POKEMON": 5,
            "SSN": "075-07-3831",
            "UID": "IA3831"
        },
        "POKEMON": {
            "POKEMON_1": {
                "POKEMON_1_ABILITY_1": "flash-fire",
                "POKEMON_1_ABILITY_2": "None",
                "POKEMON_1_EVOLUTION_CHAIN_ID": 15,
                "POKEMON_1_EVOLVES_FROM_SPECIES_ID": 37,
                "POKEMON_1_EVOLVES_FROM_SPECIES_NAME": "vulpix",
                "POKEMON_1_EVOLVES_TO_SPECIES_ID": 0,
                "POKEMON_1_EVOLVES_TO_SPECIES_NAME": "None",
                "POKEMON_1_GENERATION_ID": 1,
                "POKEMON_1_HEIGHT": 11,
                "POKEMON_1_HIDDEN_ABILITY": "drought",
                "POKEMON_1_ID": 38,
                "POKEMON_1_LEVEL": 49,
                "POKEMON_1_MOVE_1": "tail-whip",
                "POKEMON_1_MOVE_1_PROSE": "Lowers the target's Defense by one stage.",
                "POKEMON_1_MOVE_2": "substitute",
                "POKEMON_1_MOVE_2_PROSE": "Transfers 1/4 of the user's max HP into a doll, protecting the user from further damage or status changes until it breaks.",
                "POKEMON_1_MOVE_3": "roar",
                "POKEMON_1_MOVE_3_PROSE": "Immediately ends wild battles.  Forces trainers to switch Pok\u00e9mon.",
                "POKEMON_1_MOVE_4": "bide",
                "POKEMON_1_MOVE_4_PROSE": "User waits for two turns, then hits back for twice the damage it took.",
                "POKEMON_1_NAME": "ninetales",
                "POKEMON_1_NATURE": "lonely",
                "POKEMON_1_SPECIES_ID": 38,
                "POKEMON_1_SPECIES_NAME": "Fox",
                "POKEMON_1_TYPE_1": "fire",
                "POKEMON_1_TYPE_2": "None",
                "POKEMON_1_WEIGHT": 199
            },
            "POKEMON_2": {
                "POKEMON_2_ABILITY_1": "effect-spore",
                "POKEMON_2_ABILITY_2": "None",
                "POKEMON_2_EVOLUTION_CHAIN_ID": 19,
                "POKEMON_2_EVOLVES_FROM_SPECIES_ID": 46,
                "POKEMON_2_EVOLVES_FROM_SPECIES_NAME": "paras",
                "POKEMON_2_EVOLVES_TO_SPECIES_ID": 0,
                "POKEMON_2_EVOLVES_TO_SPECIES_NAME": "None",
                "POKEMON_2_GENERATION_ID": 1,
                "POKEMON_2_HEIGHT": 10,
                "POKEMON_2_HIDDEN_ABILITY": "damp",
                "POKEMON_2_ID": 47,
                "POKEMON_2_LEVEL": 9,
                "POKEMON_2_MOVE_1": "substitute",
                "POKEMON_2_MOVE_1_PROSE": "Transfers 1/4 of the user's max HP into a doll, protecting the user from further damage or status changes until it breaks.",
                "POKEMON_2_MOVE_2": "toxic",
                "POKEMON_2_MOVE_2_PROSE": "Badly poisons the target, inflicting more damage every turn.",
                "POKEMON_2_MOVE_3": "scratch",
                "POKEMON_2_MOVE_3_PROSE": "Inflicts regular damage with no additional effect.",
                "POKEMON_2_MOVE_4": "rest",
                "POKEMON_2_MOVE_4_PROSE": "User sleeps for two turns, completely healing itself.",
                "POKEMON_2_NAME": "parasect",
                "POKEMON_2_NATURE": "mild",
                "POKEMON_2_SPECIES_ID": 47,
                "POKEMON_2_SPECIES_NAME": "Mushroom",
                "POKEMON_2_TYPE_1": "bug",
                "POKEMON_2_TYPE_2": "grass",
                "POKEMON_2_WEIGHT": 295
            },
            "POKEMON_3": {
                "POKEMON_3_ABILITY_1": "flash-fire",
                "POKEMON_3_ABILITY_2": "None",
                "POKEMON_3_EVOLUTION_CHAIN_ID": 15,
                "POKEMON_3_EVOLVES_FROM_SPECIES_ID": 37,
                "POKEMON_3_EVOLVES_FROM_SPECIES_NAME": "vulpix",
                "POKEMON_3_EVOLVES_TO_SPECIES_ID": 0,
                "POKEMON_3_EVOLVES_TO_SPECIES_NAME": "None",
                "POKEMON_3_GENERATION_ID": 1,
                "POKEMON_3_HEIGHT": 11,
                "POKEMON_3_HIDDEN_ABILITY": "drought",
                "POKEMON_3_ID": 38,
                "POKEMON_3_LEVEL": 15,
                "POKEMON_3_MOVE_1": "rage",
                "POKEMON_3_MOVE_1_PROSE": "If the user is hit after using this move, its Attack rises by one stage.",
                "POKEMON_3_MOVE_2": "take-down",
                "POKEMON_3_MOVE_2_PROSE": "User receives 1/4 the damage it inflicts in recoil.",
                "POKEMON_3_MOVE_3": "ember",
                "POKEMON_3_MOVE_3_PROSE": "Has a $effect_chance% chance to [burn]{mechanic:burn} the target.",
                "POKEMON_3_MOVE_4": "swift",
                "POKEMON_3_MOVE_4_PROSE": "Never misses.",
                "POKEMON_3_NAME": "ninetales",
                "POKEMON_3_NATURE": "quiet",
                "POKEMON_3_SPECIES_ID": 38,
                "POKEMON_3_SPECIES_NAME": "Fox",
                "POKEMON_3_TYPE_1": "fire",
                "POKEMON_3_TYPE_2": "None",
                "POKEMON_3_WEIGHT": 199
            },
            "POKEMON_4": {
                "POKEMON_4_ABILITY_1": "clear-body",
                "POKEMON_4_ABILITY_2": "None",
                "POKEMON_4_EVOLUTION_CHAIN_ID": 30,
                "POKEMON_4_EVOLVES_FROM_SPECIES_ID": 0,
                "POKEMON_4_EVOLVES_FROM_SPECIES_NAME": "None",
                "POKEMON_4_EVOLVES_TO_SPECIES_ID": 73,
                "POKEMON_4_EVOLVES_TO_SPECIES_NAME": "tentacruel",
                "POKEMON_4_GENERATION_ID": 1,
                "POKEMON_4_HEIGHT": 9,
                "POKEMON_4_HIDDEN_ABILITY": "rain-dish",
                "POKEMON_4_ID": 72,
                "POKEMON_4_LEVEL": 6,
                "POKEMON_4_MOVE_1": "mega-drain",
                "POKEMON_4_MOVE_1_PROSE": "Drains half the damage inflicted to heal the user.",
                "POKEMON_4_MOVE_2": "acid",
                "POKEMON_4_MOVE_2_PROSE": "Has a $effect_chance% chance to lower the target's Special Defense by one stage.",
                "POKEMON_4_MOVE_3": "bubble-beam",
                "POKEMON_4_MOVE_3_PROSE": "Has a $effect_chance% chance to lower the target's Speed by one stage.",
                "POKEMON_4_MOVE_4": "water-gun",
                "POKEMON_4_MOVE_4_PROSE": "Inflicts regular damage with no additional effect.",
                "POKEMON_4_NAME": "tentacool",
                "POKEMON_4_NATURE": "lonely",
                "POKEMON_4_SPECIES_ID": 72,
                "POKEMON_4_SPECIES_NAME": "Jellyfish",
                "POKEMON_4_TYPE_1": "water",
                "POKEMON_4_TYPE_2": "poison",
                "POKEMON_4_WEIGHT": 455
            },
            "POKEMON_5": {
                "POKEMON_5_ABILITY_1": "run-away",
                "POKEMON_5_ABILITY_2": "None",
                "POKEMON_5_EVOLUTION_CHAIN_ID": 32,
                "POKEMON_5_EVOLVES_FROM_SPECIES_ID": 0,
                "POKEMON_5_EVOLVES_FROM_SPECIES_NAME": "None",
                "POKEMON_5_EVOLVES_TO_SPECIES_ID": 78,
                "POKEMON_5_EVOLVES_TO_SPECIES_NAME": "rapidash",
                "POKEMON_5_GENERATION_ID": 1,
                "POKEMON_5_HEIGHT": 10,
                "POKEMON_5_HIDDEN_ABILITY": "flame-body",
                "POKEMON_5_ID": 77,
                "POKEMON_5_LEVEL": 17,
                "POKEMON_5_MOVE_1": "skull-bash",
                "POKEMON_5_MOVE_1_PROSE": "Raises the user's Defense by one stage.  User charges for one turn before attacking.",
                "POKEMON_5_MOVE_2": "rage",
                "POKEMON_5_MOVE_2_PROSE": "If the user is hit after using this move, its Attack rises by one stage.",
                "POKEMON_5_MOVE_3": "double-edge",
                "POKEMON_5_MOVE_3_PROSE": "User receives 1/3 the damage inflicted in recoil.",
                "POKEMON_5_MOVE_4": "take-down",
                "POKEMON_5_MOVE_4_PROSE": "User receives 1/4 the damage it inflicts in recoil.",
                "POKEMON_5_NAME": "ponyta",
                "POKEMON_5_NATURE": "naughty",
                "POKEMON_5_SPECIES_ID": 77,
                "POKEMON_5_SPECIES_NAME": "Fire Horse",
                "POKEMON_5_TYPE_1": "fire",
                "POKEMON_5_TYPE_2": "None",
                "POKEMON_5_WEIGHT": 300
            }
        }
    }
}
```