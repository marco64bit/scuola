import random
import string
from pprint import pprint


def create_random_id():
    """
    return random string of 20 chars
    """
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))


class CacheManger():

    CACHE = {}

    def load_from_cache(self, id):
        return CacheManger.CACHE.get(id)
    
    def save_in_cache(self, id, data):
        CacheManger.CACHE[id] = data


class Tag(CacheManger):

    id = None
    tag_name = None

    def __init__(self, tag_name):
        self.id = create_random_id()
        self.tag_name = tag_name


class Appuntamento(CacheManger):

    id = None
    datec = None
    start = None
    end = None
    text = None
    tag = None

    def __init__(self, date, start, end, text, tag=None):
        self.id = create_random_id()
        self.date = date
        if start > end:
            raise Exception("Start must be < end")
        self.start = start
        self.end = end
        self.text = text
        self.tag = tag
        self.duration = self.end - self.start

    def _load():
        """load from file"""
        pass

    def get(self):
        cached = self.load_from_cache(self.id)
        if cached:
            print("LOADED FROM CACHE")
            return cached
        
        out = {
            "date": self.date,
            "start": self.start,
            "text": self.text,
            "duration": round(self.duration * 10) / 10,
        }
        if self.tag:
            out["tag_name"] = self.tag.tag_name
            
        self.save_in_cache(self.id, out)
        return out

    @staticmethod
    def list(search_string=None):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass


tag_salute = Tag(tag_name="salute")

appuntamento_1 = Appuntamento(date='22/03/2023',
                              start=11.0,
                              end=12.0,
                              text="Vai dal dentista",
                              tag=tag_salute)

appuntamento_2 = Appuntamento(date='21/03/2023',
                              start=12.0, 
                              end=18.30,
                              text="Corso di yoga")

## pprint serve solo per stampare più leggibile un json, va a capo se serve
pprint(appuntamento_1.get())
print("="*20)
pprint(appuntamento_2.get())
print("="*20)


# loaded from cache now
pprint(appuntamento_2.get())
print("="*20)


