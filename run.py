import csv
import hashlib

class UserAuth:
    def __init__(self):
        self.users = {}

    def register(self, email: str, password: str) -> bool:
        if email in self.users:
            return False
        self.users[email] = hashlib.sha256(password.encode()).hexdigest()
        return True

    def reset_password(self, email: str) -> bool:
        # TODO: implement email sending
        return email in self.users

def process_csv(filepath: str) -> list:
    results = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                results.append(row)
            except Exception as e:
                print(f"Skipping invalid row: {e}")
    return results
