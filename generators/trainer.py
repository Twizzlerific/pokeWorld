from faker import *
from datetime import date
import random
import itertools
import pokeDataGenerator
import config

fake = Faker(['en-US', 'en_US'])
# Remove comment to Use same seed (Good for updates):
# Faker.seed(1337)


def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


class Trainer:
    """Create a trainer object with optional arguments for name, age, sex"""

    def return_data(self):
        data = self.data
        return data

    def __init__(self, gender=None, name=None, birth_date=None, address=None, mail=None, job=None, pkm_1=None,
                 pkm_2=None, pkm_3=None, pkm_4=None, pkm_5=None, pkm_6=None):

        self.gender = gender
        self.name = name
        self.birth_date = birth_date
        self.address = address
        self.mail = mail
        self.job = job
        self.pkm_1 = pkm_1
        self.pkm_2 = pkm_2
        self.pkm_3 = pkm_3
        self.pkm_4 = pkm_4
        self.pkm_5 = pkm_5
        self.pkm_6 = pkm_6
        self.data = {}

        """Randomly chooses Gender if not defined"""
        if self.gender is None:
            self.gender = 'M' if random.randint(0, 1) == 0 else 'F'

        """Social Security Number is randomly generated UUID"""
        self.ssn = fake.ssn(taxpayer_identification_number_type='SSN')

        """Based on the gender, we will randomly generate a trainer name if not defined"""
        if self.name is None:
            if self.gender == 'M':
                self.name = fake.first_name_male() + " " + fake.last_name()
            else:
                self.name = fake.first_name_female() + " " + fake.last_name()
        first_name = str(self.name).split(" ")[0]
        last_name = str(self.name).split(" ")[-1]

        """Pick a random date for Birthdate it not defined"""
        if self.birth_date is None:
            try:
                self.birth_date = str(fake.date_of_birth(tzinfo=None, minimum_age=5, maximum_age=100))
            except ValueError:
                # For leap year
                self.birth_date = "1987-09-05"

        """Parse the string of birth_date to create year, month, and day"""
        birth_year = int(self.birth_date.split("-")[0])
        birth_month = int(self.birth_date.split("-")[1])
        birth_day = int(self.birth_date.split("-")[2])
        age = calculate_age(date(birth_year, birth_month, birth_day))

        """Random generate a job if one is not defined"""
        if self.job is None:
            self.job = str(fake.job()).replace('\'', '')

        """Randomly pick a Blood Type"""
        blood_type_letters = ["A", "B", "AB", "O"]
        blood_type_modifies = ["+", "-"]
        blood_type_options = list(itertools.product(blood_type_letters, blood_type_modifies))
        blood_type = "".join(random.choice(blood_type_options))

        """Randomly Generate an address if not defined"""
        if self.address is None:
            home_state = str(fake.state_abbr(include_territories=True))
            home_zip = int(fake.postalcode_in_state(state_abbr=home_state))
            self.address = str(fake.street_address() + ", " + home_state + " " + str(home_zip))

        """Randomly Generates mail"""
        domains = [fake.domain_name(), fake.free_email_domain()]
        domain_options = list(itertools.product(domains))
        domain = "".join(random.choice(domain_options))
        if self.mail is None:
            random_schema = random.randint(0, 2)

            if random_schema == 0:
                self.mail = first_name + "." + last_name + "@" + domain
            if random_schema == 1:
                self.mail = last_name + "." + first_name + "@" + domain
            if random_schema == 2:
                self.mail = first_name[0] + "." + last_name + "@" + domain

        """Creating a unique Identifier"""
        uid = str(first_name[0:2] + last_name[0:2] + self.ssn[-4:]).upper()

        """Random integer to decide number of pokemon"""
        num_of_pkm = random.randint(1, 6)

        """Trainer bio data construction JSON"""
        self.data[uid] = {"BIO": {
            "UID": uid,
            "NAME": self.name,
            "GENDER": self.gender,
            "SSN": str(self.ssn),
            "FIRST_NAME": first_name,
            "LAST_NAME": last_name,
            "BIRTH_DATE": self.birth_date,
            "BIRTH_YEAR": birth_year,
            "BIRTH_MONTH": birth_month,
            "BIRTH_DAY": birth_day,
            "AGE": age,
            "JOB": self.job,
            "BLOOD_TYPE": blood_type,
            "ADDRESS": self.address,
            "HOME_ZIP": home_zip,
            "HOME_STATE": home_state,
            "MAIL": str(self.mail.lower()),
            "POKEMON": num_of_pkm
        },
            "POKEMON": {

            }}

        """Generate and append pokemon Data"""

        trainer_pokemon_data = {}

        for i in range(1, num_of_pkm + 1):
            pkm_data = {}
            output_random_pokemon_data = pokeDataGenerator.random_pokemon()
            pkm_position = 'pokemon_'.upper() + str(i)
            pkm_prefix = pkm_position + '_'.upper()
            pkm_level = random.randint(1, config.MAX_TRAINER_POKEMON_LEVEL)
            pk_bio = output_random_pokemon_data['bio']
            pkm_data[pkm_prefix + 'LEVEL'] = pkm_level

            pkm_random_moves = pokeDataGenerator.get_random_moves(pkm_level, output_random_pokemon_data['moves'])

            for k in pk_bio:
                pkm_data[pkm_prefix + str(k).upper()] = pk_bio[k]

            for pkm_moves in pkm_random_moves:
                pkm_move_key = pkm_prefix + 'MOVE_' + str(pkm_random_moves.index(pkm_moves) + 1)
                pkm_data[pkm_move_key] = pkm_moves

                pkm_move_key_prose = pkm_prefix + 'MOVE_' + str(pkm_random_moves.index(pkm_moves) + 1) + '_PROSE'
                pkm_data[pkm_move_key_prose] = output_random_pokemon_data['moves'][pkm_moves]['move_effect_prose']

            pkm_nature = pokeDataGenerator.get_random_nature()
            pkm_nature_prefix = pkm_prefix + 'NATURE'
            pkm_data[pkm_nature_prefix] = pkm_nature

            trainer_pokemon_data[pkm_position] = pkm_data

        self.data[uid]['POKEMON'] = trainer_pokemon_data
