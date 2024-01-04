Dic = {
    'a': 'あ',
    'i': 'い',
    'u': 'う',
    'e': 'え',
    'o': 'お',
    'ka': 'か',
    'ki': 'き',
    'ku': 'く',
    'ke': 'け',
    'ko': 'こ',
    'ga': 'が',
    'gi': 'ぎ',
    'gu': 'ぐ',
    'ge': 'げ',
    'go': 'ご',
    'sa': 'さ',
    'shi': 'し',
    'su': 'す',
    'se': 'せ',
    'so': 'そ',
    'zu': 'ず',
    'ji': 'じ',
    'ta': 'た',
    'cha': 'ちゃ',
    'chi': 'ち',
    'tsu': 'つ',
    'te': 'て',
    'to': 'と',
    'da': 'だ',
    'dji': 'ぢ',
    'de': 'で',
    'do': 'ど',
    'na': 'な',
    'ni': 'に',
    'nu': 'ぬ',
    'ne': 'ね',
    'no': 'の',
    'ha': 'は',
    'hi': 'ひ',
    'fi': 'ふぃ',
    'fu': 'ふ',
    'he': 'へ',
    'ho': 'ほ',
    'ba': 'ば',
    'bi': 'び',
    'bu': 'ぶ',
    'be': 'べ',
    'bo': 'ぼ',
    'pa': 'ぱ',
    'pi': 'ぴ',
    'ma': 'ま',
    'mi': 'み',
    'mu': 'む',
    'me': 'め',
    'mo': 'も',
    'ya': 'や',
    'yu ': 'ゆ',
    'yo': 'よ',
    'wa': 'わ',
    'wo': 'を',
    'ra': 'ら',
    'ri': 'り',
    'ru': 'る',
    're': 'れ',
    'ro': 'ろ',
    'n': 'ん'
}

Foreign_Name = {
    "kurt-": "kato-",
    "ck-": "shikei-"
}

letters = ["c", "k", "j", "g", "s", "t", "d", "n", "h", "b", "p", "f", "m", "y", "r", 'w', "z", "-"]
Vowels = ['a', 'i', 'u', 'e', 'o']


def hiragana(letter, n):
    Vowels = ['a', 'i', 'u', 'e', 'o']
    k = letter
    try:
        z = n[n.index(letter) + 1]
        zz = n[n.index(letter) + 2]
        if z in Vowels:
            k += z
            k = Dic.get(k, '')
            return k
        elif k == z and zz in Vowels and k != 'n':
            return 'っ'
        elif k == z and zz in Vowels and k == 'n':
            return 'ん'
        elif k == 't' or 'c' or 's' and z not in Vowels and zz in Vowels:
            word = k + z + zz
            return Dic.get(word, '')
        else:
            k = Dic.get(k, '')
            return k
    except:
        try:
            z = n[n.index(letter) + 1]
            if z in Vowels:
                k += z
                k = Dic.get(k, '')
                return k
            else:
                k = Dic.get(k, '')
                return k
        except:
            k = Dic.get(k, '')
            return k


def conditions_in_words(words, letter, index, prefix):
    back_index = index - 1
    front_index = index + 1
    try:
        if words[index] == "-":
            return prefix
        elif words[back_index] not in Vowels and words[index] in Vowels:
            return ''
        elif (words[back_index] != "n" and words[back_index] not in Vowels) and words[index] not in Vowels and words[
            front_index] in Vowels:
            return ''
        elif words[index] not in Vowels and words[front_index] not in Vowels and words[front_index + 1] in Vowels:
            word = words[index] + words[front_index] + words[front_index + 1]
            if word in Dic:
                return Dic.get(word, '')
        elif words[back_index] == words[index] and words[front_index] in Vowels:
            word = words[index] + words[front_index]
            return Dic.get(word, '')
        elif words[0] == words[index] and words[front_index] in Vowels and len(words) > front_index:
            word = words[index] + words[front_index]
            return Dic.get(word, '')
        elif words[2] == words[index] and ((len(words) - 1) > front_index and words[front_index] in Vowels):
            word = words[index] + words[front_index]
            return Dic.get(word, '')
        elif letter in Vowels:
            return Dic.get(letter, '')
        else:
            if letter in letters:
                if letter == 'n':
                    if len(words) != front_index or words[front_index] in Vowels:
                        return hiragana('n', words)
                    else:
                        return 'ん'
                elif letter == '-':
                    return prefix
                else:
                    return hiragana(letter, words)
    except:
        return ""


def add_prefix(word):
    if '-kun' in word:
        word = word.replace('kun', '')
        return word, '-くん'
    elif '-chan' in word:
        word = word.replace('chan', '')
        return word, '-ちゃん'
    elif '-san' in word:
        word = word.replace('san', '')
        return word, '-さん'
    elif '-sama' in word:
        word = word.replace('sama', '')
        return word, '-さま'
    elif '-dono' in word:
        word = word.replace('dono', '')
        return word, '-どの'
    return False


def hiragana_converter(word_input):
    final, wa, ga, o, prefix = '', '', '', '', ''
    Wordz = word_input.split()
    for n, x in enumerate(Wordz):  # checks duplicate words
        if Wordz[0] == Wordz[n] and n != 0:
            Wordz[n] += 's'
    for word in Wordz:
        if word_and_prefix := add_prefix(word):
            word, prefix = word_and_prefix
        elif word == 'wa':
            final += ' は'
        elif word == 'o':
            final += ' を'
        elif word == 'ga':
            final += ' が'
        if word in Foreign_Name:
            word = Foreign_Name[word]
        if word != 'wa' and word != 'o' and word != 'ga':
            for i, letter in enumerate(word):
                if i == 0:
                    if word != Wordz[0] and not word_and_prefix:
                        final += ' '
                    if word_and_prefix and final:
                        final += ' '
                    if letter in Vowels:
                        final += Dic.get(letter, '')
                    else:
                        if letter in letters:
                            final += hiragana(letter, word)
                if i == 1:
                    if word[0] not in Vowels:
                        final += ''
                    elif word[0] not in Vowels and word[1] not in Vowels and word[2] in Vowels:
                        final += ''
                    else:
                        if letter in Vowels:
                            final += Dic.get(letter, '')
                        else:
                            if letter in letters:
                                final += hiragana(letter, word)

                if i == 2:
                    if word[1] not in Vowels:
                        final += ''
                    elif word[1] not in Vowels and word[2] not in Vowels and word[3] in Vowels:
                        final += ''
                    else:
                        if letter in Vowels:
                            final += Dic.get(letter, '')
                        else:
                            if letter in letters:
                                if letter == 'n':
                                    try:
                                        if word[3] not in Vowels and word[3] != 'n':
                                            final += 'ん'
                                        else:
                                            final += hiragana('n', word)
                                    except:
                                        final += 'ん'
                                else:
                                    final += hiragana(letter, word)
                if i == 3:
                    final += conditions_in_words(word, letter, i, prefix)

                if i == 4:
                    final += conditions_in_words(word, letter, i, prefix)

                if i == 5:
                    final += conditions_in_words(word, letter, i, prefix)

                if i == 6:
                    final += conditions_in_words(word, letter, i, prefix)

                if i == 7:
                    final += conditions_in_words(word, letter, i, prefix)

                if i == 8:
                    final += conditions_in_words(word, letter, i, prefix)

                if i == 9:
                    final += conditions_in_words(word, letter, i, prefix)

    return final


if __name__ == '__main__':
    print(hiragana_converter("ore wa kurt-kun ga suki"))
