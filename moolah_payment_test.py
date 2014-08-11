from moolah_io import moolah
import json
m = moolah()
apiKey = 'YOUR-API-KEY'
sale = m.create(
    apiKey,
    'bitcoin',
    'GBP',
    '10',
    'test',
	)

# decode json to python
decodedProduct = json.loads(sale)
print decodedProduct

# get transaction guid
guid = decodedProduct['guid']
print guid

# check payment status
saleStatus = m.status(guid, apiKey)
print saleStatus
