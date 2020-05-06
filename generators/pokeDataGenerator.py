import random
import query
import codecs
import sys
import config
import unicodedata

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)
pokedex = {}


def generate_pokemon_data(pkm_id):
    conn = query.connect_to_sqlite()

    query_pokemon = conn.execute('SELECT * FROM POKEMON WHERE ID =' + str(pkm_id) + ';')

    for row in query_pokemon:
        id = row[0]
        name = row[1]
        species_id = row[2]
        height = row[3]
        weight = row[4]

        """Querying for species Name where local_language_id = 9 (english)"""
        query_pokemon_species_names = conn.execute(
            'SELECT * FROM POKEMON_SPECIES_NAMES WHERE POKEMON_SPECIES_ID =' + str(
                species_id) + " AND LOCAL_LANGUAGE_ID = 9;")
        result_query_pokemon_species_names = query_pokemon_species_names.fetchone()
        species_name = result_query_pokemon_species_names[3]

        """Querying for species flavor text where version_id=1 (red/blue) and local_language_id=9"""
        query_pokemon_species_flavor_text = conn.execute(
            'SELECT * FROM POKEMON_SPECIES_FLAVOR_TEXT WHERE SPECIES_ID =' + str(
                species_id) + " AND LANGUAGE_ID = 9 AND VERSION_ID=1;")
        result_query_pokemon_species_flavor_text = query_pokemon_species_flavor_text.fetchone()[3]

        # @TODO: UTF-8 encode flavor_text and add to fields list
        # result_query_pokemon_species_flavor_text_intermediate = query_pokemon_species_flavor_text.fetchone()

        species_flavor = result_query_pokemon_species_flavor_text

        """Querying pokemon_species and evolutions on the ID"""
        query_pokemon_species = conn.execute('SELECT * FROM POKEMON_SPECIES WHERE ID =' + str(id) + ";")
        result_query_pokemon_species = query_pokemon_species.fetchone()
        generation_id = result_query_pokemon_species[2]
        evolves_from_species_id = result_query_pokemon_species[3]
        evolution_chain = result_query_pokemon_species[4]

        if evolves_from_species_id is not None:
            query_evolve_name = conn.execute(
                'SELECT identifier FROM POKEMON WHERE ID =' + str(evolves_from_species_id) + ';')
            evolves_from_species_name = query_evolve_name.fetchone()[0]
        else:
            evolves_from_species_id = 0
            evolves_from_species_name = "None"

        """Querying pokemon for pokemon_evolved_to based on ID and evolved_species_ID"""
        query_pokemon_evolve_to = conn.execute(
            'SELECT id FROM POKEMON_SPECIES WHERE evolution_chain_id =' + str(evolution_chain) + ";")
        result_query_pokemon_evolve_to = query_pokemon_evolve_to.fetchall()
        evolution_chain_members = []
        for y in result_query_pokemon_evolve_to:
            evolution_chain_members.append(y[0])

        if id + 1 in evolution_chain_members:
            evolves_to_species_id = id + 1
            query_pokemon_evolution_species = conn.execute(
                'SELECT identifier FROM POKEMON_SPECIES WHERE ID =' + str(evolves_to_species_id) + ';')
            results_query_pokemon_evolution_species = query_pokemon_evolution_species.fetchone()[0]
            evolves_to_species_name = results_query_pokemon_evolution_species
        else:
            evolves_to_species_id = 0
            evolves_to_species_name = "None"

        """Querying for Stats"""
        for stat in conn.execute('SELECT * FROM POKEMON_STATS WHERE POKEMON_ID = ' + str(id) + ';'):
            if stat[1] == 1:
                health = stat[2]
            elif stat[1] == 2:
                attack = stat[2]
            elif stat[1] == 3:
                defense = stat[2]
            elif stat[1] == 4:
                sp_attack = stat[2]
            elif stat[1] == 5:
                sp_defense = stat[2]
            elif stat[1] == 6:
                speed = stat[2]

        """Querying for pokemon_types based on id to get type_id and slot number for types"""
        query_pk_type = conn.execute('SELECT * FROM POKEMON_TYPES WHERE POKEMON_ID = ' + str(id) + ';')
        result_query_pk_type = query_pk_type.fetchall()

        for pk_type in result_query_pk_type:
            if pk_type[2] == 1:
                type_id_slot_1 = pk_type[1]
                query_type_slot_1_name = conn.execute(
                    'SELECT IDENTIFIER FROM TYPES WHERE ID = ' + str(type_id_slot_1) + ';')
                type_slot_1 = query_type_slot_1_name.fetchone()[0]
            if pk_type[2] == 2:
                type_id_slot_2 = pk_type[1]
                query_type_slot_2_name = conn.execute(
                    'SELECT IDENTIFIER FROM TYPES WHERE ID = ' + str(type_id_slot_2) + ';')
                type_slot_2 = query_type_slot_2_name.fetchone()[0]
            else:
                type_slot_2 = "None"

        """Queries for Abilities: ability 1(not null), ability 2(optional), ability 3(hidden)"""
        query_pk_abilities = conn.execute(
            'SELECT pa.*, ab.identifier FROM pokemon_abilities pa JOIN abilities ab ON pa.ability_id = ab.id '
            'WHERE pa.POKEMON_ID =' + str(id) + ';')
        results_query_pk_abilities = query_pk_abilities.fetchall()

        for pk_abilities in results_query_pk_abilities:
            if pk_abilities[3] == 1:
                pk_ability_1 = pk_abilities[4]
            if pk_abilities[3] == 2:
                pk_ability_2 = pk_abilities[4]
            else:
                pk_ability_2 = "None"
            if pk_abilities[3] == 3:
                pk_hidden_ability_name = pk_abilities[4]
            else:
                pk_hidden_ability_name = "None"

        """Queries for Pokemon Moves based on ID"""

        query_pk_moves = conn.execute(
            'SELECT PKM.MOVE_ID, PKM.LEVEL, MV.IDENTIFIER, MV.TYPE_ID, T.IDENTIFIER, '
            'MV.POWER, MV.PP, MV.EFFECT_ID, E.SHORT_EFFECT FROM POKEMON_MOVES PKM '
            'JOIN MOVES MV ON PKM.MOVE_ID = MV.ID JOIN TYPES T ON MV.TYPE_ID = T.ID '
            'JOIN MOVE_EFFECT_PROSE E ON MV.EFFECT_ID = E.MOVE_EFFECT_ID '
            'WHERE PKM.VERSION_GROUP_ID =' + str(config.VERSION_GROUP_ID) + ' AND E.LOCAL_LANGUAGE_ID =' + str(config.LOCAL_LANGUAGE_ID) + ' AND PKM.POKEMON_ID=' + str(id) + ';')
        results_query_pk_moves = query_pk_moves.fetchall()
        pk_moves = {}

        for pk_move in results_query_pk_moves:
            move_name = pk_move[2]
            move_prose = unicodedata.normalize('NFKD', unicode(pk_move[8])).encode('ascii', 'replace')

            pk_moves[move_name] = {
                'move_id': pk_move[0],
                'move_level': pk_move[1],
                'move_name': pk_move[2],
                'move_type_id': pk_move[3],
                'move_type_name': pk_move[4],
                'mv_power': pk_move[5],
                'mv_pp': pk_move[6],
                'move_effect_id': pk_move[7],
                'move_effect_prose': move_prose,
            }

        # JSON building
        pokedex['bio'] = {
            'id': id,
            "name": name,
            'height': height,
            'weight': weight,
            'generation_id': generation_id,
            'species_id': species_id,
            'species_name': species_name,
            # 'species_flavor': species_flavor,
            'evolution_chain_id': evolution_chain,
            'evolves_from_species_id': evolves_from_species_id,
            'evolves_from_species_name': evolves_from_species_name,
            'evolves_to_species_id': evolves_to_species_id,
            'evolves_to_species_name': evolves_to_species_name,
            'type_1': type_slot_1,
            'type_2': type_slot_2,
            'ability_1': pk_ability_1,
            'ability_2': pk_ability_2,
            'hidden_ability': pk_hidden_ability_name

        }
        pokedex['stats'] = {
            'health': health,
            'attack': attack,
            'defense': defense,
            'sp_attack': sp_attack,
            'sp_defense': sp_defense,
            'speed': speed

        }
        pokedex['moves'] = pk_moves

    return pokedex


def random_pokemon():
    random_id = random.randint(1, config.MAX_POKEMON_ID)
    pokemon_data = generate_pokemon_data(random_id)
    return pokemon_data


def get_random_moves(lvl, moves):
    pkm_level = lvl
    all_moves = dict(moves)
    possible_moves = []
    chosen_moves = []

    for p_moves in all_moves.iterkeys():
        if int(all_moves[p_moves]['move_level']) > pkm_level:
            pass
        else:
            possible_moves.append(all_moves[p_moves]['move_name'])

    for i in range(4):
        if i > len(possible_moves):
            break
        else:
            selected_move = random.choice(possible_moves)
            selected_move_index = possible_moves.index(selected_move)
            chosen_moves.append(selected_move)
            possible_moves.pop(selected_move_index)
    return chosen_moves


def get_random_nature():
    random_nature = random.randint(1, 25)
    pkm_natures = {
        1: 'hardy',
        2: 'bold',
        3: 'modest',
        4: 'calm',
        5: 'timid',
        6: 'lonely',
        7: 'docile',
        8: 'mild',
        9: 'gentle',
        10: 'hasty',
        11: 'adamant',
        12: 'impish',
        13: 'bashful',
        14: 'careful',
        15: 'rash',
        16: 'jolly',
        17: 'naughty',
        18: 'lax',
        19: 'quirky',
        20: 'naive',
        21: 'brave',
        22: 'relaxed',
        23: 'quiet',
        24: 'sassy',
        25: 'serious'
    }
    return pkm_natures[random_nature]

