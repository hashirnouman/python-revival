"""Custom contianer"""


class TagCloud:
    """tag cloud class"""

    def __init__(self):
        self.tags = {}

    def add(self, tag):
        """add new tag"""
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
# cloud.add('python')
# cloud['python'] = 10
# cloud.add('python')
# cloud.add('python')
# cloud.add('Python')
print(cloud.__dict__)
# print(len(cloud))
# in python there not a concept of private members like other languges like c#
