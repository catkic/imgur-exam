from imgurpython import ImgurClient

client_id = '17e6ca4e5c3785d'
client_secret = '0032aba7460da31f80c779f640696cef151d7f8b'

client = ImgurClient(client_id, client_secret)

    # Example request
items = client.gallery()
for item in items:
    print(item.link)
