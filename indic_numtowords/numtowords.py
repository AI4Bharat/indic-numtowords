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

supported_langs = ('as', 'bn', 'en', 'gu', 'hi', 'ml', 'mr', 'or', 'pa', 'ta', 'te', 'kn', 'ur')
lang_func_dict = {
    'as': as_convert,
    'bn': bn_convert,
    'en': en_convert,
    'gu': gu_convert,
    'hi': hi_convert,
    'ml': ml_convert,
    'mr': mr_convert,
    'or': or_convert,
    'pa': pa_convert,
    'ta': ta_convert,
    'te': te_convert,
    'kn': kn_convert,
    'ur': ur_convert
}


def num2words(num, lang = 'en', variations = False):
    if lang not in supported_langs:
        raise Exception("Language not supported. Please check the language code")
    results = lang_func_dict[lang](num)
    if variations == False:
        return results[0]
    variations = list(set(get_variations(num, lang)))
    results.extend(variations)
    results = [re.sub(r"[\u200c\u200b]", "", line) for line in results]
    return results


user_variation_file_map = {
    'as' : as_variations,
    'bn' : bn_variations,
    'en' : en_variations,
    'gu' : gu_variations,
    'hi' : hi_variations,
    'ml' : ml_variations,
    'mr' : mr_variations,
    'or' : or_variations,
    'pa' : pa_variations,
    'ta' : ta_variations,
    'te' : te_variations,
    'kn' : kn_variations,
    'ur' : ur_variations

}

def add_variation(num, word, lang):
    #first read all the variations from the tsv file
    user_variation_file = user_variation_file_map[lang]
    user_variation_dict = dict()
    with open(user_variation_file, 'r') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            user_variation_dict[row[0]] = list(row[1:])
    if num in user_variation_dict:
        user_variation_dict[num].append(word)
    else:
        user_variation_dict[num] = [word]
    
    with open(user_variation_file, 'w') as f:
        for num in user_variation_dict.keys():
            line = num + '\t'
            for word in user_variation_dict[num]:
                line += word + '\t'
            line = line.strip()
            line += '\n'
            f.write(line)



def get_variations(num, lang):

    user_variation_dict = user_variation_file_map[lang]
    
    if int(num) in user_variation_dict:
        return set(user_variation_dict[int(num)])
    else:
        return set()
