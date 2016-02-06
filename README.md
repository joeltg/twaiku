# twaiku
Backend for the Twaiku Twitter client

## synonym api
get_synonyms(String) -> [String]      

## syllables api
does_word_exist(String) -> Boolean  
count_syllables_word(String) -> Int  
count_syllables_line(String) -> Int    
count_syllables_haiku([String]) -> [Int]    

## Dev
Create ```server/keys.py``` that defines the string ```oxford``` to be a Microsoft Oxford WebLM API key. Then run ```python server/app.py``` to start the flask server.
