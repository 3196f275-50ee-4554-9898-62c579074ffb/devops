import requests

def display_metadata(metadata):
    for key, value in metadata.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    response = requests.get('http://127.0.0.1:5000/metadata')
    metadata = response.json()
    display_metadata(metadata)