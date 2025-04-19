import sqlite3
from contextlib import closing

DB_FILE = 'lights.db'
DEFAULT_LIGHTS = ['green', 'orange', 'red']


def connect():
    """Get a new connection to the database."""
    return sqlite3.connect(DB_FILE)


def setup_database():
    """Initializes the database and sets default states for lights."""
    with closing(connect()) as conn:
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS light_state (
                    name TEXT PRIMARY KEY,
                    state INTEGER NOT NULL CHECK (state IN (0, 1))
                )
            ''')

            # Insert default lights with state=0 if they do not exist
            for light in DEFAULT_LIGHTS:
                conn.execute('''
                    INSERT OR IGNORE INTO light_state (name, state)
                    VALUES (?, 0)
                ''', (light,))


def ensure_database():
    """Ensures the DB is initialized. Safe to call multiple times."""
    setup_database()


def set_light_state(name, state):
    ensure_database()
    with closing(connect()) as conn:
        with conn:
            conn.execute('''
                INSERT INTO light_state (name, state)
                VALUES (?, ?)
                ON CONFLICT(name) DO UPDATE SET state = excluded.state
            ''', (name, state))


def get_light_state(name):
    ensure_database()
    with closing(connect()) as conn:
        cur = conn.cursor()
        cur.execute('SELECT state FROM light_state WHERE name = ?', (name,))
        row = cur.fetchone()
        return row[0] if row else 0


def get_all_states():
    ensure_database()
    with closing(connect()) as conn:
        cur = conn.cursor()
        cur.execute('SELECT name, state FROM light_state')
        return dict(cur.fetchall())
