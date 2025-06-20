
from textblob import TextBlob

def tespit_et(cumle):
    blob = TextBlob(cumle)
    if blob.sentiment.polarity > 0.3:
        return "mutlu"
    elif blob.sentiment.polarity < -0.3:
        return "üzgün"
    elif abs(blob.sentiment.polarity) < 0.1:
        return "sinirli"
    else:
        return "mutlu"
