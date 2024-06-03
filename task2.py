from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Get image dimensions
    height, width, channels = image_array.shape
    
    # Apply a simple encryption operation: add key to pixel values
    encrypted_array = (image_array + key) % 256
    
    # Convert back to Image and save
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    # Convert image to numpy array
    image_array = np.array(image)
    
    # Apply the decryption operation: subtract key from pixel values
    decrypted_array = (image_array - key) % 256
    
    # Convert back to Image and save
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    while True:
        print("\nImage Encryption Tool:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")

        choice = input("Select an option (1, 2, or 3): ")

        if choice == '1':
            image_path = input("Enter the path to the image you want to encrypt: ")
            output_path = input("Enter the path to save the encrypted image: ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(image_path, output_path, key)
        elif choice == '2':
            image_path = input("Enter the path to the image you want to decrypt: ")
            output_path = input("Enter the path to save the decrypted image: ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(image_path, output_path, key)
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1, 2, or 3).")

if __name__ == "__main__":
    main()
