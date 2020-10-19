While this project started as a way of generating meaningful data for HBase, I realized it uses could extend to other components. To extend the dataset for additional components, I created the formatters as a way of editing the same data for different outputs. 

---

- [HBase](#HBase)
    + [HBase Shell](#HBase-Shell)
    + [HBase Thrift](#HBase-Thrift)
- [Phoenix](#Phoenix)
- [CSVs](#CSVs)
- [JSONs](#JSONS)

---

## HBase
When it comes to HBase, there are several methods for ingesting from this script. The two main methods are the use of the HBase shell or the HBase Thirft server.  


#### HBase Shell
[HBase shell](https://hbase.apache.org/book.html#shell) is a (J)Ruby based 'Interactive Ruby' (IRB) prompt with administrative as well as data creation/manulation commands built in. For our purposes, it is also a method of scripting data ingestion into HBase. 

This output if achieved by setting the `OUTPUT_METHOD` to `HBASE` and the `OUTPUT_TO_FILE` to `True`. The output will be a file that can be pushed through the HBase shell using a command such as: 

```bash
./hbase shell pokeWorldOutput
```

This method has the benefit of being faster (usually) and requiring only that the file be moved onto an client machine.

The output will be a file crafted by the HBase Formatter which takes the randomized data and constructs a series of statements such as : 

`"put 'POKEMON_TRAINERS', 'IA3831', 'PKM:POKEMON_5_GENERATION_ID', 1`

These are collected into an array and then iterated into the file. 

#### HBase Thrift

The HBase is built on top of the [Thrift](http://thrift.apache.org/) framework and interacts with the backend Java client. For this project, I used the [HappyBase](https://happybase.readthedocs.io/en/latest/) python library which interacts with the HBase thrift server. This allows direct connection to the HBase interface from the launch of the script when dumping the dummy data. 

Use of this requires a Thrift server which can be started on Hortonworks HDP Platform by following the documentation:

[Starting the HBase ThriftServer](https://docs.cloudera.com/HDPDocuments/HDP2/HDP-2.6.5/bk_command-line-installation/content/ref-2a6efe32-d0e1-4e84-9068-4361b8c36dc8.1.html)

Once started, we create a connection via the `query.py`: 
```python
def connect_to_hbase():
    connection = happybase.Connection(host=config.HBASE_SERVER, port=int(config.HBASE_SERVER_PORT), autoconnect=False, transport='buffered')
    connection.open()
    return connection
```

The `generator.py` passes the trainer data to the formatter which sets up the data as an OrderedDictionary before passing back for an iteration through the HappyBase batch api:

```python
with table.batch() as b:
    for key in output:
        b.put(uid, {key.encode('utf-8'): output[key]})
```

## Phoenix

[Phoenix](https://phoenix.apache.org/index.html) is the SQL layer on top of the HBase NoSQL infrastructure. To connect to Phoenix from the generator, I used the [phoenixdb](https://python-phoenixdb.readthedocs.io/en/latest/) python library and then formatted the data to include each row in a single `UPSERT` command. 

I parsed out the specific for creating the connection into the `query.py` file 

``` python
def connect_to_phoenix():
    db = phoenixdb.connect(config.PHOENIX_QUERY_SERVER, max_retries=2, autocommit=True)
    return db

```

The returned connection is then used by the `generator.py` to pass along the data built by the Phoenix output formatter: 

```python
db = query.connect_to_phoenix()
with db.cursor() as cursor:
    cursor.execute(output.replace(';', ''))
```

The formatter crafts statements in the syntax of:

```
UPSERT INTO POKEWORLD_TABLE(<PARSED_FIELDS>) VALUES (<GENERATED VALUES>)
```

As some fields may not exist (such as a trainer only have 4 Pokemon instead of 6) the formatter will only insert data for the columns where data is present or required. If `OUTPUT_TO_FILE` is set to `True`, this will generate a file which can be used when passed to `psql.py`.

## CSVs
Ideal output for use cases such as importing into the Hive Data warehouse but can also be used to perform bulk uploads into HBase. 

___Phoenix Bulk Upload using PSQL:___
```bash
/usr/hdp/current/phoenix-client/bin/psql.py -t POKEMON_TRAINERS ZK_QUORUM:2181/hbase-unsecure pokeWorldOutput.csv
```
> For more information see [Phoenix Documentation Here](https://phoenix.apache.org/bulk_dataload.html)

___Example Output:___
```csv
323 Liu Row Apt. 194 ID 83325,45,1974-08-07,7,8,1974,O+,Darlene,F,ID,83325,Colour technologist,Hansen,d.hansen@yahoo.com,Darlene Hansen,6,769-71-1797,DAHA1797,static,None,60,239,elekid,0,None,1,11,vital-spirit,125,18,mega-punch,Inflicts regular damage with no additional effect.,strength,Inflicts regular damage with no additional effect.,mimic,Copies the targets last used move.,reflect,Reduces damage from physical attacks by half.,electabuzz,serious,125,Electric,electric,None,300,intimidate,None,63,0,None,0,None,1,14,sheer-force,128,40,double-edge,User receives 1/3 the damage inflicted in recoil.,bide,User waits for two turns then hits back for twice the damage it took.,mimic,Copies the targets last used move.,thunderbolt,Has a $effect_chance% chance to [paralyze]{mechanic:paralysis} the target.,tauros,quiet,128,Wild Bull,normal,None,884,pickup,None,22,0,None,53,persian,1,4,unnerve,52,5,thunderbolt,Has a $effect_chance% chance to [paralyze]{mechanic:paralysis} the target.,rage,If the user is hit after using this move its Attack rises by one stage.,bubble-beam,Has a $effect_chance% chance to lower the targets Speed by one stage.,pay-day,Scatters money on the ground worth five times the users level.,meowth,bashful,52,Scratch Cat,normal,None,42,shield-dust,None,4,0,None,11,metapod,1,3,run-away,10,51,string-shot,Lowers the targets Speed by one stage.,tackle,Inflicts regular damage with no additional effect.,,,,,caterpie,lax,10,Worm,bug,None,29,synchronize,None,78,0,None,0,None,1,4,None,151,21,psychic,Has a $effect_chance% chance to lower the targets Special Defense by one stage.,mega-kick,Inflicts regular damage with no additional effect.,substitute,Transfers 1/4 of the users max HP into a doll protecting the user from further damage or status changes until it breaks.,submission,User receives 1/4 the damage it inflicts in recoil.,mew,adamant,151,New Species,psychic,None,40,inner-focus,None,76,148,dragonair,0,None,1,22,multiscale,149,18,water-gun,Inflicts regular damage with no additional effect.,bide,User waits for two turns then hits back for twice the damage it took.,blizzard,Has a $effect_chance% chance to freeze the target.,hyper-beam,User foregoes its next turn to recharge.,dragonite,hasty,149,Dragon,dragon,flying,2100
1475 Cortez Prairie Apt. 184 KY 40650,77,1942-05-04,4,5,1942,B+,Victor,M,KY,40650,Teacher secondary school,King,victor.king@forbes.com,Victor King,3,183-72-5745,VIKI5745,overgrow,None,1,1,bulbasaur,3,venusaur,1,10,chlorophyll,2,59,double-team,Raises the users evasion by one stage.,leech-seed,Seeds the target stealing HP from it every turn.,tackle,Inflicts regular damage with no additional effect.,cut,Inflicts regular damage with no additional effect.,ivysaur,hasty,2,Seed,grass,poison,130,compound-eyes,None,4,11,metapod,0,None,1,11,tinted-lens,12,30,double-team,Raises the users evasion by one stage.,bide,User waits for two turns then hits back for twice the damage it took.,hyper-beam,User foregoes its next turn to recharge.,poison-powder,Poisons the target.,butterfree,relaxed,12,Butterfly,bug,flying,320,flash-fire,None,15,37,vulpix,0,None,1,11,drought,38,58,mimic,Copies the targets last used move.,body-slam,Has a $effect_chance% chance to [paralyze]{mechanic:paralysis} the target.,toxic,Badly poisons the target inflicting more damage every turn.,quick-attack,Inflicts regular damage with no additional effect.,ninetales,naive,38,Fox,fire,None,199,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
```

## JSONS
JSON output dumps the raw data that goes into formatters. You can see an example in the [Fields](fields.md) guide.

