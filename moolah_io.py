import urllib


class moolah_payment:

    def gen_address(self, guid, currency, amount, product, returnUrl, ipn):
        params = urllib.urlencode({
                                  'guid': guid,
                                  'currency': currency,
                                  'amount': amount,
                                  'product': product,
                                  'return': returnUrl,
                                  'ipn:': ipn
                                  })

        f = urllib.urlopen("https://moolah.io/api/pay?%s" % params)
        data = f.read()
        return data

    def check_staus(self, tx_id):
        f = urllib.urlopen("https://moolah.io/api/pay/check/" + tx_id)
        data = f.read()
        return data


class moolah_send:

    def __init__(self, api_key):
        self.api_key = api_key

    def send_funds(self, guid, payload):
        params = urllib.urlencode({
                                  'guid': guid,
                                  'api_ley': self.api_key,
                                  'payload:': payload
                                  })

        f = urllib.urlopen("https://moolah.ch/api/merchant/send/", params)
        data = f.read()
        return data
