import trainer
import formatter
import query
import csv
import json
import configs.configuration as config


def generator(count=1):
    import time
    suffix = "_" + str(time.time()).replace(".", "")

    if config.OUTPUT_FILE_NAME == '':
        output_file_uri = config.OUTPUT_FILE_DIR + 'pokeWorld_Output_' + suffix
    else:
        output_file_uri = config.OUTPUT_FILE_DIR + config.OUTPUT_FILE_NAME + suffix

    for requests in range(0, count):
        new_trainer = trainer.Trainer()
        new_trainer_data = new_trainer.return_data()
        uid = new_trainer_data.keys()[0]

        if config.OUTPUT_METHOD == 'PHOENIX':
            if config.OUTPUT_TO_FILE is True:
                """Since we are putting to file, we will output csv"""
                output = formatter.output_csv(new_trainer_data, uid)

                output_file = output_file_uri + '.csv'
                csv_file = open(output_file, 'a')
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(output)

            else:
                """We Will make a connection to Phoenix Query Server"""
                output = formatter.output_phoenix_create(new_trainer_data, uid)
                db = query.connect_to_phoenix()

                with db.cursor() as cursor:
                    cursor.execute(output.replace(';', ''))
                db.close()

        if config.OUTPUT_METHOD == 'HBASE':
            if config.OUTPUT_TO_FILE is True:
                """HBase is selected but we want to put the 'put' commands to a file for hbase shell"""
                output = formatter.output_hbase_shell(new_trainer_data, uid)

                for item in output:

                    output_file = output_file_uri + '.txt'
                    with open(output_file, 'a') as output:
                        output.write(item.encode('UTF-8'))

            else:
                """We will make a direct connection to HBase thrift server"""
                output = formatter.output_happy_base(new_trainer_data, uid)
                connection = query.connect_to_hbase()
                table = connection.table(config.HBASE_TABLE_NAME)

                with table.batch() as b:
                    for key in output:
                        b.put(uid, {key.encode('utf-8'): output[key]})

        if config.OUTPUT_METHOD == 'CSV':
            if config.OUTPUT_TO_FILE is True:
                """OUTPUTTING CSV TO FILE"""
                output = formatter.output_csv(new_trainer_data, uid)

                output_file = output_file_uri + '.csv'
                csv_file = open(output_file, 'a')
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(output)

            else:
                """We will output csv to shell (NOT RECOMMENDED)"""
                output = formatter.output_csv(new_trainer_data, uid)
                print output

        if config.OUTPUT_METHOD == "JSON":
            jsonData = json.dumps(new_trainer_data, indent=4)

            if config.OUTPUT_TO_FILE is True:
                output_file = output_file_uri + '.json'
                with open(output_file, 'a') as output:
                    output.write(jsonData)
            else:
                print(jsonData)






