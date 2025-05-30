# Chandler Sarcasm AI Assistant (like.... Coould It Be Any Snaekier)

This is a Chandler Bing-inspired voice assistant built with Python, Vosk (for offline speech recognition), and pyttsx3 (for text-ro-speech). It listens to your voice, decodes what you say, and hits you with responses dripping in sarcasm and sass — because why not?

---

## Features

- 🎤 Offine Voice Recognition using Vosk
- 🤖 Randomized fallbacks responses if it doesn't understand you  
- 🗣️ Text-to-Speech with bulit-in sarcasm via
- 😂 Snarky One-Liners inspired by Chandler Bing from _Friends_  
- ❌ Safe Exit with commandes like "exit", "goodbye", or "see you later"

---

## Requriements

Before running the assistant, make sure to install the following:

pip install vosk pyttsx3 sounddevice

Also, download a Vosk model (e.g. small English model):

wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip
mv vosk-model-small-en-us-0.15 Model

---

## How It Works
 1. The assistant continuously listens for your voice input using sounddevice.
 2. Vosk processes your voice and converts it into text.
 3. Based on keywords in your input, Chandler responds with a sarcastic remark.
 4. If it doesn't match any keyword? You still get judged.

---

## How To Run 

python chandler_assistant.py
Then say something like:

“Hello”

“Tell me a joke”

“How are you?”

“What's the weather?”

“You’re irritating”

Say exit, goodbye, or see you later to end the chat.

---

## 🤖 Sample Responses

You Say	Chandler Replies
"hello"	"Hey! Let's pretend I'm excited to talk to you."
"thank you"	"Thank me? Wow. Someone’s standards are low."
"how are you?"	"Living the dream. The nightmare version, obviously."
"tell me something"	"Something. There. I told you something."
"You're irritating"	"Oh, am I irritating you? Well, could I be any more successful at my job then?"

---

## 👋 Exit with Flair
"Could I be leaving any faster?"

---

## ⚠️ Note
This assistant is just for fun and is not meant to be taken seriously. Please don't ask it to do your taxes. Or do. It’ll definitely judge you either way.

---
