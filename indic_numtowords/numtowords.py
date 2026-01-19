import re
import csv

from indic_numtowords.asm.cardinal import convert as as_convert
from indic_numtowords.ben.cardinal import convert as bn_convert
from indic_numtowords.eng.cardinal import convert as en_convert
from indic_numtowords.guj.cardinal import convert as gu_convert
from indic_numtowords.hin.cardinal import convert as hi_convert
from indic_numtowords.mal.cardinal import convert as ml_convert
from indic_numtowords.mar.cardinal import convert as mr_convert
from indic_numtowords.ori.cardinal import convert as or_convert
from indic_numtowords.pun.cardinal import convert as pa_convert
from indic_numtowords.tam.cardinal import convert as ta_convert
from indic_numtowords.tel.cardinal import convert as te_convert
from indic_numtowords.kan.cardinal import convert as kn_convert
from indic_numtowords.urd.cardinal import convert as ur_convert

from indic_numtowords.asm.data.user_variations import variations as as_variations
from indic_numtowords.ben.data.user_variations import variations as bn_variations
from indic_numtowords.eng.data.user_variations import variations as en_variations
from indic_numtowords.guj.data.user_variations import variations as gu_variations
from indic_numtowords.hin.data.user_variations import variations as hi_variations
from indic_numtowords.mal.data.user_variations import variations as ml_variations
from indic_numtowords.mar.data.user_variations import variations as mr_variations
from indic_numtowords.ori.data.user_variations import variations as or_variations
from indic_numtowords.pun.data.user_variations import variations as pa_variations
from indic_numtowords.tam.data.user_variations import variations as ta_variations
from indic_numtowords.tel.data.user_variations import variations as te_variations
from indic_numtowords.kan.data.user_variations import variations as kn_variations
from indic_numtowords.urd.data.user_variations import variations as ur_variations

from indic_numtowords.doi.data.nums import DIRECT_DICT as doi_direct_dict
from indic_numtowords.sat.data.nums import DIRECT_DICT as sat_direct_dict
from indic_numtowords.mai.data.nums import DIRECT_DICT as mai_direct_dict
from indic_numtowords.sin.data.nums import DIRECT_DICT as sd_direct_dict
from indic_numtowords.brx.data.nums import DIRECT_DICT as brx_direct_dict
from indic_numtowords.nep.data.nums import DIRECT_DICT as ne_direct_dict
from indic_numtowords.mni.data.nums import DIRECT_DICT as mni_direct_dict
from indic_numtowords.kok.data.nums import DIRECT_DICT as kok_direct_dict
from indic_numtowords.kas.data.nums import DIRECT_DICT as ks_direct_dict
from indic_numtowords.san.data.nums import DIRECT_DICT as sa_direct_dict

from indic_numtowords.doi.data.nums import EXCEPTIONS_DICT as doi_exceptions_dict
from indic_numtowords.sat.data.nums import EXCEPTIONS_DICT as sat_exceptions_dict
from indic_numtowords.mai.data.nums import EXCEPTIONS_DICT as mai_exceptions_dict
from indic_numtowords.sin.data.nums import EXCEPTIONS_DICT as sd_exceptions_dict
from indic_numtowords.brx.data.nums import EXCEPTIONS_DICT as brx_exceptions_dict
from indic_numtowords.nep.data.nums import EXCEPTIONS_DICT as ne_exceptions_dict
from indic_numtowords.mni.data.nums import EXCEPTIONS_DICT as mni_exceptions_dict
from indic_numtowords.kok.data.nums import EXCEPTIONS_DICT as kok_exceptions_dict
from indic_numtowords.kas.data.nums import EXCEPTIONS_DICT as ks_exceptions_dict
from indic_numtowords.san.data.nums import EXCEPTIONS_DICT as sa_exceptions_dict

from indic_numtowords.doi.utils import split_number as doi_split_number
from indic_numtowords.sat.utils import split_number as sat_split_number
from indic_numtowords.mai.utils import split_number as mai_split_number
from indic_numtowords.sin.utils import split_number as sd_split_number
from indic_numtowords.brx.utils import split_number as brx_split_number
from indic_numtowords.nep.utils import split_number as ne_split_number
from indic_numtowords.mni.utils import split_number as mni_split_number
from indic_numtowords.kok.utils import split_number as kok_split_number
from indic_numtowords.kas.utils import split_number as ks_split_number
from indic_numtowords.san.utils import split_number as sa_split_number

from indic_numtowords.doi.cardinal import process_text as doi_process_text
from indic_numtowords.sat.cardinal import process_text as sat_process_text
from indic_numtowords.mai.cardinal import process_text as mai_process_text
from indic_numtowords.sin.cardinal import process_text as sd_process_text
from indic_numtowords.brx.cardinal import process_text as brx_process_text
from indic_numtowords.nep.cardinal import process_text as ne_process_text
from indic_numtowords.mni.cardinal import process_text as mni_process_text
from indic_numtowords.kok.cardinal import process_text as kok_process_text
from indic_numtowords.kas.cardinal import process_text as ks_process_text
from indic_numtowords.san.cardinal import process_text as sa_process_text

supported_langs = (
    "as",
    "bn",
    "en",
    "gu",
    "hi",
    "ml",
    "mr",
    "or",
    "pa",
    "ta",
    "te",
    "kn",
    "ur",
)
extended_supported_langs = (
    "doi",
    "sat",
    "mai",
    "sd",
    "brx",
    "ne",
    "mni",
    "kok",
    "ks",
    "sa",
)

lang_func_dict = {
    "as": as_convert,
    "bn": bn_convert,
    "en": en_convert,
    "gu": gu_convert,
    "hi": hi_convert,
    "ml": ml_convert,
    "mr": mr_convert,
    "or": or_convert,
    "pa": pa_convert,
    "ta": ta_convert,
    "te": te_convert,
    "kn": kn_convert,
    "ur": ur_convert,
}

user_variation_file_map = {
    "as": as_variations,
    "bn": bn_variations,
    "en": en_variations,
    "gu": gu_variations,
    "hi": hi_variations,
    "ml": ml_variations,
    "mr": mr_variations,
    "or": or_variations,
    "pa": pa_variations,
    "ta": ta_variations,
    "te": te_variations,
    "kn": kn_variations,
    "ur": ur_variations,
}

direct_dict_mapping = {
    "doi": doi_direct_dict,
    "sat": sat_direct_dict,
    "mai": mai_direct_dict,
    "sd": sd_direct_dict,
    "brx": brx_direct_dict,
    "ne": ne_direct_dict,
    "mni": mni_direct_dict,
    "kok": kok_direct_dict,
    "ks": ks_direct_dict,
    "sa": sa_direct_dict,
}

exceptions_dict_mapping = {
    "doi": doi_exceptions_dict,
    "sat": sat_exceptions_dict,
    "mai": mai_exceptions_dict,
    "sd": sd_exceptions_dict,
    "brx": brx_exceptions_dict,
    "ne": ne_exceptions_dict,
    "mni": mni_exceptions_dict,
    "kok": kok_exceptions_dict,
    "ks": ks_exceptions_dict,
    "sa": sa_exceptions_dict,
}

split_number_mapping = {
    "doi": doi_split_number,
    "sat": sat_split_number,
    "mai": mai_split_number,
    "sd": sd_split_number,
    "brx": brx_split_number,
    "ne": ne_split_number,
    "mni": mni_split_number,
    "kok": kok_split_number,
    "ks": ks_split_number,
    "sa": sa_split_number,
}

process_text_mapping = {
    "doi": doi_process_text,
    "sat": sat_process_text,
    "mai": mai_process_text,
    "sd": sd_process_text,
    "brx": brx_process_text,
    "ne": ne_process_text,
    "mni": mni_process_text,
    "kok": kok_process_text,
    "ks": ks_process_text,
    "sa": sa_process_text,
}

# Decimal point words for each language
decimal_point_words = {
    "en": "point",
    "hi": "दशमलव",
    "bn": "দশমিক",
    "ta": "புள்ளி",
    "te": "పాయింట్",
    "mr": "दशांश",
    "gu": "દશાંશ",
    "kn": "ದಶಮಾಂಶ",
    "ml": "പോയിന്റ്",
    "pa": "ਦਸ਼ਮਲਵ",
    "or": "ଦଶମିକ",
    "as": "দশমিক",
    "ur": "اعشاریہ",
    "ne": "दशमलव",
    "sa": "दशमलव",
    "kok": "दशांश",
    "mai": "दशमलव",
    "doi": "दशमलव",
    "sd": "ڏهاڪو",
    "brx": "दशमलव",
    "mni": "দশমিক",
    "ks": "دَشمَلَو",
    "sat": "दशमलव",
}

# Indian Rupee currency terms for each language
# Format: {"unit": "rupees word", "subunit": "paise word", "connector": "and word"}
currency_formats = {
    "INR": {
        "en": {"unit": "rupees", "subunit": "paise", "connector": "and"},
        "hi": {"unit": "रुपये", "subunit": "पैसे", "connector": "और"},
        "bn": {"unit": "টাকা", "subunit": "পয়সা", "connector": "এবং"},
        "ta": {"unit": "ரூபாய்", "subunit": "பைசா", "connector": "மற்றும்"},
        "te": {"unit": "రూపాయలు", "subunit": "పైసలు", "connector": "మరియు"},
        "mr": {"unit": "रुपये", "subunit": "पैसे", "connector": "आणि"},
        "gu": {"unit": "રૂપિયા", "subunit": "પૈસા", "connector": "અને"},
        "kn": {"unit": "ರೂಪಾಯಿ", "subunit": "ಪೈಸೆ", "connector": "ಮತ್ತು"},
        "ml": {"unit": "രൂപ", "subunit": "പൈസ", "connector": "ഉം"},
        "pa": {"unit": "ਰੁਪਏ", "subunit": "ਪੈਸੇ", "connector": "ਅਤੇ"},
        "or": {"unit": "ଟଙ୍କା", "subunit": "ପଇସା", "connector": "ଏବଂ"},
        "as": {"unit": "টকা", "subunit": "পইচা", "connector": "আৰু"},
        "ur": {"unit": "روپے", "subunit": "پیسے", "connector": "اور"},
        "ne": {"unit": "रुपैयाँ", "subunit": "पैसा", "connector": "र"},
        "sa": {"unit": "रूप्यकाणि", "subunit": "पैसाः", "connector": "च"},
        "kok": {"unit": "रुपया", "subunit": "पैसे", "connector": "आनी"},
        "mai": {"unit": "टाका", "subunit": "पैसा", "connector": "आ"},
        "doi": {"unit": "रुपये", "subunit": "पैसे", "connector": "ते"},
        "sd": {"unit": "رپيا", "subunit": "پئسا", "connector": "۽"},
        "brx": {"unit": "रां", "subunit": "पैसा", "connector": "आरो"},
        "mni": {"unit": "রুপি", "subunit": "পয়সা", "connector": "অমসুং"},
        "ks": {"unit": "رۄپیہ", "subunit": "پیسہ", "connector": "تہٕ"},
        "sat": {"unit": "टाका", "subunit": "पैसा", "connector": "आर"},
    }
}


def _convert_integer(number, lang, variations=False, split=False):
    """
    Internal helper to convert an integer to words.
    This extracts the core integer conversion logic from num2words.
    """
    if lang in extended_supported_langs:
        return num2words_extended(number, lang=lang, variations=variations, split=split)

    if lang not in supported_langs:
        raise ValueError("Language not supported. Please check the language code.")

    number_str = str(number)
    extended = len(number_str) > 9

    if extended or split:
        return " ".join(lang_func_dict[lang](digit)[0] for digit in str(number))

    results = lang_func_dict[lang](number)
    if not variations:
        return results[0]
    variation_list = list(set(get_variations(number, lang)))
    results.extend(variation_list)
    results = [re.sub(r"[\u200c\u200b]", "", line) for line in results]
    return results


def num2words(number, lang="en", variations=False, split=False, currency=None):
    """
    Convert a number to its textual representation in a specified language.

    Args:
        number (int, float, or str): The number to convert.
        lang (str): The ISO code for the target language. Defaults to English ('en').
        variations (bool, optional): If True, returns variations of the number.
        split (bool, optional): If True, converts each digit separately.
        currency (str, optional): Currency code (e.g., 'INR') for currency formatting.
            When provided, formats the number as currency (e.g., "forty-two rupees and fifty paise").

    Returns:
        str: The textual representation of the number.
        list[str]: A list of variations if `variations` is True.

    Examples:
        >>> num2words(42.5, lang='en')
        'forty-two point five'
        >>> num2words(42.50, lang='en', currency='INR')
        'forty-two rupees and fifty paise'
        >>> num2words(100.25, lang='hi', currency='INR')
        'एक सौ रुपये और पच्चीस पैसे'
    """
    # Validate language
    all_supported = supported_langs + extended_supported_langs
    if lang not in all_supported:
        raise ValueError("Language not supported. Please check the language code.")

    # Handle string input - normalize and check for decimal
    if isinstance(number, str):
        number = number.strip().replace(",", "")
        # Check if it's a decimal number
        if "." in number:
            try:
                number = float(number)
            except ValueError:
                raise ValueError("Input string must be a valid number")
        elif number.lstrip("-").isdigit():
            number = int(number)
        else:
            raise ValueError("Input string must be a valid number")

    # Handle float/decimal numbers
    if isinstance(number, float):
        return _convert_decimal(number, lang, currency)

    # Handle currency for integer amounts (e.g., 100 rupees and zero paise)
    if currency is not None:
        return _convert_decimal(float(number), lang, currency)

    # Original integer conversion logic
    return _convert_integer(number, lang, variations, split)


def _convert_decimal(number, lang, currency=None):
    """
    Convert a decimal number to words.

    Args:
        number (float): The decimal number to convert.
        lang (str): The language code.
        currency (str, optional): Currency code for currency formatting.

    Returns:
        str: The textual representation of the decimal number.
    """
    # Convert to string to handle precision
    number_str = str(number)

    # Handle negative numbers
    is_negative = number < 0
    if is_negative:
        number_str = number_str[1:]  # Remove minus sign

    # Split into whole and fractional parts
    if "." in number_str:
        whole_str, frac_str = number_str.split(".")
    else:
        whole_str, frac_str = number_str, "0"

    # Convert whole part
    whole_int = int(whole_str) if whole_str else 0
    whole_words = _convert_integer(whole_int, lang)

    # For currency mode
    if currency is not None:
        if currency not in currency_formats:
            raise ValueError(f"Currency '{currency}' is not supported. Supported: {list(currency_formats.keys())}")

        currency_info = currency_formats[currency].get(lang)
        if currency_info is None:
            raise ValueError(f"Currency '{currency}' is not available for language '{lang}'")

        # For INR, paise is 1/100 of rupee, so we need 2 decimal places
        # Pad or truncate fractional part to 2 digits for paise
        frac_str = frac_str[:2].ljust(2, "0")
        frac_int = int(frac_str)

        frac_words = _convert_integer(frac_int, lang) if frac_int > 0 else None

        # Build currency string
        result = f"{whole_words} {currency_info['unit']}"
        if frac_words:
            result += f" {currency_info['connector']} {frac_words} {currency_info['subunit']}"

        if is_negative:
            # Add negative indicator (minus/negative in the language)
            negative_words = {"en": "minus", "hi": "ऋण", "bn": "ঋণাত্মক"}
            negative_word = negative_words.get(lang, "minus")
            result = f"{negative_word} {result}"

        return result

    # For decimal point mode (non-currency)
    decimal_word = decimal_point_words.get(lang, "point")

    # Convert fractional part digit by digit
    frac_digit_words = []
    for digit in frac_str:
        digit_word = _convert_integer(int(digit), lang)
        frac_digit_words.append(digit_word)

    frac_words = " ".join(frac_digit_words)

    result = f"{whole_words} {decimal_word} {frac_words}"

    if is_negative:
        negative_words = {"en": "minus", "hi": "ऋण", "bn": "ঋণাত্মক"}
        negative_word = negative_words.get(lang, "minus")
        result = f"{negative_word} {result}"

    return result


def num2words_extended(
    number: int | str, lang: str, variations: bool = False, split: bool = False
) -> str | list:
    """
    Convert a number to its textual representation in a specified Indian language.

    Args:
        number (int or str): The number to convert, provided as an integer or a numeric string.
        lang (str): The language code representing the target Indian language for conversion.
        variations (bool, optional): Returns a list of possible textual variations if set to True. Defaults to False.
        split (bool, optional): Converts each digit separately into its word form when set to True. Defaults to False.

    Returns:
        str: The textual representation of the number if `variations` is False.
        list[str]: A list of textual variations if `variations` is True.

    Raises:
        ValueError: If the input is not a valid number.
    """
    number_str = str(number).lstrip("0") or "0"

    extended = len(number_str) > 9

    if extended or split:
        return " ".join(
            direct_dict_mapping[lang][digit][0]
            for digit in (number if split else number_str)
        )

    numbers = split_number_mapping[lang](number_str)
    converted_text = []

    for index, num in enumerate(numbers if lang != "sa" else reversed(numbers)):
        index = len(numbers) - 1 - index if lang == "sa" else index
        converted_text = process_text_mapping[lang](
            num, converted_text, index, len(number_str)
        )

    exceptions = exceptions_dict_mapping[lang].get(number_str, [])

    result_text = (
        exceptions + [re.sub(r"[\u200c\u200b]", "", i) for i in converted_text]
        if lang == "ks"
        else [re.sub(r"[\u200c\u200b]", "", i) for i in converted_text] + exceptions
    )

    idx = -1 if lang == "ks" else 0

    return result_text if variations else result_text[idx]


def add_variation(num, word, lang):
    user_variation_file = user_variation_file_map[lang]
    user_variation_dict = dict()

    with open(user_variation_file, "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for row in reader:
            user_variation_dict[row[0]] = list(row[1:])

    if num in user_variation_dict:
        user_variation_dict[num].append(word)
    else:
        user_variation_dict[num] = [word]

    with open(user_variation_file, "w") as f:
        for num in user_variation_dict.keys():
            line = num + "\t"
            for word in user_variation_dict[num]:
                line += word + "\t"
            line = line.strip()
            line += "\n"
            f.write(line)


def get_variations(num, lang):
    user_variation_dict = user_variation_file_map[lang]

    if int(num) in user_variation_dict:
        return set(user_variation_dict[int(num)])
    else:
        return set()
