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
| as           | Assamese                  |
| bn           | Bangla                    |
| brx          | Bodo                      |
| doi          | Dogri                     |
| en           | English                   |
| gu           | Gujarati                  |
| hi           | Hindi                     |
| kn           | Kannada                   |
| ks           | Kashmiri                  |
| kok          | Konkani                   |
| mai          | Maithili                  |
| ml           | Malayalam                 |
| mr           | Marathi                   |
| mni          | Manipuri                  |
| ne           | Nepali                    |
| or           | Odia                      |
| pa           | Panjabi                   |
| sa           | Sanskrit                  |
| sd           | Sindhi                    |
| ta           | Tamil                     |
| te           | Telugu                    |
| ur           | Urdu                      |


iso_codes = {
    'Assamese': 'as',
    'Bengali': 'bn',
    'Bodo': 'brx',
    'Dogri': 'doi',
    'Gujarati': 'gu',
    'Hindi': 'hi',
    'Kannada': 'kn',
    'Kashmiri': 'ks',
    'Konkani': 'kok',
    'Maithili': 'mai', 
    'Malayalam': 'ml',
    'Manipuri': 'mni',
    'Marathi': 'mr',
    'Nepali': 'ne',
    'Odia': 'or',
    'Punjabi': 'pa',
    'Sanskrit': 'sa',
    'Santali': 'sat', 
    'Sindhi': 'sd',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Urdu': 'ur'
}

## Release Notes

This package contains work on converting numbers to words. The contents of this package can also be downloaded from our [GitHub repo.](https://github.com/AI4Bharat/indic-numtowords)
