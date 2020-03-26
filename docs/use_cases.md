


## Stress testing Splits/Compaction
While adding a large amount of rows:

- Use the HBase Master UI to split regions 
- Initiate compaction
- Kill and then restart RegionServers
- Set up Replication and then kill Destination RS (Check Znodes)
- Lower the `hbase.hregion.max.filesize` to create a large number of regions
