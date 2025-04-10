import sqlite3

DB_NAME = "shortlisted.db"

def store_candidate_result(candidate_name, score, matched_role, invite_message):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shortlisted (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            candidate_name TEXT,
            score REAL,
            matched_role TEXT,
            invite_message TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO shortlisted (candidate_name, score, matched_role, invite_message)
        VALUES (?, ?, ?, ?)
    """, (candidate_name, score, matched_role, invite_message))

    conn.commit()
    conn.close()
    