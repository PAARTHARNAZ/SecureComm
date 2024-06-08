# SecureComm

SecureComm is a versatile tool designed to facilitate various cryptographic and secure communication tasks using OpenSSL. It includes functionalities for file encryption/decryption, certificate management, hash generation, and setting up secure TLS/SSL communication.

## Features

- **Encrypt and Decrypt Files**: Encrypt and decrypt files using AES-256.
- **Manage Certificates**: Generate self-signed certificates, Certificate Signing Requests (CSR), and sign CSRs.
- **Generate Hashes**: Generate SHA-256 and MD5 hashes of files.
- **Set up SSL Server**: Establish a secure TLS/SSL server.
- **Connect SSL Client**: Connect to a TLS/SSL server as a client.
- **Digital Signature**: Generate and verify digital signatures.

## Prerequisites

Ensure you have `openssl` installed on your system. If not, install it using:

```sh
sudo apt-get install openssl
```

## Installation

Clone the repository and navigate to the directory:

```sh
git clone https://github.com/PAARTHARNAZ/SecureComm.git
cd SecureComm
```

## Usage

Run SecureComm from the command line:

```sh
python securecomm.py
```

### Main Menu

The script presents a main menu with the following options:

1. **Encrypt and Decrypt Files**
2. **Manage Certificates**
3. **Generate Hashes**
4. **Set up SSL Server**
5. **Connect SSL Client to already set up server**
6. **Digital Signature and Verification**
0. **Exit**

### Example Workflow

1. **Encrypt a File**:

    ```sh
    Enter your choice: 1
    ```

2. **Manage Certificates**:

    ```sh
    Enter your choice: 2
    ```

3. **Generate Hashes**:

    ```sh
    Enter your choice: 3
    ```

4. **Set up SSL Server**:

    ```sh
    Enter your choice: 4
    ```

5. **Connect SSL Client**:

    ```sh
    Enter your choice: 5
    ```

6. **Digital Signature and Verification**:

    ```sh
    Enter your choice: 6
    ```

## Functionality Details

### Encrypt and Decrypt Files

Encrypt a file:

```python
encrypt_file(input_file, output_file)
```

Decrypt a file:

```python
decrypt_file(input_file, output_file)
```

### Manage Certificates

Generate self-signed certificates and CSR:

```python
generate_certificates()
```

Sign a CSR:

```python
sign_certificate()
```

### Generate Hashes

Generate SHA-256 hash:

```python
generate_sha256_hash(input_file)
```

Generate MD5 hash:

```python
generate_md5_hash(input_file)
```

### Set up SSL Server

Set up a TLS/SSL server:

```python
setup_ssl_server()
```

### Connect SSL Client

Connect to a TLS/SSL server as a client:

```python
setup_ssl_client()
```

### Digital Signature

Generate a digital signature:

```python
generate_digital_signature(input_file)
```

Verify a digital signature:

```python
verify_digital_signature(input_file)
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and ensure you have permission to perform cryptographic operations and network communications on the target systems.

---

Happy securing with SecureComm!
