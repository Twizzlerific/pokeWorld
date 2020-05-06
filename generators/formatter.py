import config
from collections import OrderedDict


def output_hbase_shell(data, uid):
    trainer_input = data[uid]
    trainer_input_bio = trainer_input['BIO']
    trainer_input_pkm = trainer_input['POKEMON']
    num_of_pkm = trainer_input_bio['POKEMON']

    bio_fields = []
    for bio_field in trainer_input['BIO']:
        bio_fields.append(bio_field)

    pkm_fields = []
    for pkm_field in trainer_input_pkm.iterkeys():
        for pkm_n_field in trainer_input_pkm[pkm_field]:
            pkm_fields.append(pkm_n_field)

    prefix = 'put \'' + config.HBASE_TABLE_NAME.upper() + '\', \'' + str(uid) + '\', '

    output = []

    """Create initial row"""
    initial_row = 'put \'' + config.HBASE_TABLE_NAME.upper() + '\', \'' + str(uid) + '\'\n'

    output.append(initial_row)

    for item in bio_fields:
        if isinstance(trainer_input_bio.get(item), int):
            bio_output = prefix + '\'BIO:' + str(item).upper() + '\', ' + str(trainer_input_bio.get(item)) + '\n'
            output.append(bio_output)
        else:
            bio_output = prefix + '\'BIO:' + str(item).upper() + '\', ' + str(
                '\'' + str(trainer_input_bio.get(str(item))).replace('\'', '').replace(', ', ' ') + '\'') + '\n'
            output.append(bio_output)

    for n in range(1, num_of_pkm + 1):
        pkm_dict = trainer_input_pkm['POKEMON_' + str(n)]

        for item in pkm_fields:
            try:
                if isinstance(pkm_dict[item], int):
                    pkm_output = prefix + '\'PKM:' + str(item).upper() + '\', ' + str(pkm_dict[item]) + '\n'
                    output.append(pkm_output)
                else:
                    pkm_output = prefix + '\'PKM:' + str(item).upper() + '\', ' + str(
                        '\'' + str(pkm_dict[item]).replace('\'s', 's').replace(', ', ' ') + '\'\n')
                    output.append(pkm_output)
            except UnicodeError as e:
                pkm_output = prefix + '\'PKM:' + str(item).upper() + '\', ' + str(
                    '\'' + str(pkm_dict[item]).replace('\'s', 's').replace(', ', ' ') + '\'\n')
                output.append(pkm_output)
            except KeyError:
                pass
    return output


def output_happy_base(data, uid):
    # Template:
    # (b'row-key-1', {b'cf:col1': b'value1', b'cf:col2': b'value2'})
    # (b'IA3831', {b'BIO:FIRST_NAME': b'Virginia', b'BIO:LAST_NAME': b'Carter'})

    trainer_input = data[uid]
    trainer_input_bio = trainer_input['BIO']
    trainer_input_pkm = trainer_input['POKEMON']
    num_of_pkm = trainer_input_bio['POKEMON']

    bio_fields = []
    for bio_field in trainer_input_bio:
        bio_fields.append(bio_field)

    pkm_fields = []
    for pkm_field in trainer_input_pkm.iterkeys():
        for pkm_n_field in trainer_input_pkm[pkm_field]:
            pkm_fields.append(pkm_n_field)

    bio_fields.sort()
    pkm_fields.sort()

    all_values = OrderedDict()

    for item in bio_fields:
        if isinstance(trainer_input_bio.get(item), int):
            bio_output = str(trainer_input_bio.get(item))
            all_values["BIO" + ":" + item] = bio_output
        else:
            if item != "UID":
                bio_output = str(trainer_input_bio.get(str(item))).replace('\'', '').replace(', ', ' ')
                all_values["BIO" + ":" + item] = bio_output
            else:
                pass

    for n in range(1, num_of_pkm + 1):
        pkm_dict = trainer_input_pkm['POKEMON_' + str(n)]

        for item in pkm_fields:
            try:
                if isinstance(pkm_dict[item], int):
                    pkm_output = str(pkm_dict[item])
                    all_values["PKM" + ":" + item] = pkm_output
                else:
                    pkm_output = str(pkm_dict[item]).replace('\'s', 's').replace(', ', ' ')
                    all_values["PKM" + ":" + item] = pkm_output
            except UnicodeError as e:
                pkm_output = str(pkm_dict[item]).replace('\'s', 's').replace(', ', ' ')
                all_values["PKM" + ":" + item] = pkm_output
            except KeyError:
                pass

    return all_values


def output_csv(data, uid):
    # Will need to take into account all fields even if there is no information
    trainer_input = data[uid]
    trainer_input_bio = trainer_input['BIO']
    trainer_input_pkm = trainer_input['POKEMON']
    num_of_pkm = trainer_input_bio['POKEMON']

    # @TODO: Create a central REPO for fields to make expansion easier

    csv_fields = ['ADDRESS', 'AGE', 'BIRTH_DATE', 'BIRTH_DAY', 'BIRTH_MONTH', 'BIRTH_YEAR', 'BLOOD_TYPE', 'FIRST_NAME',
                  'GENDER', 'HOME_STATE', 'HOME_ZIP', 'JOB', 'LAST_NAME', 'MAIL', 'NAME', 'POKEMON', 'SSN', 'UID',
                  'POKEMON_1_ABILITY_1', 'POKEMON_1_ABILITY_2', 'POKEMON_1_EVOLUTION_CHAIN_ID',
                  'POKEMON_1_EVOLVES_FROM_SPECIES_ID', 'POKEMON_1_EVOLVES_FROM_SPECIES_NAME',
                  'POKEMON_1_EVOLVES_TO_SPECIES_ID', 'POKEMON_1_EVOLVES_TO_SPECIES_NAME', 'POKEMON_1_GENERATION_ID',
                  'POKEMON_1_HEIGHT', 'POKEMON_1_HIDDEN_ABILITY', 'POKEMON_1_ID', 'POKEMON_1_LEVEL', 'POKEMON_1_MOVE_1',
                  'POKEMON_1_MOVE_1_PROSE', 'POKEMON_1_MOVE_2', 'POKEMON_1_MOVE_2_PROSE', 'POKEMON_1_MOVE_3',
                  'POKEMON_1_MOVE_3_PROSE', 'POKEMON_1_MOVE_4', 'POKEMON_1_MOVE_4_PROSE', 'POKEMON_1_NAME',
                  'POKEMON_1_NATURE', 'POKEMON_1_SPECIES_ID', 'POKEMON_1_SPECIES_NAME', 'POKEMON_1_TYPE_1',
                  'POKEMON_1_TYPE_2', 'POKEMON_1_WEIGHT', 'POKEMON_2_ABILITY_1', 'POKEMON_2_ABILITY_2',
                  'POKEMON_2_EVOLUTION_CHAIN_ID', 'POKEMON_2_EVOLVES_FROM_SPECIES_ID',
                  'POKEMON_2_EVOLVES_FROM_SPECIES_NAME', 'POKEMON_2_EVOLVES_TO_SPECIES_ID',
                  'POKEMON_2_EVOLVES_TO_SPECIES_NAME', 'POKEMON_2_GENERATION_ID', 'POKEMON_2_HEIGHT',
                  'POKEMON_2_HIDDEN_ABILITY', 'POKEMON_2_ID', 'POKEMON_2_LEVEL', 'POKEMON_2_MOVE_1',
                  'POKEMON_2_MOVE_1_PROSE', 'POKEMON_2_MOVE_2', 'POKEMON_2_MOVE_2_PROSE', 'POKEMON_2_MOVE_3',
                  'POKEMON_2_MOVE_3_PROSE', 'POKEMON_2_MOVE_4', 'POKEMON_2_MOVE_4_PROSE', 'POKEMON_2_NAME',
                  'POKEMON_2_NATURE', 'POKEMON_2_SPECIES_ID', 'POKEMON_2_SPECIES_NAME', 'POKEMON_2_TYPE_1',
                  'POKEMON_2_TYPE_2', 'POKEMON_2_WEIGHT', 'POKEMON_3_ABILITY_1', 'POKEMON_3_ABILITY_2',
                  'POKEMON_3_EVOLUTION_CHAIN_ID', 'POKEMON_3_EVOLVES_FROM_SPECIES_ID',
                  'POKEMON_3_EVOLVES_FROM_SPECIES_NAME', 'POKEMON_3_EVOLVES_TO_SPECIES_ID',
                  'POKEMON_3_EVOLVES_TO_SPECIES_NAME', 'POKEMON_3_GENERATION_ID', 'POKEMON_3_HEIGHT',
                  'POKEMON_3_HIDDEN_ABILITY', 'POKEMON_3_ID', 'POKEMON_3_LEVEL', 'POKEMON_3_MOVE_1',
                  'POKEMON_3_MOVE_1_PROSE', 'POKEMON_3_MOVE_2', 'POKEMON_3_MOVE_2_PROSE', 'POKEMON_3_MOVE_3',
                  'POKEMON_3_MOVE_3_PROSE', 'POKEMON_3_MOVE_4', 'POKEMON_3_MOVE_4_PROSE', 'POKEMON_3_NAME',
                  'POKEMON_3_NATURE', 'POKEMON_3_SPECIES_ID', 'POKEMON_3_SPECIES_NAME', 'POKEMON_3_TYPE_1',
                  'POKEMON_3_TYPE_2', 'POKEMON_3_WEIGHT', 'POKEMON_4_ABILITY_1', 'POKEMON_4_ABILITY_2',
                  'POKEMON_4_EVOLUTION_CHAIN_ID', 'POKEMON_4_EVOLVES_FROM_SPECIES_ID',
                  'POKEMON_4_EVOLVES_FROM_SPECIES_NAME', 'POKEMON_4_EVOLVES_TO_SPECIES_ID',
                  'POKEMON_4_EVOLVES_TO_SPECIES_NAME', 'POKEMON_4_GENERATION_ID', 'POKEMON_4_HEIGHT',
                  'POKEMON_4_HIDDEN_ABILITY', 'POKEMON_4_ID', 'POKEMON_4_LEVEL', 'POKEMON_4_MOVE_1',
                  'POKEMON_4_MOVE_1_PROSE', 'POKEMON_4_MOVE_2', 'POKEMON_4_MOVE_2_PROSE', 'POKEMON_4_MOVE_3',
                  'POKEMON_4_MOVE_3_PROSE', 'POKEMON_4_MOVE_4', 'POKEMON_4_MOVE_4_PROSE', 'POKEMON_4_NAME',
                  'POKEMON_4_NATURE', 'POKEMON_4_SPECIES_ID', 'POKEMON_4_SPECIES_NAME', 'POKEMON_4_TYPE_1',
                  'POKEMON_4_TYPE_2', 'POKEMON_4_WEIGHT', 'POKEMON_5_ABILITY_1', 'POKEMON_5_ABILITY_2',
                  'POKEMON_5_EVOLUTION_CHAIN_ID', 'POKEMON_5_EVOLVES_FROM_SPECIES_ID',
                  'POKEMON_5_EVOLVES_FROM_SPECIES_NAME', 'POKEMON_5_EVOLVES_TO_SPECIES_ID',
                  'POKEMON_5_EVOLVES_TO_SPECIES_NAME', 'POKEMON_5_GENERATION_ID', 'POKEMON_5_HEIGHT',
                  'POKEMON_5_HIDDEN_ABILITY', 'POKEMON_5_ID', 'POKEMON_5_LEVEL', 'POKEMON_5_MOVE_1',
                  'POKEMON_5_MOVE_1_PROSE', 'POKEMON_5_MOVE_2', 'POKEMON_5_MOVE_2_PROSE', 'POKEMON_5_MOVE_3',
                  'POKEMON_5_MOVE_3_PROSE', 'POKEMON_5_MOVE_4', 'POKEMON_5_MOVE_4_PROSE', 'POKEMON_5_NAME',
                  'POKEMON_5_NATURE', 'POKEMON_5_SPECIES_ID', 'POKEMON_5_SPECIES_NAME', 'POKEMON_5_TYPE_1',
                  'POKEMON_5_TYPE_2', 'POKEMON_5_WEIGHT', 'POKEMON_6_ABILITY_1', 'POKEMON_6_ABILITY_2',
                  'POKEMON_6_EVOLUTION_CHAIN_ID', 'POKEMON_6_EVOLVES_FROM_SPECIES_ID',
                  'POKEMON_6_EVOLVES_FROM_SPECIES_NAME', 'POKEMON_6_EVOLVES_TO_SPECIES_ID',
                  'POKEMON_6_EVOLVES_TO_SPECIES_NAME', 'POKEMON_6_GENERATION_ID', 'POKEMON_6_HEIGHT',
                  'POKEMON_6_HIDDEN_ABILITY', 'POKEMON_6_ID', 'POKEMON_6_LEVEL', 'POKEMON_6_MOVE_1',
                  'POKEMON_6_MOVE_1_PROSE', 'POKEMON_6_MOVE_2', 'POKEMON_6_MOVE_2_PROSE', 'POKEMON_6_MOVE_3',
                  'POKEMON_6_MOVE_3_PROSE', 'POKEMON_6_MOVE_4', 'POKEMON_6_MOVE_4_PROSE', 'POKEMON_6_NAME',
                  'POKEMON_6_NATURE', 'POKEMON_6_SPECIES_ID', 'POKEMON_6_SPECIES_NAME', 'POKEMON_6_TYPE_1',
                  'POKEMON_6_TYPE_2', 'POKEMON_6_WEIGHT']

    bio_fields = []
    for bio_field in trainer_input['BIO']:
        bio_fields.append(bio_field)

    pkm_fields = []
    for pkm_field in trainer_input['POKEMON'].iterkeys():
        for pkm_n_field in trainer_input['POKEMON'][pkm_field]:
            pkm_fields.append(pkm_n_field)

    bio_fields.sort()
    pkm_fields.sort()

    all_fields = []

    for i in bio_fields:
        all_fields.append(i)

    for i in pkm_fields:
        all_fields.append(i)

    all_values = []
    pkm_dict = {}

    for n in range(1, num_of_pkm + 1):
        for field in trainer_input_pkm['POKEMON_' + str(n)]:
            pkm_dict[field] = (trainer_input_pkm['POKEMON_' + str(n)][field])

    for item in csv_fields:
        index = csv_fields.index(item)

        if item in trainer_input_bio.keys():
            all_values.insert(index, trainer_input_bio[item])

        elif item in pkm_dict:
            all_values.insert(index, pkm_dict[item])
        else:
            all_values.insert(index, '')

    for item in all_values:
        index = all_values.index(item)

        if isinstance(item, int):
            pass
        elif isinstance(item, str) or isinstance(item, unicode):
            base_item = item.replace(',', '').replace('\'s', 's').encode('UTF-8')
            all_values[index] = base_item

    return all_values


def output_phoenix_create(data, uid):
    trainer_input = data[uid]
    trainer_input_bio = trainer_input['BIO']
    trainer_input_pkm = trainer_input['POKEMON']
    num_of_pkm = trainer_input_bio['POKEMON']

    bio_fields = []
    for bio_field in trainer_input['BIO']:
        bio_fields.append(bio_field)

    pkm_fields = []
    for pkm_field in trainer_input['POKEMON'].iterkeys():
        for pkm_n_field in trainer_input['POKEMON'][pkm_field]:
            pkm_fields.append(pkm_n_field)

    bio_fields.sort()
    pkm_fields.sort()

    all_fields = []

    for i in bio_fields:
        if i != "UID":
            all_fields.append("BIO" + '."' + i + '"')
        elif i == "UID":
            all_fields.append(i)

    for i in pkm_fields:
        all_fields.append('"PKM"' + '."' + i + '"')

    final_fields = ', '.join(all_fields)

    prefix = 'UPSERT INTO ' + config.HBASE_TABLE_NAME.upper() + '('
    suffix = ');'

    all_values = []

    for item in bio_fields:
        if isinstance(trainer_input_bio.get(item), int):
            bio_output = str(trainer_input_bio.get(item))
            all_values.append(bio_output)
        else:
            bio_output = str('\'' + str(trainer_input_bio.get(str(item))).replace('\'', '').replace(', ', ' ') + '\'')
            all_values.append(bio_output)

    for n in range(1, num_of_pkm + 1):
        pkm_dict = trainer_input_pkm['POKEMON_' + str(n)]

        for item in pkm_fields:
            try:
                if isinstance(pkm_dict[item], int):
                    pkm_output = str(pkm_dict[item])
                    all_values.append(pkm_output)
                else:
                    pkm_output = str('\'' + str(pkm_dict[item]).replace('\'s', 's').replace(', ', ' ') + '\'')
                    all_values.append(pkm_output)
            except UnicodeError as e:
                pkm_output = str('\'' + str(pkm_dict[item]).replace('\'s', 's').replace(', ', ' ') + '\'')
                all_values.append(pkm_output)
            except KeyError:
                pass
    final_values = ', '.join(all_values)
    output = prefix + final_fields + ') VALUES (' + final_values + suffix
    return output


def output_json(data, uid):
    """Added For future projects (i.e. Flattened JSONs)"""
    pass


test = {
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


# output_phoenix_create(test, "IA3831")
# output_hbase_shell(test, "IA3831")
# output_csv(test, "IA3831")
# output_happy_base(test, "IA3831")
