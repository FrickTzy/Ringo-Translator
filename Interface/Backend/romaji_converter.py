import pykakasi


class RomajiConverter:
    hiragana_list = ["あ", "い", "う", "え", "お",
                     "か", "き", "く", "け", "こ",
                     "さ",
                     "は", "ひ", "ふ", "へ", "ほ",
                     "り"]
    common_romaji = {
        "konnichiha": "konnichiwa",
        "sayounara": "sayonara"
    }
    text = "愛している"

    def __init__(self):
        self.converter = pykakasi.Kakasi()

    def convert(self, japanese_text) -> str:
        final_romaji = ""
        for romaji in self.converter.convert(japanese_text):
            is_hiragana = self.hiragana_detector(romaji)
            if (temp_romaji := ("{} ".format(romaji['hepburn'].lower()))) and is_hiragana:
                temp_romaji = self.convert_common_romaji(temp_romaji)
                final_romaji += self.word_fixer(temp_romaji)
            else:
                final_romaji += temp_romaji
        return final_romaji.strip()

    def hiragana_detector(self, romaji_list) -> bool:
        if "{}".format(romaji_list['orig'].lower()[0]) in self.hiragana_list:
            return True
        return False

    def convert_common_romaji(self, word) -> str:
        return self.common_romaji.get(word.strip(), word)

    @staticmethod
    def word_fixer(romaji) -> str:
        romaji = romaji.strip()
        romaji_word = ""
        suffix_wo = ""
        prefix_wa = ""
        if romaji.startswith("ha"):
            prefix_wa += "wa "
            romaji = romaji.removeprefix('ha')
        if romaji.endswith("wo"):
            romaji = romaji.removesuffix("wo")
            suffix_wo = " o "
        romaji_word += f"{prefix_wa}{romaji}{suffix_wo}"

        return romaji_word


if __name__ == "__main__":
    converter = RomajiConverter()
    print(converter.convert("こんにちは"))
