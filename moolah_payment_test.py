from moolah_io import moolah_payment
import json

# Example use of moolah_payment class to generate a payment address using
# moolah_payment.gen_address() and check the transaction status using
# moolah_payment.check_status()

guid = "guid_as_found_on_moolah_dashboard"

# Generate payment address
p = moolah_payment()
product1 = p.gen_address(guid, 'GBP', '10',
                         'product1', 'http://example.com',
                         'http://example.com/ipn')

# show payment address
print product1

# decode json to python
decodedProduct = json.loads(product1)
print decodedProduct

# get transaction id
tx = decodedProduct['tx']
print tx

# check payment status
productStatus = p.check_status(tx)
print productStatus
