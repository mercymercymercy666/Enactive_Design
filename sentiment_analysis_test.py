import speech_recognition as sr
from textblob import TextBlob

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to categorize emotions based on sentiment scores
def categorize_emotion(sentiment):
    if sentiment < -0.5:
        return "Bad"
    elif sentiment < -0.25:
        return "Sad"
    elif sentiment < 0:
        return "Disgusted"
    elif sentiment == 0:
        return "Surprised"
    elif sentiment < 0.25:
        return "Happy"
    elif sentiment < 0.5:
        return "Fearful"
    else:
        return "Angry"

# Function to suggest messages based on detected emotion
def suggest_message(emotion):
    messages = {
        "Bad": "Take a deep breath and calm down.",
        "Sad": "It's okay to feel down sometimes. Talk to someone you trust.",
        "Disgusted": "Try to focus on the positive things around you.",
        "Surprised": "Life is full of surprises. Embrace the moment.",
        "Happy": "Celebrate your happiness and spread positivity.",
        "Fearful": "Take small steps to overcome your fears.",
        "Angry": "Count to ten before reacting to anger. It helps."
    }
    return messages.get(emotion, "I'm not sure how to help with that emotion.")

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)

# Perform speech recognition
try:
    input_text = recognizer.recognize_google(audio)
    print("You said:", input_text)

    # Perform sentiment analysis
    analysis = TextBlob(input_text)
    sentiment = analysis.sentiment.polarity

    # Categorize the sentiment into emotions
    emotion = categorize_emotion(sentiment)

    # Suggest a message based on the detected emotion
    suggested_message = suggest_message(emotion)

    print(f"Detected Emotion: {emotion}")
    print(f"Suggested Message: {suggested_message}")

except sr.UnknownValueError:
    print("Speech Recognition could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")
