import requests

def get_word_meaning(word):
    """Fetch up to 4 meanings for the given word from an online dictionary API."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meanings = []

        for meaning in data[0]["meanings"]:
            part_of_speech = meaning["partOfSpeech"]
            definitions = meaning["definitions"][:4]  # Limit to 4 meanings
            
            for d in definitions:
                meanings.append(f"({part_of_speech}) {d['definition']}")

            if len(meanings) >= 4:
                break

        return meanings[:4]  # Return only 4 meanings

    else:
        return ["❌ Word not found. Please check your spelling."]
