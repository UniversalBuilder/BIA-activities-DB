import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_projects_table()

    def create_projects_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        """)
        self.conn.commit()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        """)
    
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                project_id INTEGER,
                FOREIGN KEY(project_id) REFERENCES projects(id)
            )
        """)
    
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS logbook_entries (
                id INTEGER PRIMARY KEY,
                details TEXT NOT NULL,
                project_id INTEGER,
                FOREIGN KEY(project_id) REFERENCES projects(id)
            )
        """)
        self.conn.commit() 

    def add_project(self, project):
        self.cursor.execute("""
            INSERT INTO projects (name, description) VALUES (?, ?)
        """, (project.name, project.description))
        self.conn.commit()
    
    def get_projects(self):
        self.cursor.execute("""
            SELECT * FROM projects
        """)
        return self.cursor.fetchall()
    
    def update_project(self, project):
        self.cursor.execute("""
            UPDATE projects SET name = ?, description = ? WHERE id = ?
        """, (project.name, project.description, project.id))
        self.conn.commit()
    
    def delete_project(self, project_id):
        self.cursor.execute("""
            DELETE FROM projects WHERE id = ?
        """, (project_id,))
        self.conn.commit()
        
    def close(self):
        self.conn.close()
        
    def insert_file(self, file):
        self.cursor.execute("""
            INSERT INTO files (name, project_id) VALUES (?, ?)
        """, (file.name, file.project_id))
        self.conn.commit()

    def get_files(self, project_id):
        self.cursor.execute("""
            SELECT * FROM files WHERE project_id = ?
        """, (project_id,))
        return self.cursor.fetchall()

    def update_file(self, file):
        self.cursor.execute("""
            UPDATE files SET name = ?, project_id = ? WHERE id = ?
        """, (file.name, file.project_id, file.id))
        self.conn.commit()

    def delete_file(self, file_id):
        self.cursor.execute("""
            DELETE FROM files WHERE id = ?
        """, (file_id,))
        self.conn.commit()

    def insert_logbook_entry(self, logbook_entry):
        self.cursor.execute("""
            INSERT INTO logbook_entries (details, project_id) VALUES (?, ?)
        """, (logbook_entry.details, logbook_entry.project_id))
        self.conn.commit()

    def get_logbook_entries(self, project_id):
        self.cursor.execute("""
            SELECT * FROM logbook_entries WHERE project_id = ?
        """, (project_id,))
        return self.cursor.fetchall()

    def update_logbook_entry(self, logbook_entry):
        self.cursor.execute("""
            UPDATE logbook_entries SET details = ?, project_id = ? WHERE id = ?
        """, (logbook_entry.details, logbook_entry.project_id, logbook_entry.id))
        self.conn.commit()

    def delete_logbook_entry(self, logbook_entry_id):
        self.cursor.execute("""
            DELETE FROM logbook_entries WHERE id = ?
        """, (logbook_entry_id,))
        self.conn.commit()
        
