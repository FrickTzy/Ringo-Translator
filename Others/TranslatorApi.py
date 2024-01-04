from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
from Stuff.NihongoTranslator.Translate_Class.Translators.Others import dictionary

api = FastAPI()


class Category(BaseModel):
    words: dict = {}


all_dict: dict = {"eng-to-jap": dictionary.eng_jap_dict,
                  "eng-to-fil": dictionary.eng_fil_dict, }


@api.get("/")
def home():
    return "Home"


@api.get("/get-words/{language}/{word_type}")
def get_words(language: str = Path(description="The language you want to acquire"),
              word_type: str = Path(description="The language you want to acquire")):
    if language in all_dict:
        if word_type in all_dict[language]:
            return all_dict[language][word_type]

        return all_dict[language]


@api.get("/get-words/{language}")
def get_language(language: str = Path(description="The language you want to acquire")):
    if language in all_dict:
        return all_dict[language]
    return {"data": "not found"}


@api.get("/get-words")
def get_words(language: str, word_type: Optional[str] = ""):
    if language in all_dict:
        if word_type in all_dict[language]:
            return all_dict[language][word_type]
        return all_dict[language]
    return {"data": "not found"}


@api.post("/make-category/{language}/{name}")
def make_category(*, language: str = Path(description="The language you want to acquire"),
                  name: str = Path(description="The name of the new category"),
                  category: Category):
    if language in all_dict:
        if name in all_dict[language]:
            return {"data": "already there"}
        else:
            all_dict[language][name] = category.words
            return all_dict[language][name]
    return {"data": "not found"}


@api.patch("/change-category/{language}/{name}")
def change_category(*, language: str = Path(description="The language you want to acquire"),
                    name: str = Path(description="The name of the category you want to change"),
                    category: Category):
    if language in all_dict:
        if name in all_dict[language]:
            all_dict[language][name] = category.words
            return all_dict[language][name]
    return {"data": "not found"}


@api.patch("/update-category/{language}/{name}")
def update_category(*, language: str = Path(description="The language you want to acquire"),
                    name: str = Path(description="The name of the category you want to change"),
                    category: Category):
    if language in all_dict:
        if name in all_dict[language]:
            for (key, item) in category.words.items():
                all_dict[language][name][key] = item
            return all_dict[language][name]
    return {"data": "not found"}
