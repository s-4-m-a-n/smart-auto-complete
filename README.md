# smart-auto-complete :black_nib:
enhancing Nepali News Writing with Intelligent Auto-Complete

# Description
"SmartAutoComplete" is an innovative project designed to revolutionize Nepali news writing by incorporating intelligent auto-complete functionality. This cutting-edge solution aims to assist journalists, editors, and writers in the creation of high-quality news articles by providing real-time suggestions and completing words or phrases based on context.
With a deep understanding of the Nepali language, SmartAutoComplete harnesses the power of advanced machine learning algorithms and natural language processing techniques.
Using a user-friendly interface, writers can seamlessly integrate SmartAutoComplete into their writing process. As they type, the system autocomplete the current or next words. This predictive capability enables writers to maintain a smooth writing flow, save time, and enhance the overall quality of their news pieces.

# Features
- Real-time auto-complete suggestions based on context and user input :ballot_box_with_check:
- Intelligent prediction of words, phrases, and sentence structures commonly used in Nepali news writing :ballot_box_with_check:
- User-friendly interface seamlessly integrated into the writing process :ballot_box_with_check:
- *Personalization and adaptation to individual writing styles* (Future work) :black_square_button: 
- *Up-to-date suggestions incorporating the latest trends and popular phrases in Nepali news* (Future work) :black_square_button:

# Technology used
- Front-end: HTML, CSS, JavaScript, Bootstrap
- Backend: python, flask, tensorflow, numpy

# Requirements
- Flask==2.3.2
- numpy==1.23.5
- tensorflow==2.12.0

# Usages
- Open the tool in a web browser.
- Start typing in the textarea, and the auto-complete feature will suggest completions based on the entered text.
- Press side arrow key if you want to keep the suggested text, else you can continue typing the suggested word will be removed.

# To run the app
```bash
python app.py
```

# End Point APIs Info
The auto-complete feature relies on an API that provides suggested completions for Nepali news writing. The API has the following endpoints:
- Endpoint: `/auto_complete_np`
- Method: `GET`
- Request Parameters: [`query`]
- Response Format: `{"text": "\<suggested text\>"}`
- Example Request:

  `http://localhost:5000/auto_complete_np?query=माओवादी केन्द्रका अध्यक्ष एवं प्रधानमन्त्री पुष्पकमल दाहाल प्रचण्डले ६ वर्षअघि एमाले र माओवादीबीच एकता गर्नु हतारो भएको टिप्पणी `

  
# Screenshot
![UI screenshot](https://github.com/s-4-m-a-n/smart-auto-complete/blob/main/screenshots/uI.png)

# Demo
![demo](https://github.com/s-4-m-a-n/smart-auto-complete/blob/main/screenshots/demo.gif)
