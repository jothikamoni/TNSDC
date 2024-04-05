import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech with additional features
def text_to_speech(text, rate=200, voice_id=None):
    try:
        # Set speech rate
        engine.setProperty('rate', rate)

        # Set voice type if specified
        if voice_id:
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[voice_id].id)

        # Print the text
        print("Text to be converted to speech:")
        print(text)

        # Convert text to speech
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error occurred:", e)

# Taking input text from the user
user_input = input("Enter the text to convert to speech: ")

# Example usage with additional features
text_to_speech(user_input, rate=150, voice_id=1)  # Adjust rate and voice type as needed
