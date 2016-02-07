# twaiku
Backend for the Twaiku Twitter client

## backend output
Sample output:

[  
    [{"text":"Robert","flag": true}, {"text":"Downey","flag": false}, {"text":"charged","flag": false}],  
    [{"text":"Robert","flag": false}, {"text":"Robert","flag": false}, {"text":"Robert","flag": false}, {"text":"Robert","flag": false}],  
    [{"text":"modesto","flag": false}, {"text":"shallow","flag": false}]  
]  

## synonym api
get_synonyms(String) -> [String]      

## syllables api
does_word_exist(String) -> Boolean  
count_syllables_word(String) -> Int  
count_syllables_line(String) -> Int    
count_syllables_haiku([String]) -> [Int]    

## Dev
Create ```server/keys.py``` that defines the string ```oxford``` to be a Microsoft Oxford WebLM API key. Then run ```python server/app.py``` to start the flask server.
