from derpibooru import Search, sort
import random

ARTISTS = ["lightisanasshole", "coco-drillo", "dyonys", "quint-t-w", "ginnythequeen"]

def template(artist: str, upvotes: int):
    for image in Search().query(f"artist:{artist}, upvotes.lte:600, upvotes.gte:{upvotes}").sort_by(sort.RANDOM).limit(1):
        return image.url

class Commands:

    @classmethod
    def light(cls, upvotes: int):
        return template(ARTISTS[0], upvotes=upvotes)

    @classmethod
    def coco(cls, upvotes=5):
        return template(ARTISTS[1], upvotes=upvotes)

    @classmethod
    def dyo(cls, upvotes: int):
        return template(ARTISTS[2], upvotes=upvotes)

    @classmethod
    def quint(cls, upvotes=5):
        return template(ARTISTS[3], upvotes=upvotes)

    @classmethod
    def ginny(cls, upvotes=5):
        return template(ARTISTS[4], upvotes=upvotes)

class Random:

    def randomimage(self, upvotes: int):
        for image in Search().query(f"safe, -screencap, upvotes.gte:{upvotes}").sort_by(sort.RANDOM).limit(1):
            return image.url

    def randomimageartistslist(self):
        for image in Search().query(f"artist:{random.choice(ARTISTS)}, upvotes.lte:600, upvotes.gte:10").sort_by(
                                                                                                sort.RANDOM).limit(1):
            return image.url

#Fixed by Tobyyy