
# Digital Parrot
Emulate a parrot behavior,
responding randomly to ongoing conversations.
As a fun demo project.

## Operating principle

- Find speech phrases in incoming audio stream. Fixed length
- Trigger on some (but not all) phrases. Randomly
- Send phrase to Speech Recognition model to get text. Online API
- Feed the text as a prompt for text generation model. Online API
- Use a Text to Speech model to generate audio. Online API
- Play back the audio locally


## Physical embodiment

- Run on a single board computer. Like Raspberry PI
- 3d print a parrot shape.

## Sound like a parrot
- Use a TTS model that can be styled as a parrot
- Might need a lot of parrot audio??

## Be funny
- Use a text generation tailored for making jokes etc
Maybe pick out particular words in phrases, repeat

## Fully it local

Replace use of online APIs with local models
Lots of integration work to make it work.
Might not be doable on a RPi, but need GPU
