from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Corpus:
    catagories: List[str]
    begin: str
    end: str
    chemin: Path
    articles: List[Article]

@dataclass
class Article:
    titre: str
    description: str


### script
from datastructures import *
a = Article("un titre", "du contenu")
c = Corpus(["sport"], "2023-04-05", "2023-04-05", "../Corpus/", [a])
