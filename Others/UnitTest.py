import unittest
from Stuff.NihongoTranslator.Translate_Class.Translators.translator import Translate
from Stuff.NihongoTranslator.Translate_Class.Translators.Others.errors import *


class TestTranslate(unittest.TestCase):

    def test_jap(self):
        result = Translate.jap("i ate an apple", "eng")
        self.assertEqual(result, "Ore wa Ringo o Tabeta \nおれ は りんご を たべた")

        result = Translate.jap("uminom ako ng tubig")
        self.assertEqual(result, "Ore wa Mizu o Nonda \nおれ は みず を のんだ")

        result = Translate.jap("i ate two apple")
        self.assertEqual(result, "Ore wa Futatsu no Ringo o Tabeta \nおれ は ふたつ の りんご を たべた")

        result = Translate.jap("i ate two apples")
        self.assertEqual(result, "Ore wa Futatsu no Ringo o Tabeta \nおれ は ふたつ の りんご を たべた")

        result = Translate.jap("i ate two yellow apples")
        self.assertEqual(result, "Ore wa Futatsu no Kiiroi Ringo o Tabeta \nおれ は ふたつ の きいろい りんご を たべた")

        result = Translate.fil("i ate two apples")
        self.assertEqual(result, "Kumain Ako ng Dalawang Mansanas ")

        result = Translate.jap("i love you")
        self.assertEqual(result, "Ore wa Kimi ga Daisuki \nおれ は きみ が だいすき")

        result = Translate.jap("i love kurt")
        self.assertEqual(result, "Ore wa Kurt-kun ga Daisuki \nおれ は かと-くん が だいすき")

        result = Translate.jap("kurt ate two red apples")
        self.assertEqual(result, "Kurt-kun wa Futatsu no Akai Ringo o Tabeta \nかと-くん は ふたつ の あかい りんご を たべた")

        result = Translate.eng("ore wa nomimono o nonda")
        self.assertEqual(result, "I Drank a Drink ")

        result = Translate.eng("ore wa ringo o tabeta")
        self.assertEqual(result, "I Ate an Apple ")

        self.assertRaises(LanguageNotMatching, Translate.jap, 'kumain', language='eng')
        self.assertRaises(UnknownLanguageError, Translate.jap, 'kumain', language='idk')

        self.assertRaises(UnknownWordError, Translate.jap, "")
        self.assertRaises(SameLanguageError, Translate.jap, "ako", language='jap')


if __name__ == '__main__':
    unittest.main()
