from pathlib import Path
import os

class ProblemDB:
    def __init__(self,**kwargs):
        try:
            self.ignore_db_path = os.path.join(kwargs['base'],".ignore.db")
        except:
            raise Exception
        Path(self.ignore_db_path).touch()
        self.db = []
        self.db_links = {}
        with open(self.ignore_db_path, 'r') as database:
            self.ignore_db = database.readlines()
    
    def __len__(self):
        return len(self.db)
    
    def __str__(self):
        return "".join(self.db)
    
    def __getitem__(self,i):
        return self.db[i]

    def add(self,title:str,item:str) -> bool:
        self.db.append(title)
        self.db_links[title] = f"{item}\n"
        return True

    def ignore_write(self,_title,href:str):
        try:
            with open(self.ignore_db_path, 'a') as database:
                database.write(href+"\n")
            return True
        except Exception as _e:
            raise

    def ignore(self,title:str) -> bool:
        try:
            if self.ignore_write("title",self.db_links[title]):
                self.db.pop(self.db.index(title))
                self.db_links.pop(title)
            return True
        except Exception as _e:
            raise

    def is_ignored(self,item: str) -> bool:
        if item + "\n" in self.ignore_db:
            return True
        return False