import urllib


class moolah:

    def create(self, apiKey, coin, currency, amount, product, apiSecret=None, ipn=None, ipn_extra=None):
        params = urllib.urlencode({
                                  'apiKey': apiKey,
                                  'coin':coin,
                                  'currency': currency,
                                  'amount': amount,
                                  'product': product,
                                  'apiSecret': apiSecret,
                                  'ipn:': ipn,
                                  'ipn_extra':ipn_extra
                                  })

        f = urllib.urlopen("https://api.moolah.io/v2/private/merchant/create",  params)
        data = f.read()
        return data

    def status(self, guid, apiKey):
        params = urllib.urlencode({
                                  'apiKey': apiKey,
                                  'guid': guid
                                  })
        f = urllib.urlopen("https://api.moolah.io/v2/private/merchant/status", params)

        data = f.read()
        return data

    def ipn(transactionata, responseData):
        #still needs generic code for handling ipn response
    	return True



