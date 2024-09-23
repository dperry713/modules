def mood_response(mood):
    mood_responses = {
        "happy": "That's great to hear! Keep smiling! 😊",
        "sad": "I'm sorry to hear that. I hope things get better soon. 💙",
        "excited": "Awesome! What's got you so excited? 🎉",
        "angry": "Take a deep breath. It's going to be okay. 💪",
        "tired": "Make sure to get some rest. You deserve it. 😴",
        "bored": "How about trying something new today? 🌟"
    }
    return mood_responses.get(mood.lower(), "I'm not sure how to respond to that, but I hope you have a good day! 🌈")