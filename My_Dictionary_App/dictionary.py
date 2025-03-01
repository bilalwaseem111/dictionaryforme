import requests

def get_word_meaning(word):
    """Fetch up to 4 meanings for the given word from an online dictionary API."""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        meanings = []

        for meaning in data[0].get("meanings", []):  # Use .get() for safer access
            part_of_speech = meaning.get("partOfSpeech", "Unknown")
            definitions = meaning.get("definitions", [])[:4]  # Limit to 4 meanings
            
            for d in definitions:
                definition_text = d.get("definition", "No definition available")
                meanings.append(f"({part_of_speech}) {definition_text}")

            if len(meanings) >= 4:
                break

        return meanings if meanings else ["⚠️ No meanings found."]

    else:
        return ["❌ Word not found. Please check your spelling."]
