**Yandex Geocoder**

**`geocoder.py`** uses 
Yandex Geocoding API (https://tech.yandex.com/maps/doc/geocoder/desc/concepts/About-docpage/) to retrieve geocoordinates on individual address level.


In the `fetchCoordinates` function at the end of the script you need to specify three parameters:

**`source_file`** - path to TSV-file with the unprocessed list of addresses stored (encoded in UTF-8)

**`fields`** - array of fieldnames which should contain `individual_address`, `street_address`, `settlement_address`

**`output_file`** - name of the output file that will be created in the `/output` folder