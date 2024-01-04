names = {
    "kurt": ("kurt", "M"),
    "ck": ("ck", "M"),
    "kuriko": ("kuriko", "F")
}

eng_jap_dict = {
    'noun': {
        "i": "ore",
        "you": "kimi",
        "him": "kare",
    },

    'verb': {
        "eat": "taberu",
        "ate": "tabeta",
        "ran": "hashitta",
        "drank": "nonda",
        "met": "atta",
        "meet": "airu",
        "open": "akeru",
        "opened": "aketa",
        "played": "asonda",
        "washed": "aratta",
        "insert": "ireru",
        "inserted": "ireta"

    },

    'feelings': {
        "love": "daisuki",
        "hate": "daikirai",
        "like": "suki",
        "dislike": "kirai"
    },

    'food': {
        "apple": "ringo",
        "water": "mizu",
        "breakfast": "asa gohan",
        "drink": "nomimono"
    },

    'numbering': {
        "one": "hitotsu",
        "two": "futatsu",
        "three": "mittsu",
    },

    'thing': {
        "pencil": "enpitsu",
        "box": "hako",
        "smartphone": "sumaho",
        "phone": "denwa",
        "rainbow": "niji",
        "glasses": "megane",
        "bag": "kaban",
        "stair": "kaidan",
        "pillow": "makura",
    },

    'greeting': {
        "hi": "konnichiwa",
        "hello": "konnichiwa"
    },

    'color': {
        "red": "akai",
        "yellow": "kiiroi",
        "blue": "aoi",
        "pink": "pinku",
        "orange": "orenji",
        "green": "midori",
        "brown": "chairoi",
        "black": "kuroi",
        "white": "shiroi",
        "color": "iro"
    },

    'adjective': {
        "bright": "akarui",
        "new": "atarashii",
        "warm": "atatakai",
        "hot": "atsui",
        "cool": "suzushii",
        "cold": "samui",
        "thick": "atsui",
        "various": "iroiro"
    },

    'season': {
        "fall": "aki",
        "autumn": "aki",
        "summer": "natsu",
    },

    'time': {
        "morning": "asa",
        "tommorow": "ashita",
    },

    'body': {
        "leg": "ashi",
        "foot": "ashi",
        "head": "atama",
        "face": "kao",
        "back": "senaka",
        "stomach": "onaka",
    },

    'pronoun': {
        "this": "kore",
        "that": "sono",
    },

    'questions': {
        "why": "nande",
        "what": "nani",
    }

}

fil_jap_dict = {
    'noun': {
        "ako": "ore",
        "ako'y": "ore",
        "'ko": "ore",
        "ikaw": "kimi",
        "kita": "kimi",
        "kami": "oretachi",
    },

    'verb': {
        "kumain": "tabeta",
        "uminom": "nonda",
        "kain": "taberu",
        "tinuro": "oshita",
    },

    'feelings': {
        "mahal": "daisuki",
        "gusto": "suki",
        "ayaw": "daikirai"
    },

    'food': {
        "mansanas": "ringo",
        "tubig": "mizu",
    },

    'numbering': {
        "isang": "hitotsu",
        "dalawang": "futatsu",
        "tatlong": "mittsu",
    },

    'thing': {
        "lapis": "enpitsu",
        "kahon": "hako",
        "selpon": "sumaho",
        "telepono": "denwa",
        "salamin": "megane"
    },

    'greeting': {
        "kamusta": "konnichiwa",
    },

    'color': {
        "dilaw": "kiiroi"
    },

    'adjective': {
        "mabigat": "omoi"
    },

    'season': {
        "maulan": "ame"
    },

    'time': {
        "umaga": "asa"
    },

    'body': {
        "kamay": "te"
    },

    'pronoun': {
        "ito": "kore",
        "ayan": "sore",
    },

    'questions': {
        "bakit": "nande",
        "ano": "nani",
    },

}

jap_fil_dict = {}
for (key, value) in fil_jap_dict.items():
    temp_dict = {value2: key1 for (key1, value2) in value.items()}
    jap_fil_dict[key] = temp_dict

jap_fil_dict["noun"]["anata"] = "ikaw"

eng_fil_dict = {
    'noun': {
        "i": "ako",
        "you": "ikaw",
    },

    'verb': {
        "eat": "kumain",
        "ate": "kumain",
        "ran": "tumakbo",
        "drank": "iminom"
    },

    'feelings': {
        "love": "mahal",
        "hate": "galit",
    },

    'food': {
        "apple": "mansanas",
        "water": "tubig",

    },

    'numbering': {
        "one": "isang",
        "two": "dalawang",
        "three": "tatlong",
    },

    'thing': {
        "pencil": "lapis",
        "box": "kahon",
        "smartphone": "selpon",
        "phone": "selpon",
        "rainbow": "bahaghari",
        "glasses": "salamin",
        "bag": "bag",
    },

    'greeting': {
        "hi": "kamusta",
        "hello": "kamusta"
    },

    'color': {
        "yellow": "dilaw",
        "red": "pula",
    },

    'adjective': {
        "heavy": "mabigat",
    },

    'season': {
        "rainy": "maulan",
    },

    'time': {
        "morning": "umaga",
    },

    'body': {
        "hands": "kamay",
    },

    'pronoun': {
        "this": "ito",
        "that": "ayan",
    },

    'questions': {
        "why": "bakit",
        "what": "ano",
    },

}

fil_eng_dict = {}
for (key, value) in eng_fil_dict.items():
    temp_dict = {value2: key1 for (key1, value2) in value.items()}
    fil_eng_dict[key] = temp_dict

jap_eng_dict = {}
for (key, value) in eng_jap_dict.items():
    temp_dict = {value2: key1 for (key1, value2) in value.items()}
    jap_eng_dict[key] = temp_dict

jap_eng_dict["noun"]["anata"] = "you"

if __name__ == "__main__":
    print(fil_eng_dict)
    print(jap_eng_dict)
