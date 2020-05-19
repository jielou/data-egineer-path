import concurrent.futures
import time
import threading

class Account:
    def __init__(self):
        self.balance = 100 # shared data
        self.lock = threading.Lock()

    def update(self, transaction, amount):
        print(f"{transaction} thread updating...")
        # add lock
        with self.lock:
            local_copy = self.balance+ amount
            time.sleep(1)
            self.balance = local_copy
        # release lock    
        print(f"{transaction} thread finishing...")

if __name__ == "__main__":
    account = Account()
    print(f"starting with balanced of {account.balance}")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        for transaction, amount in [("deposit", 50), ("withdrawal", -150)]:
            ex.submit(account.update, transaction, amount)
    print(f"ending balanced of {account.balance}")

    
