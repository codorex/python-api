CLUBS = [
    { 
        'id': 1,
        'name': 'ASP.NET Fundamentals',
        'description': 'Roadmap for the basics of ASP.NET.'
    },
     { 
        'id': 2,
        'name': 'CSS3 Starter guide',
        'description': 'Roadmap for the basics of CSS3.'
    },
     { 
        'id': 3,
        'name': 'Learning to fly',
        'description': 'Roadmap for the basics of cloud development.'
    }
]

class CollectionWrapper():
    def __init__(self, collection):
        self.collection = collection

    def firstOrDefault(self, predicate):
        for item in self.collection:
            if predicate(item):
                return item
        return None

    def where(self, predicate):
        return [item for item in self.collection if predicate(item)]

    def max(self, predicate):
        largest = 0
        for item in self.collection:
            if predicate(item) > largest:
                largest = predicate(item)
        return largest + 1
        