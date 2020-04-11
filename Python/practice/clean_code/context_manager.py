
import contextlib

def stop_database():
    print("systemctl stop postgresql.service")
def start_database():
    print("systemctl start postgresql.service")

class DBHandler:
    def __enter__(self):
        stop_database()
        return self
    def __exit__(self, exc_type, ex_value, ex_traceback):
        start_database()

def db_backup():
    print("pg_dump database")
def main():
    with DBHandler():
        db_backup()

if __name__=='__main__':
    @contextlib.contextmanager
    def db_handler():
        stop_database()
        yield
        start_database()

    with db_handler():
        db_backup()