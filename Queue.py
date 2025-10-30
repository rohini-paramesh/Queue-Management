from collections import deque
import time

class QueueSimulation:
    def __init__(self, num_counters=2):
        self.regular_queue = deque()
        self.priority_queue = deque()
        self.counters = {f"Counter-{i+1}": None for i in range(num_counters)}
        self.customer_id = 1
        self.customer_times = {}

    def add_customer(self, priority=False):
        customer = f"Customer-{self.customer_id}"
        self.customer_id += 1
        if priority:
            self.priority_queue.append(customer)
        else:
            self.regular_queue.append(customer)
        self.customer_times[customer] = time.time()
        queue_type = "Priority" if priority else "Regular"
        print(f"{customer} has joined the {queue_type} queue.")

    def serve_customer(self):
        for counter, customer in self.counters.items():
            if customer is None:
                # Serve from priority queue first, then regular queue
                if self.priority_queue:
                    next_customer = self.priority_queue.popleft()
                elif self.regular_queue:
                    next_customer = self.regular_queue.popleft()
                else:
                    print("No customers in the queue!")
                    return

                self.counters[counter] = next_customer
                wait_time = time.time() - self.customer_times.pop(next_customer, time.time())
                print(f"{next_customer} is being served at {counter}. (Waited {wait_time:.2f} seconds)")
                return

        print("All counters are busy! Please wait.")

    def complete_service(self, counter):
        if self.counters[counter]:
            print(f"{self.counters[counter]} has completed service at {counter}.")
            self.counters[counter] = None
        else:
            print(f"{counter} is already free.")

    def display_queue(self):
        priority = " -> ".join(self.priority_queue) if self.priority_queue else "Empty"
        regular = " -> ".join(self.regular_queue) if self.regular_queue else "Empty"
        print(f"Priority Queue: {priority}")
        print(f"Regular Queue: {regular}")

    def display_counters(self):
        for counter, customer in self.counters.items():
            status = customer if customer else "Free"
            print(f"{counter}: {status}")

    def run_simulation(self):
        print("Welcome to the Queue Simulation System!")
        print("1. Add Regular Customer\n2. Add Priority Customer\n3. Serve Customer")
        print("4. Complete Service at Counter\n5. Display Queue\n6. Display Counters\n7. Exit")
        
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    self.add_customer(priority=False)
                elif choice == 2:
                    self.add_customer(priority=True)
                elif choice == 3:
                    self.serve_customer()
                elif choice == 4:
                    counter = input("Enter the counter name (e.g., Counter-1): ")
                    self.complete_service(counter)
                elif choice == 5:
                    self.display_queue()
                elif choice == 6:
                    self.display_counters()
                elif choice == 7:
                    print("Exiting the simulation. Goodbye!")
                    break
                else:
                    print("Invalid choice! Please choose a vcalid Option")
            except ValueError:
                print("Please enter a valid number.")

if __name__ == "__main__":
    simulation = QueueSimulation(num_counters=3)
    simulation.run_simulation()
