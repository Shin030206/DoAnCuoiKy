class Category:
    def __init__(self,cateid,catename):
        self.cateid=cateid
        self.catename=catename
    def __str__(self):
        return f'{self.cateid}\t{self.catename}'