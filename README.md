
# AI4Bharat num2words

> A module to convert numbers to words for Indian languages and English.

## Installation

To install the module, run the following command:
```sh
pip install indic-numtowords
```

## Import

To use the library, import it using the following command:
```ssh
from indic_numtowords import num2words 
```

## Usage

1. Converts numbers into words in various languages:
  ```ssh
  words = num2words(38, lang='ta')
  #output: 'முப்பத்து எட்டு'
  ```
2. Returns variations for numbers:
  ```ssh
  words = num2words(150, lang='hi', variations=True)
  #output: ['एक सौ पचास', 'डेढ़ सौ'] 
  ```
3. Converts each digit separately:
  ```ssh
  words = num2words(420, lang='doi', split=True)
  #output: 'चार दो सिफर'
  ```

## Parameters
The `num2words` function accepts the following parameters:

- **`number`**: (int) The non-negative integer to convert into words.
- **`lang`**: (str) The ISO code for the target language. Defaults to English (`en`).
- **`variations`**: (bool, optional) If set to `True`, returns variations of the number.
- **`split`**: (bool, optional) If `True`, converts each digit separately into its word form.

## Supported Languages
The following languages are supported by the `num2words` module:

- **`as`**: Assamese
- **`bn`**: Bengali
- **`brx`**: Bodo
- **`doi`**: Dogri
- **`en`**: English
- **`gu`**: Gujarati
- **`hi`**: Hindi
- **`kn`**: Kannada
- **`ks`**: Kashmiri
- **`kok`**: Konkani
- **`mai`**: Maithili
- **`ml`**: Malayalam
- **`mr`**: Marathi
- **`mni`**: Manipuri
- **`ne`**: Nepali
- **`or`**: Odia
- **`pa`**: Punjabi
- **`sa`**: Sanskrit
- **`sat`**: Santali
- **`sd`**: Sindhi
- **`ta`**: Tamil
- **`te`**: Telugu
- **`ur`**: Urdu

## Release Notes

This package contains work on converting numbers to words. The contents of this package can also be downloaded from our [GitHub repo.](https://github.com/AI4Bharat/indic-numtowords)

## Meta

Distributed under the MIT license. See LICENSE for more information.
