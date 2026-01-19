
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

### Basic Integer Conversion

```python
words = num2words(38, lang='ta')
# Output: 'முப்பத்து எட்டு'
```

### Decimal Numbers (New in v1.1.0)

```python
words = num2words(42.5, lang='en')
# Output: 'forty two point five'

words = num2words(3.14, lang='hi')
# Output: 'तीन दशमलव एक चार'
```

### Currency Formatting (New in v1.1.0)

```python
words = num2words(42.50, lang='en', currency='INR')
# Output: 'forty two rupees and fifty paise'

words = num2words(100.25, lang='hi', currency='INR')
# Output: 'एक सौ रुपये और पच्चीस पैसे'

words = num2words(50.75, lang='ta', currency='INR')
# Output: 'ஐம்பது ரூபாய் மற்றும் எழுபத்து ஐந்து பைசா'
```

### Variations

```python
words = num2words(150, lang='hi', variations=True)
# Output: ['एक सौ पचास', 'डेढ़ सौ']
```

### Split Digits

```python
words = num2words(420, lang='doi', split=True)
# Output: 'चार दो सिफर'
```

## Parameters

The `num2words` function accepts the following parameters:

- **`number`**: (int, float, or str) The number to convert into words. Supports integers, decimals, and string representations.
- **`lang`**: (str) The ISO code for the target language. Defaults to English (`en`).
- **`variations`**: (bool, optional) If set to `True`, returns variations of the number.
- **`split`**: (bool, optional) If `True`, converts each digit separately into its word form.
- **`currency`**: (str, optional) Currency code for currency formatting. Currently supports `'INR'` (Indian Rupee).

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
