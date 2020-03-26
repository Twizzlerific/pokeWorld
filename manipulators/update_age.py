import config
import generators.query as query
from generators.trainer import calculate_age
from datetime import date


def birthday_update():
    today = date.today()

    month = str(today.month)
    day = str(today.day)
    birthday_query = 'SELECT UID, AGE FROM ' + config.HBASE_TABLE_NAME + ' WHERE (BIRTH_MONTH=' + month + ' AND BIRTH_DAY=' + day + ')'

    if config.OUTPUT_METHOD == 'PHOENIX':

        if config.OUTPUT_TO_FILE is True:
            pass  # @TODO: Format
        else:
            db = query.connect_to_phoenix()

            with db.cursor() as cursor:
                cursor.execute(birthday_query)

                results = cursor.fetchall()
                for row in results:
                    uid = row[0]
                    current_age = row[1]
                    new_age = int(current_age + 1)
                    age_update_query = 'UPSERT INTO ' + config.HBASE_TABLE_NAME + '(UID, AGE) VALUES (\'' + uid + '\',' + str(new_age) + ')'
                    print age_update_query
                    cursor.execute(age_update_query)



birthday_update()