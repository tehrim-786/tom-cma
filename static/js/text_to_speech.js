let speech = new SpeechSynthesisUtterance();
let voices = []
voices = window.speechSynthesis.getVoices();
speech.voice=voices[0]

speech.text = document.getElementById('results').textContent;
window.speechSynthesis.speak(speech)
