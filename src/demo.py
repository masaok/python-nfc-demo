import time
# from acr122u.reader import ACR122UReader
import nfc

def main():
    # reader = ACR122UReader()  # Initialize the reader
    
    # if not reader.connection:
    #     print("Unable to connect to the reader. Ensure it's connected properly.")
    #     return
    
    # print("Waiting for a card...")

    while True:

        try:

            reader = nfc.Reader()
            card_data = reader.get_uid()
        
            if card_data:
                print(f"Card detected: {card_data}")
                reader.print_data(card_data)
        
        except:
            print("Unable to connect to the reader. Ensure it's connected properly.")

        time.sleep(2.5)  # Sleep for 0.5 seconds to prevent too frequent polling

if __name__ == '__main__':
    main()
