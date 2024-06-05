# works with both python 2 and 3
from __future__ import print_function

import africastalking

class VOICE:
    def __init__(self):
		# Set your app credentials
        self.username = "edaktari"
        self.api_key = "2ac340bb0eee0916e8dee724caa5739381e8c17c20cf7f3e50accb0c2bf48ebd "
		# Initialize the SDK
        africastalking.initialize(self.username, self.api_key)
		# Get the voice service
        self.voice = africastalking.Voice

    def call(self):
        # Set your Africa's Talking phone number in international format
        callFrom = "+254730731029"
        # Set the numbers you want to call to in a comma-separated list
        callTo   = ["+254790020935"]
        try:
			# Make the call
            result = self.voice.call(callFrom, callTo)
            print (result)
        except Exception as e:
            print ("Encountered an error while making the call:%s" %str(e))

if __name__ == '__main__':
    VOICE().call()