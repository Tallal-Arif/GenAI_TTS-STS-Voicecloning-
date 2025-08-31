from deepgram import DeepgramClient, PrerecordedOptions
import os
# The API key we created in step 3
DEEPGRAM_API_KEY = '8d41f8e5cd85d49a1132f79b5c511648d518a723'

transcription_folder = "transcriptions"

def main():
    for i in range(10):
        PATH_TO_FILE = f'life_3_0_page_0_{i+1}'
        deepgram = DeepgramClient(DEEPGRAM_API_KEY)

        with open(f'Audio/{PATH_TO_FILE}.wav', 'rb') as buffer_data:
            payload = { 'buffer': buffer_data }

            options = PrerecordedOptions(
                smart_format=True, model="nova-2", language="en-US"
            )

            response = deepgram.listen.prerecorded.v('1').transcribe_file(payload, options)
            print(response.to_json(indent=4))
            full_transcript = response['results']['channels'][0]['alternatives'][0]['transcript']
            
            
            os.makedirs(transcription_folder, exist_ok=True)
            file_path = os.path.join(transcription_folder, f'{PATH_TO_FILE}.txt')
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(full_transcript)
            print(f"Transcript saved to {file_path}")

if __name__ == '__main__':
    main()


