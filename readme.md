## Description
A personalized language-learning app designed to help you read and understand chinese books. The app processes the book sentence by sentence, allowing you to translate each sentence, view the correct translation, and learn new vocabulary in context.  
Later, connection to some cards app like anki would be done, so that when adding new words to the "review bucket", you can learn them separately.
![App Screenshot](screenshot.png)
## How to use
First - put a chinese book in pdf format into backend folder. Change the name in files to load it properly   
backend: create venv, run setup.sh, run main.sh  
frontend: npm install, npm run dev  
then, go to http://localhost:5173/reader and read your book sentence by sentence
## Attributions
Chinese dictionary is CC-CEDICT: https://www.mdbg.net/chinese/dictionary?page=cedict
