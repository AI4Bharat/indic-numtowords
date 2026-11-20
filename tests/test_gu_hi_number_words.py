from indic_numtowords import num2words
from indic_numtowords.guj.cardinal import convert as gu_convert
from indic_numtowords.guj.data.nums import direct_dict as gu_direct, variations_dict as gu_variations
from indic_numtowords.hin.data.nums import variations_dict as hi_variations


def _in_block(text, start, end):
    return all(start <= ord(ch) <= end for ch in text if not ch.isspace())


def test_hindi_sava_spelling():
    # 125, 225 ... 925 were spelled "सावा"; the word is "सवा"
    assert "सवा सौ" in num2words(125, lang="hi", variations=True)
    assert not any("सावा" in v for vs in hi_variations.values() for v in vs)


def test_gujarati_table_is_gujarati_script():
    # 10000000 was stored as Gurmukhi "ਕਰੋੜ"
    assert gu_direct["10000000"] == ["કરોડ"]
    for words in gu_direct.values():
        for w in words:
            assert _in_block(w, 0x0A80, 0x0AFF), w
    for words in gu_variations.values():
        for w in words:
            assert _in_block(w, 0x0A80, 0x0AFF), w


def test_gujarati_variations():
    assert "દોઢસો" in num2words(150, lang="gu", variations=True)
    assert "અઢીસો" in num2words(250, lang="gu", variations=True)
    assert "સવાસો" in num2words(125, lang="gu", variations=True)
    assert "સાડા ત્રણ સો" in num2words(350, lang="gu", variations=True)
    assert "પોણા બસો" in num2words(175, lang="gu", variations=True)
    # inside a larger number, like Hindi ("एक हज़ार डेढ़ सौ")
    assert "એક હજાર દોઢસો" in gu_convert(1150)


def test_gujarati_joined_hundreds():
    # written Gujarati joins the hundreds ("એકસો", "ત્રણસો"); offered alongside the spaced default
    assert "એકસો પચ્ચીસ" in num2words(125, lang="gu", variations=True)
    assert "એકસો પચાસ" in num2words(150, lang="gu", variations=True)
    assert "ત્રણસો પચાસ" in num2words(350, lang="gu", variations=True)
    assert "સાડા ત્રણસો" in num2words(350, lang="gu", variations=True)
    assert "એક હજાર એકસો પચાસ" in num2words(1150, lang="gu", variations=True)
    assert {"એક સો", "એકસો", "સો"} <= set(num2words(100, lang="gu", variations=True))


def test_gujarati_default_output_unchanged():
    # variations only add alternatives; the first (default) reading stays the plain cardinal
    assert num2words(150, lang="gu") == "એક સો પચાસ"
    assert num2words(250, lang="gu") == "બસો પચાસ"
    assert num2words(1150, lang="gu") == "એક હજાર એક સો પચાસ"
    assert num2words(10000000, lang="gu") == "એક કરોડ"
    assert num2words(45, lang="gu") == "પિસ્તાલીસ"
