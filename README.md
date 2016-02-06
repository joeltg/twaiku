# twaiku
Backend for the Twaiku Twitter client


## syllables api
does_word_exist(word)  
count_syllables_word(String)  
count_syllables_line(String)  
count_syllables_haiku([String])  

## Dev
Create ```server/keys.py``` that defines the string ```oxford``` to be a Microsoft Oxford WebLM API key. Then run ```python server/app.py``` to start the flask server.
