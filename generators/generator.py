import datetime
import config
import trainer
import formatter
import query
import csv
import happybase


for requests in range(0, config.TRAINER_COUNT):
    new_trainer = trainer.Trainer()
    new_trainer_data = new_trainer.return_data()
    uid = new_trainer_data.keys()[0]

    if config.OUTPUT_METHOD == 'PHOENIX':
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
                if config.OUTPUT_FILE_NAME == '':
                    output_file = 'hbase_shell_' + str(datetime.datetime) + '.txt'
                    with open(output_file) as output:
                        output.write(item)
                else:
                    with open(config.OUTPUT_FILE_NAME) as output:
                        output.write(item)

        else:
            """We will make a direct connection to HBase thrift server"""
            output = formatter.output_happy_base(new_trainer_data, uid)
            connection = query.connect_to_hbase()
            table = connection.table(config.HBASE_TABLE_NAME)

            for command in output:
                table.put(uid, output)

    if config.OUTPUT_METHOD == 'CSV':
        if config.OUTPUT_TO_FILE is True:
            """OUTPUTTING CSV TO FILE"""
            output = formatter.output_csv(new_trainer_data, uid)

            if config.OUTPUT_FILE_NAME == '':
                output_file = 'pokeWorld_Output_' + str(datetime.datetime) + '.csv'
                csv_file = open(output_file, 'a')
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(output)

            else:
                output_file = config.OUTPUT_FILE_NAME + '.csv'
                csv_file = open(output_file, 'a')
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(output)

        else:
            """We will output csv to shell (NOT RECOMMENDED)"""
            output = formatter.output_csv(new_trainer_data, uid)
            print output






