VOICE_ALONE_API_KEY = 'sk_8b624361fe722395798ef3b51986b4d016a68f744d010d27f5bdd29c018d14cc'



import requests
def main():
    url = "https://api.async.ai/voices/clone"

    payload={
        "name": "My VOice",
        "language": "en",
        "description": "Cloned from sample_voice.wav"
    }
    files=[
    ('audio',('audio', open('sample_audio.wav','rb'),'audio/wav'))
    ]
    headers = {
    'x-api-key': VOICE_ALONE_API_KEY,
    'version': 'v1'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


if __name__ == '__main__':
    main()




#c62645cc-5747-4e75-8165-71bac3d8d42c