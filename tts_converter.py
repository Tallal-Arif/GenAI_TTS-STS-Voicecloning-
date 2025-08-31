import os
import requests
import time

text_file_directory = 'Text'
file_name = 'life_3_0'
page = '_page_'
ext = '.txt'
files = {}
text = []
speech_file_directory = 'Audio'

for filename in sorted(os.listdir(text_file_directory)):
    file_path = os.path.join(text_file_directory, filename)
    num = int(filename.split("_")[-1].split(".")[0])
    files[num-1] = filename

    
for key in sorted(files.keys()):
    file_path = os.path.join(text_file_directory, file_name + page + str(key) + '.txt')
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
            text.append(content.replace('\t', ' ').replace('\n', ' '))





API_KEY = 'a5cd0e4f-71ec-4cb6-a0a3-991508671c6a'


tts_text = text[0].split('.')

for i in range(10):
    tts_payload = {
        "text": f'{tts_text[i]}',
        "voice_id": 20305,
        "language": 1,
    }

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://client.camb.ai/apis/tts",
        json=tts_payload,
        headers=headers
    )
    response.raise_for_status()
    task_data = response.json()
    task_id = task_data["task_id"]
    print(f"Speech task created! Task ID: {task_id}")


    while True:
        status_response = requests.get(
            f"https://client.camb.ai/apis/tts/{task_id}",
            headers=headers
        )
        status_data = status_response.json()
        status = status_data["status"]
        print(f"Status: {status}")

        if status == "SUCCESS":
            run_id = status_data["run_id"]
            break
        elif status == "FAILED":
            print("Task failed!")
            break

        time.sleep(15)

    if status == "SUCCESS":
        print(f"Speech ready! Run ID: {run_id}")
        audio_response = requests.get(
            f"https://client.camb.ai/apis/tts-result/{run_id}",
            headers=headers,
            stream=True
        )
        file_path = os.path.join(speech_file_directory, file_name + page + '0_' + str(i + 1) + '.wav')
        with open(file_path, "wb") as audio_file:
            for chunk in audio_response.iter_content(chunk_size=1024):
                if chunk:
                    audio_file.write(chunk)
            print('File saved successfully')

        print(f"✨ Generated speech was saved as ${file_name + page + '0_' + str(i + 1) + '.wav'}")
