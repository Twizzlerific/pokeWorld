Brief examples of how the data looks once formatted as well as a listing of all of the current fields.

---

<!-- toc -->

- [Examples of Output Data](#Examples-of-Output-Data)
  * [HBase](#HBase)
  * [Phoenix](#Phoenix)
  * [CSV](#CSV)
  * [JSON](#JSON)
- [Fields](#Fields)

<!-- tocstop -->

---

## Examples of Output Data

### HBase

__HBase Shell Files:__
Example of HBase data generated:
```
put 'POKEMON_TRAINERS', 'KECO6035'
put 'POKEMON_TRAINERS', 'KECO6035', 'BIO:FIRST_NAME', 'Kelly'
put 'POKEMON_TRAINERS', 'KECO6035', 'BIO:LAST_NAME', 'Cole'
put 'POKEMON_TRAINERS', 'KECO6035', 'BIO:UID', 'KECO6035'
...
```

__HBase Thrift Data:__
Example of data formatted for HBase Thrift Server
```
('ASWI0950', {'BIO:ADDRESS': '06139 Jones Camp Apt. 730 MO 63422'})
('ASWI0950', {'BIO:AGE': '99'})
('ASWI0950', {'BIO:BIRTH_DATE': '1921-01-11'})
('ASWI0950', {'BIO:BIRTH_DAY': '11'})
('ASWI0950', {'BIO:BIRTH_MONTH': '1'})
```

### Phoenix

__Data sent to Phoenix Query Server:__
Example of Phoenix Data generated before sending to remote

```
UPSERT INTO POKEMON_TRAINERS \
(BIO."ADDRESS", BIO."AGE", BIO."BIRTH_DATE", BIO."BIRTH_DAY", BIO."BIRTH_MONTH", BIO."BIRTH_YEAR", BIO."BLOOD_TYPE", BIO."FIRST_NAME", BIO."GENDER", BIO."HOME_STATE", BIO."HOME_ZIP", BIO."JOB", BIO."LAST_NAME", BIO."MAIL", BIO."NAME", BIO."POKEMON", BIO."SSN", UID, \
"PKM"."POKEMON_1_ABILITY_1", "PKM"."POKEMON_1_ABILITY_2", "PKM"."POKEMON_1_EVOLUTION_CHAIN_ID", "PKM"."POKEMON_1_EVOLVES_FROM_SPECIES_ID", "PKM"."POKEMON_1_EVOLVES_FROM_SPECIES_NAME", "PKM"."POKEMON_1_EVOLVES_TO_SPECIES_ID", "PKM"."POKEMON_1_EVOLVES_TO_SPECIES_NAME", "PKM"."POKEMON_1_GENERATION_ID", "PKM"."POKEMON_1_HEIGHT", "PKM"."POKEMON_1_HIDDEN_ABILITY", "PKM"."POKEMON_1_ID", "PKM"."POKEMON_1_LEVEL", "PKM"."POKEMON_1_MOVE_1", "PKM"."POKEMON_1_MOVE_1_PROSE", "PKM"."POKEMON_1_MOVE_2", "PKM"."POKEMON_1_MOVE_2_PROSE", "PKM"."POKEMON_1_NAME", "PKM"."POKEMON_1_NATURE", "PKM"."POKEMON_1_SPECIES_ID", "PKM"."POKEMON_1_SPECIES_NAME", "PKM"."POKEMON_1_TYPE_1", "PKM"."POKEMON_1_TYPE_2", "PKM"."POKEMON_1_WEIGHT", "PKM"."POKEMON_2_ABILITY_1", \
"PKM"."POKEMON_2_ABILITY_2", "PKM"."POKEMON_2_EVOLUTION_CHAIN_ID", "PKM"."POKEMON_2_EVOLVES_FROM_SPECIES_ID", "PKM"."POKEMON_2_EVOLVES_FROM_SPECIES_NAME", "PKM"."POKEMON_2_EVOLVES_TO_SPECIES_ID", "PKM"."POKEMON_2_EVOLVES_TO_SPECIES_NAME", "PKM"."POKEMON_2_GENERATION_ID", "PKM"."POKEMON_2_HEIGHT", "PKM"."POKEMON_2_HIDDEN_ABILITY", "PKM"."POKEMON_2_ID", "PKM"."POKEMON_2_LEVEL", "PKM"."POKEMON_2_MOVE_1", "PKM"."POKEMON_2_MOVE_1_PROSE", "PKM"."POKEMON_2_MOVE_2", "PKM"."POKEMON_2_MOVE_2_PROSE", "PKM"."POKEMON_2_MOVE_3", "PKM"."POKEMON_2_MOVE_3_PROSE", "PKM"."POKEMON_2_MOVE_4", "PKM"."POKEMON_2_MOVE_4_PROSE", "PKM"."POKEMON_2_NAME", "PKM"."POKEMON_2_NATURE", "PKM"."POKEMON_2_SPECIES_ID", "PKM"."POKEMON_2_SPECIES_NAME", "PKM"."POKEMON_2_TYPE_1", "PKM"."POKEMON_2_TYPE_2", "PKM"."POKEMON_2_WEIGHT") \
VALUES ('1481 Natalie Roads Apt. 322 NJ 7780', 31, '1989-04-16', 16, 4, 1989, 'A+', 'Bryan', 'M', 'NJ', 7780, 'Engineer biomedical', 'Atkins', 'b.atkins@thompson-flynn.info', 'Bryan Atkins', 2, '862-69-4728', 'BRAT4728', 'shield-dust', 'None', 5, 0, 'None', 14, 'kakuna', 1, 3, 'run-away', 13, 15, 'string-shot', 'Lowers the targets Speed by one stage.', 'poison-sting', 'Has a $effect_chance% chance to [poison]{mechanic:poison} the target.', 'weedle', 'serious', 13, 'Hairy Bug', 'bug', 'poison', 32, 'swift-swim', 'None', 70, 140, 'kabuto', 0, 'None', 1, 13, 'weak-armor', 141, 11, 'ice-beam', 'Has a $effect_chance% chance to [freeze]{mechanic:freeze} the target.', 'substitute', 'Transfers 1/4 of the users max HP into a doll protecting the user from further damage or status changes until it breaks.', 'body-slam', 'Has a $effect_chance% chance to [paralyze]{mechanic:paralysis} the target.', 'rest', 'User sleeps for two turns completely healing itself.', 'kabutops', 'jolly', 141, 'Shellfish', 'rock', 'water', 405);
...
```

### CSV
Example of CSV data generated:
```
323 Liu Row Apt. 194 ID 83325,45,1974-08-07,7,8,1974,O+,Darlene,F,ID,83325,Colour technologist,Hansen,d.hansen@yahoo.com,Darlene Hansen,6,769-71-1797,DAHA1797,static,None,60,239,elekid,0,None,1,11,vital-spirit,125,18,mega-punch,Inflicts regular damage with no additional effect.,strength,Inflicts regular damage with no additional effect.,mimic,Copies the targets last used move.,reflect,Reduces damage from physical attacks by half.,electabuzz,serious,125,Electric,electric,None,300,intimidate,None,63,0,None,0,None,1,14,sheer-force,128,40,double-edge,User receives 1/3 the damage inflicted in recoil.,bide,User waits for two turns then hits back for twice the damage it took.,mimic,Copies the targets last used move.,thunderbolt,Has a $effect_chance% chance to [paralyze]{mechanic:paralysis} the target.,tauros,quiet,128,Wild Bull,normal,None,884,pickup,None,22,0,None,53,persian,1,4,unnerve,52,5,thunderbolt,Has a $effect_chance% chance to [paralyze]{mechanic:paralysis} the target.,rage,If the user is hit after using this move its Attack rises by one stage.,bubble-beam,Has a $effect_chance% chance to lower the targets Speed by one stage.,pay-day,Scatters money on the ground worth five times the users level.,meowth,bashful,52,Scratch Cat,normal,None,42,shield-dust,None,4,0,None,11,metapod,1,3,run-away,10,51,string-shot,Lowers the targets Speed by one stage.,tackle,Inflicts regular damage with no additional effect.,,,,,caterpie,lax,10,Worm,bug,None,29,synchronize,None,78,0,None,0,None,1,4,None,151,21,psychic,Has a $effect_chance% chance to lower the targets Special Defense by one stage.,mega-kick,Inflicts regular damage with no additional effect.,substitute,Transfers 1/4 of the users max HP into a doll protecting the user from further damage or status changes until it breaks.,submission,User receives 1/4 the damage it inflicts in recoil.,mew,adamant,151,New Species,psychic,None,40,inner-focus,None,76,148,dragonair,0,None,1,22,multiscale,149,18,water-gun,Inflicts regular damage with no additional effect.,bide,User waits for two turns then hits back for twice the damage it took.,blizzard,Has a $effect_chance% chance to freeze the target.,hyper-beam,User foregoes its next turn to recharge.,dragonite,hasty,149,Dragon,dragon,flying,2100
1475 Cortez Prairie Apt. 184 KY 40650,77,1942-05-04,4,5,1942,B+,Victor,M,KY,40650,Teacher secondary school,King,victor.king@forbes.com,Victor King,3,183-72-5745,VIKI5745,overgrow,None,1,1,bulbasaur,3,venusaur,1,10,chlorophyll,2,59,double-team,Raises the users evasion by one stage.,leech-seed,Seeds the target stealing HP from it every turn.,tackle,Inflicts regular damage with no additional effect.,cut,Inflicts regular damage with no additional effect.,ivysaur,hasty,2,Seed,grass,poison,130,compound-eyes,None,4,11,metapod,0,None,1,11,tinted-lens,12,30,double-team,Raises the users evasion by one stage.,bide,User waits for two turns then hits back for twice the damage it took.,hyper-beam,User foregoes its next turn to recharge.,poison-powder,Poisons the target.,butterfree,relaxed,12,Butterfly,bug,flying,320,flash-fire,None,15,37,vulpix,0,None,1,11,drought,38,58,mimic,Copies the targets last used move.,body-slam,Has a $effect_chance% chance to [paralyze]{mechanic:paralysis} the target.,toxic,Badly poisons the target inflicting more damage every turn.,quick-attack,Inflicts regular damage with no additional effect.,ninetales,naive,38,Fox,fire,None,199,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
```
### JSON
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

## Fields
|Field_Name | Data_Type|Description|
|---|---|---|
|BIO|||
|ADDRESS | VARCHAR| Full address for random person
|AGE | INTEGER | Calculated at time of creation based on Birthdate and current date.|
|BIRTH_DATE | VARCHAR | Randomized Date of Birth|
|BIRTH_DAY | INTEGER | Numeric day|
|BIRTH_MONTH | INTEGER | Numeric month|
|BIRTH_YEAR | INTEGER | Numeric year|
|BLOOD_TYPE | VARCHAR | Randomized Blood type|
|FIRST_NAME | VARCHAR|First portion of NAME|
|GENDER | VARCHAR | Randomized gender
|HOME_STATE | VARCHAR | Two-letter state parsed from Address 
|HOME_ZIP | INTEGER | Numeric Zip based on State
|JOB | VARCHAR | Randomized Profession
|LAST_NAME | VARCHAR |Last portion of NAME|
|MAIL | VARCHAR | Random schema based on Name and random domain.
|NAME | VARCHAR|Full name|
|POKEMON | INTEGER | Representing number of pokemon
|SSN | VARCHAR | Randomized Social Security Number
|UID | VARCHAR | First letter of the first/last name followed by last 4 numbers of Social: `str(first_name[1] + last_name[1] + self.ssn[-4:]).upper()`|
|PKM|||
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
|POKEMON_N_TYPE_1 | VARCHAR|
|POKEMON_N_TYPE_2 | VARCHAR|
|POKEMON_N_WEIGHT | INTEGER|
