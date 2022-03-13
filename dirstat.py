from sqlite3 import connect, OperationalError
from pathlib import Path

class SQLDatabase:
    def __init__(self, database:str|Path=":memory:"):
        self.database = database

    def __enter__(self):
        self.connection = connect(self.database)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, *args):
        self.connection.commit()
        self.connection.close()


def main(searchdir:Path, pattern:str, recurse:bool):
    with SQLDatabase() as cur:
        cur.execute("create table extensions (extension text, count int)")

        # Writing
        for path in (searchdir.absolute().rglob(pattern)
                     if recurse else
                     searchdir.glob(pattern)):
            res = cur.execute("select * from extensions where extension = ?", (path.suffix,)).fetchall()
            
            if res:
                ext, count = res[0]
                cur.execute("update extensions set count = ? where extension = ?", (count + 1, ext or path.name))

                continue
            
            cur.execute("insert into extensions values (?, 1)", (path.suffix or path.name,))

        # Reading
        for ext, count in cur.execute("select * from extensions order by count"):
            print(ext, count)

def verifyArgs(args) -> bool:
    return args.dir.is_dir()

if __name__ == "__main__":
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("dir", type=Path, help="Directory to search")
    parser.add_argument("-p", "--pattern", default="*", help="Glob pattern to use when searching 'dir'. '*' by default")
    parser.add_argument("-r", "--recursive", action="store_true", help="Makes the program go down folders. Off by default")

    args = parser.parse_args()

    if verifyArgs(args):
        main(args.dir, args.pattern, args.recursive)
