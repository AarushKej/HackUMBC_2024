from pynput.keyboard import Key, Listener

# Function to handle when a key is pressed
def on_press(key):
    try:
        print(f"Key {key.char} pressed")  # Print regular keys
    except AttributeError:
        print(f"Special key {key} pressed")  # Print special keys

# Function to handle when a key is released
def on_release(key):
    print(f"Key {key} released")
    if key == Key.esc:
        # Stop the listener when 'Esc' is pressed
        print("Esc pressed. Exiting...")
        return False  # Returning False stops the listener

# Start listening to the keyboard
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()