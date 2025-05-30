import pyttsx3
import json
import queue
import sounddevice as sd
import vosk
import random

#initialize tts engine
engine = pyttsx3.init()

#load vosk model
model = vosk.Model("Model")

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))


def recognize():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16', channels=1, callback=callback):
        rec= vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                return result.get("text", "")


responses = {
    "hello":[
        "Hello! Oh look, it's my favorite person... said no one ever.",
        "Hey! Let's pretend I'm excited to talk to you.",
        "Hi. You again? What did I do to deserve this honor."
    ],
    "thank you":[
        "You’re welcome. But let’s not make this a habit",
        "Don’t mention it. No, seriously… don’t mention it.",
        "Thank me? Wow. Someone’s standards are low."
    ],
    "time":[
        "Oh look, it’s time again… to question all your life choices.",
        "Well it’s time o’clock. Better get back to doing absolutely nothing productive.",
        "Ah, time… nature’s way of reminding us we're late for something"
    ],
    "joke":
    [
        "My career. Oh wait, you meant a joke-joke?",
        "Why did the assistant cross the road? To escape user input.",
        "I told a joke once. The therapist is still recovering."
    ],
    "Weather":[
      "Today’s forecast is throwing more mood swings than Ross deciding between Rachel and Julie.",
       "Oh look, sunshine! Like Joey finding pizza — everyone’s happy.",
        " Clouds are creeping in… probably because someone forgot to laugh at my jokes.",
        "Rain might show up, and no, it’s not just Monica crying over a dirty kitchen."
    ],
    "How are you":[
        "Oh, I’m fine. You know, for someone whose life is a sitcom without a laugh track.",
        "Living the dream. The nightmare version, obviously.",
        "I'm great! If by great, you mean slowly unraveling but with sarcasm."
    ],
    "okay":[
     "Okay? That’s it? Wow, bring the excitement down a notch.",
        "Just okay? Was it something I didn’t say?",
        "Alright? You sound like you just agreed to do your taxes."
    ],
    "what are you doing":[
        "Talking to you. Clearly, I peaked.",
        "Oh, just waiting for my existential crisis to finish buffering.",
        "Nothing much, just sitting here — being artificial and judgmental."
    ],
    "tell me something":[
        "Did you know lobsters mate for life? Unlike most people you know.",
        "Here's something: Life is like coffee. Bitter, but addictive.",
        "Something. There. I told you something."
    ],
    "that's not funny":[
        "Not funny? Ouch. I’ll send that feedback straight to my therapist — oh wait, I’m the therapist.",
        "You know who else didn’t laugh? My boss. Now we're both here."
    ],
    "irritating":[
        "Oh, am I irritating you? Well, could I be any more successful at my job then?",
        "I mean, it's not easy being this charmingly annoying — it takes years of practice and emotional repression.",
        "But hey, if I’m the most irritating thing in your day… you’re doing great, buddy. 😏"
    ]

}
            

def get_chandler_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return random.choice(responses["hello"])
    elif"thank you" in user_input:
        return random.choice(responses["thank you"])
    elif"time" in user_input:
        return random.choice(responses["time"])
    elif"joke" in user_input:
        return random.choice(responses["joke"])
    elif"weather" in user_input:
        return random.choice(responses["Weather"])
    elif "how are you" in user_input:
        return random.choice(responses['How are you'])
    elif"okay" in user_input:
        return random.choice(responses["okay"])
    elif "what are you doing"in user_input:
        return random.choice(responses["what are you doing"])
    elif"tell me something" in user_input:
        return random.choice(responses["tell me something"])
    elif "funny" in user_input:
        return random.choice(responses["that's not funny"])
    elif"irritating" in user_input:
        return random.choice(responses["irritating"])
  
    else:
        fallback_line =[
           f"You said '{user_input}'... Should I pretend that's not slightly terrifying?",
        f"Hmm. '{user_input}', huh? That’s definitely... a sentence.",
        f"Interesting. And by interesting, I mean totally confusing.",
        f"Wow, I understood that less than I understand my own feelings.",
        f"You said '{user_input}'. I'm still processing the trauma.",
        f"Is that a command or just an existential cry for help?",
        f"Are we sure you're not just messing with me right now?"   
        ]

        follow_ups = [
            "So, what else is on your mind?",
            "Ask me something, or I’ll just keep judging you silently.",
            "Come on, don’t leave me hanging here.",
            "Keep talking, I’m here for the entertainment.",
            "You can do better than that, try again!"
        ]
        
        fallback = random.choice(fallback_line).format(user_input)
        follow_up = random.choice(follow_ups)
        return f"{fallback} {follow_up}"
       
    

#main loop
while True:
    print("🎤 Listening... Say Something:")
    text = recognize()
    print("🗣️ You Said:" , text)

    if text.lower() in ["exit", "goodbye", "see you later"]:
        print("👋 Chandler says: Could i *be* leaving any faster?")
        engine.say("could I*be* leaving any faster?")
        engine.runAndWait()
        break


    response = get_chandler_response(text)
    print("🤖 Chandler says:", response)
    engine.say(response)
    engine.runAndWait()

