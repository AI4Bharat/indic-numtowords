# AI4Bharat num2words

A module to convert numbers to words for Indian languages and English.

## Installation

```
pip install indic-numtowords
```

## Usage

```
from indic_numtowords import num2words 

words = num2words(38, lang='ta', variations=False)
#output: 'முப்பத்து எட்டு'

words = num2words(150, lang='hi', variations=True)
#output: ['एक सौ पचास', 'डेढ़ सौ'] 

```

## Supported Languages

| ISO 639 Code | Language                  |
| ------------ | ------------------------- |
| as           | Assamese - অসমীয়া |
| bn           | Bangla - বাংল         |
| en           | English                   |
| gu           | Gujarati - ગુજરાત   |
| hi           | Hindi - हिंद          |
| kn           | Kannada - ಕನ್ನ        |
| ml           | Malayalam - മലയാള    |
| mr           | Marathi - मराठी      |
| or           | Oriya - ଓଡ଼ି          |
| pa           | Panjabi - ਪੰਜਾਬ      |
| ta           | Tamil - தமிழ          |
| te           | Telugu - తెలుగ       |
| ur           | Urdu - اُردُ         |

## Release Notes

This package contains work on converting numbers to words. The contents of this package can also be downloaded from our [GitHub repo.](https://github.com/AI4Bharat/indic-numtowords)
