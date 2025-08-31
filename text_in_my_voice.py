import requests
import json
import os

ASYNC_API = 'sk_8b624361fe722395798ef3b51986b4d016a68f744d010d27f5bdd29c018d14cc'
url = "https://api.async.ai/text_to_speech"


output_folder = "My_Voice"
os.makedirs(output_folder, exist_ok=True)

input_folder = "transcriptions"

for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            transcript_text = f.read().strip()

        payload = json.dumps({
            "model_id": "asyncflow_v2.0",
            "transcript": transcript_text,
            "voice": {
                "mode": "id",
                "id": "c62645cc-5747-4e75-8165-71bac3d8d42c"
            },
            "output_format": {
            "container": "mp3",
            "sample_rate": 44100,
            "bit_rate": 192000
            }

        })

        headers = {
            'x-api-key': ASYNC_API,
            'version': 'v1',
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)

        if response.status_code == 200:
            base_name = os.path.splitext(filename)[0] + ".mp3"
            output_path = os.path.join(output_folder, base_name)

            with open(output_path, "wb") as out_f:
                out_f.write(response.content)

            print(f"✅ Saved: {output_path}")
        else:
            print(f"❌ Failed for {filename}: {response.status_code}, {response.text}")
