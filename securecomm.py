import subprocess
import os

# Function to clear the console screen
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# ASCII art banner
banner = """

  ___                   ____ ____  _     
 / _ \ _ __   ___ _ __ / ___/ ___|| |    
| | | | '_ \ / _ \ '_ \\___ \___ \| |    
| |_| | |_) |  __/ | | |___) |__) | |___ 
 \___/| .__/ \___|_| |_|____/____/|_____|
      |_|                                


"""

# Function to encrypt a file using AES-256
def encrypt_file(input_file, output_file):
    subprocess.run(['openssl', 'enc', '-aes-256-cbc', '-in', input_file, '-out', output_file])
    print("File encrypted successfully!")

# Function to decrypt a file using AES-256
def decrypt_file(input_file, output_file):
    subprocess.run(['openssl', 'enc', '-d', '-aes-256-cbc', '-in', input_file, '-out', output_file])
    print("File decrypted successfully!")

# Function to generate a self-signed certificate and CSR
def generate_certificates():
    subprocess.run(['openssl', 'req', '-x509', '-newkey', 'rsa:2048', '-keyout', 'key.pem', '-out', 'cert.pem', '-days', '365', '-subj', '/CN=localhost'])
    subprocess.run(['openssl', 'req', '-new', '-key', 'key.pem', '-out', 'csr.pem'])
    print("Certificates generated successfully!")

# Function to sign a CSR with a self-signed certificate
def sign_certificate():
    subprocess.run(['openssl', 'x509', '-req', '-in', 'csr.pem', '-signkey', 'key.pem', '-out', 'ca-cert.pem', '-days', '365'])
    print("CSR signed successfully!")

# Function to generate SHA-256 hash
def generate_sha256_hash(input_file):
    subprocess.run(['openssl', 'dgst', '-sha256', input_file])
    print("SHA-256 hash generated successfully!")

# Function to generate MD5 hash
def generate_md5_hash(input_file):
    subprocess.run(['openssl', 'dgst', '-md5', input_file])
    print("MD5 hash generated successfully!")

# Function to set up a TLS/SSL server
def setup_ssl_server():
    subprocess.run(['openssl', 's_server', '-cert', 'server-cert.pem', '-key', 'server-key.pem', '-accept', '4433'])
    print("TLS/SSL server set up successfully!")

# Function to establish TLS/SSL connection from client
def connect_ssl_client():
    subprocess.run(['openssl', 's_client', '-connect', 'localhost:4433', '-CAfile', 'ca-cert.pem'])
    print("TLS/SSL client connected successfully!")

# Function to set up a TLS/SSL client
def setup_ssl_client():
    subprocess.run(['openssl', 's_client', '-connect', 'localhost:4433', '-CAfile', 'ca-cert.pem'])

# Function to generate a digital signature
def generate_digital_signature(input_file):
    subprocess.run(['openssl', 'dgst', '-sha256', '-sign', 'private-key.pem', '-out', 'signature.sha256', input_file])
    print("Digital signature generated successfully!")

# Function to verify a digital signature
def verify_digital_signature(input_file):
    subprocess.run(['openssl', 'dgst', '-sha256', '-verify', 'public-key.pem', '-signature', 'signature.sha256', input_file])
    print("Digital signature verified successfully!")

# Function to create client key and certificate
def generate_client_certificate():
    subprocess.run(['openssl', 'req', '-newkey', 'rsa:2048', '-nodes', '-keyout', 'client-key.pem', '-out', 'client-req.pem', '-subj', '/CN=localhost'])
    subprocess.run(['openssl', 'x509', '-req', '-in', 'client-req.pem', '-CA', 'ca-cert.pem', '-CAkey', 'ca-key.pem', '-CAcreateserial', '-out', 'client-cert.pem', '-days', '365'])

# Main menu function
def main_menu():
    clear_screen()
    print(banner)
    print("1. Encrypt and Decrypt Files")
    print("2. Manage Certificates")
    print("3. Generate Hashes")
    print("4. Set up SSL Server")
    print("5. Connect SSL Client to already set up server")
    print("6. Digital Signature and Verification")
    print("0. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        clear_screen()
        print("Encrypt and Decrypt Files")
        encrypt_file(input_file, output_file)
        input("Press Enter to continue...")
        main_menu()
    elif choice == '2':
        clear_screen()
        print("Manage Certificates")
        generate_certificates()
        sign_certificate()
        input("Press Enter to continue...")
        main_menu()
    elif choice == '3':
        clear_screen()
        print("Generate Hashes")
        generate_sha256_hash(input_file)
        generate_md5_hash(input_file)
        input("Press Enter to continue...")
        main_menu()
    elif choice == '4':
        clear_screen()
        print("Implement Secure Communication (Server)")
        setup_ssl_server()
        print("TLS/SSL server set up successfully!")
        input("Press Enter to continue...")
        main_menu()
    elif choice == '5':
        clear_screen()
        print("Implement Secure Communication (Client)")
        generate_client_certificate()  # Generate client key and certificate
        setup_ssl_client()  # Connect to server with SSL/TLS
        print("TLS/SSL client connected successfully!")
        input("Press Enter to continue...")
        main_menu()
    elif choice == '6':
        clear_screen()
        print("Digital Signature and Verification")
        subprocess.run(['openssl', 'genrsa', '-out', 'private-key.pem', '2048'])
        subprocess.run(['openssl', 'rsa', '-in', 'private-key.pem', '-pubout', '-out', 'public-key.pem'])
        generate_digital_signature(input_file)
        verify_digital_signature(input_file)
        print("Digital signature generated and verified successfully!")
        input("Press Enter to continue...")
        main_menu()
    elif choice == '0':
        clear_screen()
        print("Exiting...")
    else:
        print("Invalid choice. Please try again.")
        input("Press Enter to continue...")
        main_menu()

# Entry point of the script
if __name__ == "__main__":
	input_file = input("Enter the path of the input file: ")
	output_file = input("Enter the path of the output file: ")
	main_menu()
