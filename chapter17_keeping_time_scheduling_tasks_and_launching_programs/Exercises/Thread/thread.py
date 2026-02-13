import threading
import time

# Main thread starts executing here
print("Started")

# Function that will run in a separate thread
def take_nap():
    # Pause execution for 5 seconds (simulating a long task)
    time.sleep(5)
    # This will be printed after the delay
    print("Wake up!")

# Create a new thread and assign the function to run
thread_obj = threading.Thread(target=take_nap)

# Start the new thread (it runs independently from the main thread)
thread_obj.start()

# Main thread continues without waiting for the new thread to finish
print("End of program")
