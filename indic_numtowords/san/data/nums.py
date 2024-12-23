DIRECT_DICT = {
    '0': ['शून्यं'],
    '1': ['एकं'],
    '2': ['द्वे'],
    '3': ['त्रीणि'],
    '4': ['चत्वारि'],
    '5': ['पञ्च'],
    '6': ['षट्'],
    '7': ['सप्त'],
    '8': ['अष्ट'],
    '9': ['नव'],
    '10': ['दश'],
    '11': ['एकादश'],
    '12': ['द्वादश'],
    '13': ['त्रयोदश'],
    '14': ['चतुर्दश'],
    '15': ['पञ्चदश'],
    '16': ['षोडश'],
    '17': ['सप्तदश'],
    '18': ['अष्टादश'],
    '19': ['नवदश'],
    '20': ['विंशतिः'],
    '21': ['एकविंशतिः'],
    '22': ['द्वाविंशतिः'],
    '23': ['त्रयोविंशतिः'],
    '24': ['चतुर्विंशतिः'],
    '25': ['पञ्चविंशतिः'],
    '26': ['षड्विंशतिः'],
    '27': ['सप्तविंशतिः'],
    '28': ['अष्टाविंशतिः'],
    '29': ['नवविंशतिः'],
    '30': ['त्रिंशत्'],
    '31': ['एकत्रिंशत्'],
    '32': ['द्वात्रिंशत्'],
    '33': ['त्रयस्त्रिंशत्'],
    '34': ['चतुस्त्रिंशत्'],
    '35': ['पञ्चत्रिंशत्'],
    '36': ['षड्त्रिंशत्'],
    '37': ['सप्तत्रिंशत्'],
    '38': ['अष्टात्रिंशत्'],
    '39': ['नवत्रिंशत्'],
    '40': ['चत्वारिंशत्'],
    '41': ['एकचत्वारिंशत्'],
    '42': ['द्विचत्वारिंशत्'],
    '43': ['त्रिचत्वारिंशत्'],
    '44': ['चतुश्चत्वारिंशत्'],
    '45': ['पञ्चचत्वारिंशत्'],
    '46': ['षट्चत्वारिंशत्'],
    '47': ['सप्तचत्वारिंशत्'],
    '48': ['अष्टचत्वारिंशत्'],
    '49': ['नवचत्वारिंशत्'],
    '50': ['पञ्चाशत्'],
    '51': ['एकपञ्चाशत्'],
    '52': ['द्विपञ्चाशत्'],
    '53': ['त्रिपञ्चाशत्'],
    '54': ['चतुःपञ्चाशत्'],
    '55': ['पञ्चपञ्चाशत्'],
    '56': ['षड्पञ्चाशत्'],
    '57': ['सप्तपञ्चाशत्'],
    '58': ['अष्टपञ्चाशत्'],
    '59': ['नवपञ्चाशत्'],
    '60': ['षष्टिः'],
    '61': ['एकषष्टिः'],
    '62': ['द्विषष्टिः'],
    '63': ['त्रिषष्टिः'],
    '64': ['चतुःषष्टिः'],
    '65': ['पञ्चषष्टिः'],
    '66': ['षड्षष्टिः'],
    '67': ['सप्तषष्टिः'],
    '68': ['अष्टषष्टिः'],
    '69': ['नवषष्टिः'],
    '70': ['सप्ततिः'],
    '71': ['एकसप्ततिः'],
    '72': ['द्विसप्ततिः'],
    '73': ['त्रिसप्ततिः'],
    '74': ['चतुःसप्ततिः'],
    '75': ['पञ्चसप्ततिः'],
    '76': ['षड्सप्ततिः'],
    '77': ['सप्तसप्ततिः'],
    '78': ['अष्टसप्ततिः'],
    '79': ['नवसप्ततिः'],
    '80': ['अशीतिः'],
    '81': ['एकाशीतिः'],
    '82': ['द्व्यशीतिः'],
    '83': ['त्र्यशीतिः'],
    '84': ['चतुरशीतिः'],
    '85': ['पञ्चाशीतिः'],
    '86': ['षडशीतिः'],
    '87': ['सप्ताशीतिः'],
    '88': ['अष्टाशीतिः'],
    '89': ['नवाशीतिः'],
    '90': ['नवतिः'],
    '91': ['एकनवतिः'],
    '92': ['द्विनवतिः'],
    '93': ['त्रिनवतिः'],
    '94': ['चतुर्नवतिः'],
    '95': ['पञ्चनवतिः'],
    '96': ['षण्णवतिः'],
    '97': ['सप्तनवतिः'],
    '98': ['अष्टनवतिः'],
    '99': ['नवनवतिः']
}

EXCEPTIONS_DICT = {

}

NUMBER_SCALE_DICT = {
    '0' : ['शतम्'],
    '1' : ['सहस्रम्'],
    '2' : ['लक्षम्'],
    '3' : ['कोटि'],
    '4' : ['अब्ज'],
    '5' : ['खर्व'],
    '6' : ['निखर्व'],
    '7' : ['महापद्म'],
    '8' : ['शङ्ख'],
    '9' : ['जलधि'],
    '10' : ['अन्त्य'],
    '11' : ['मध्य'],
    '12' : ['परार्ध']
}


PREFIX_REPLACEMENTS = {
    'एकं': {
        ('अ', 'द'): 'एका',
        ('अ', 'द', 'ख', 'म', 'ज', 'च', 'प', 'ष', 'स', 'न', 'ल', 'श', 'वि', 'को', 'त्रि'): 'एक',
        ('उ'): 'एको'
    },
    'द्वे': {
        ('अ'): 'द्व्य',
        ('वि', 'त्रि', 'द'): 'एक',
        ('च', 'प', 'ष', 'स', 'न', 'श', 'ल', 'को', 'ख', 'ज', 'म'): 'द्वि',
        ('उ'): 'द्व्यु'
    },
    'त्रीणि': {
        ('अ'): 'त्र्य',
        ('वि', 'द'): 'त्र्ययो',
        ('त्रि'): 'त्रयस्',
        ('च', 'प', 'ष', 'स', 'न', 'श', 'ल', 'को', 'ख', 'ज', 'म'): 'त्रि',
        ('उ'): 'त्र्यु'
    },
    'चत्वारि': {
        ('अ'): 'चतुर',
        ('द', 'वि', 'न', 'ल', 'ज', 'म'): 'चतुर्',
        ('त्रि', 'स'): 'चतुस्',
        ('प'): 'चतुः',
        ('च', 'ष', 'को', 'ख'): 'चतुष्',
        ('श'): 'चतुश्',
        ('स'): 'चतुस्',
        ('उ'): 'चतुरु'
    },
    'पञ्च': {
        ('अ'): 'पञ्चा',
        ('उ'): 'पञ्चो'
    },
    'षट्': {
        ('द'): 'षोड',
        ('वि','त्रि','च','प','ष','स','न','श','को','ख', 'ज', 'म'): 'षड्',
        ('अ'): 'षड',
        ('उ'): 'षडु'
    },
    'सप्त': {
        ('अ'): 'सप्ता',
        ('उ'): 'सप्तो'
    },
    'अष्ट': {
        ('अ'): 'अष्टा',
        ('द', 'वि', 'त्रि'): 'अष्टा',
        ('उ'): 'अष्टो'
    },
    'नव': {
        ('अ'): 'नवा',
        ('उ'): 'नवो'
    },
    'तिः': {
        ('अ'): 'त्य',
        ('उ'): 'त्यु',
        ('श', 'स', 'ल', 'को', 'ख', 'ज', 'म'): 'ति'
    },
    'त्': {
        ('अ'): 'द',
        ('उ'): 'दु'
    },
    'श': {
        ('अ'): 'शा',
        ('उ'): 'शो'
    },
    'ष्टिः': {
        ('अ'): 'ष्ट्य',
        ('श', 'स', 'ल', 'को', 'ख', 'ज', 'म'): 'ष्टि',
        ('उ'): 'ष्ट्यु'
    },
    'शतम्': {
        ('अ'): 'शता',
        ('उ'): 'शतो'
    },
    'लक्षम्': {
        ('अ'): 'लक्षा',
        ('उ'): 'लक्षो'
    },
    'सहस्रम्': {
        ('अ'): 'सहस्रा',
        ('उ'): 'सहस्रो'
    },
    'कोटि': {
        ('अ'): 'कोट्य',
        ('उ'): 'कोट्यु'
    }
}

VARIATIONS_DICT = {
    '0': ['पूज्यं'],
    '19': ['एकोनविंशतिः'],
    '29': ['एकोनत्रिंशत्'],
    '39': ['एकोनचत्वारिंशत्'],
    '49': ['एकोनपञ्चाशत्'],
    '59': ['एकोनषष्टिः'],
    '69': ['एकोनसप्ततिः'],
    '79': ['एकोनअशीतिः'],
    '89': ['एकोननवतिः'],
    '99': ['एकोनशतम्']
}



