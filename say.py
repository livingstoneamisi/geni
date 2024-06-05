from flask import Flask, request, Response
import xml.etree.ElementTree as ET

app = Flask(__name__)

# Replace this dictionary with an actual database table if necessary
balance_dict = {
    '1234': 100,
    '1235': 150,
    '1236': 190,
}

@app.route('/queryBalance', methods=['POST'])
def query_balance():
    # Get the POST variables
    session_id = request.form.get('sessionId')
    is_active = request.form.get('isActive')

    if is_active == '1':
        # This is the first request; prompt for the account number
        response = ET.Element('Response')
        get_digits = ET.SubElement(response, 'GetDigits', finishOnKey='#', callbackUrl=" https://e544-197-136-96-242.ngrok-free.app/getBalance")
        say = ET.SubElement(get_digits, 'Say')
        say.text = "Please enter your pin to complete the transaction"
        response_xml = ET.tostring(response, encoding='utf-8', method='xml').decode()

        return Response(response_xml, content_type='text/plain')

    return '', 204

@app.route('/getBalance', methods=['POST'])
def get_balance():
    # Read the DTMF digits
    account_number = request.form.get('dtmfDigits')

    # Check if the account number is in the dictionary
    # if account_number in balance_dict:
    #     balance = balance_dict[account_number]
    #     text = f"Your balance is {balance} shillings. Good bye."
    # else:
    text = "transaction completed success"
        

    # Create the XML response
    response = ET.Element('Response')
    say = ET.SubElement(response, 'Say')
    say.text = text
    response_xml = ET.tostring(response, encoding='utf-8', method='xml').decode()

    return Response(response_xml, content_type='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
