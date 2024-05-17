import threading

# Custom iterator to generate a sequence of numbers
class NumberGenerator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

# Function to process a number (simulating some work)
def process_number(number):
    try:
        if number < 0:
            raise ValueError(f"Negative number encountered: {number}")
        print(f"Processing number: {number}")
    except ValueError as e:
        print(f"Error: {e}")

# Worker function for threading
def worker(numbers):
    for number in numbers:
        process_number(number)

# Main function to setup and start threads
def main():
    # Create an iterator for numbers 1 to 10
    number_generator = NumberGenerator(1, 10)
    
    # Split the work into two threads
    thread1_numbers = []
    thread2_numbers = []
    
    try:
        for number in number_generator:
            if number % 2 == 0:
                thread1_numbers.append(number)
            else:
                thread2_numbers.append(number)
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    # Create threads
    thread1 = threading.Thread(target=worker, args=(thread1_numbers,))
    thread2 = threading.Thread(target=worker, args=(thread2_numbers,))
    
    # Start threads
    thread1.start()
    thread2.start()
    
    # Wait for threads to complete
    thread1.join()
    thread2.join()

    print("Processing complete.")

if __name__ == "__main__":
    main()
