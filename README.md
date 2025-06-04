
# Yescrypt CLI Password Hasher

A sophisticated command-line interface (CLI) tool for secure password hashing using the yescrypt algorithm.

```
                                                  __                
 ___.__. ____   ______ ___________ ___.__._______/  |_  ___________ 
<   |  |/ __ \ /  ___// ___\_  __ <   |  |\____ \   __\/ __ \_  __ \
 \___  \  ___/ \___ \\  \___|  | \/\___  ||  |_> >  | \  ___/|  | \/
 / ____|\___  >____  >\___  >__|   / ____||   __/|__|  \___  >__|   
 \/         \/     \/     \/       \/     |__|             \/       
```

## Brief Description

This Python script implements a secure password hashing tool using the **yescrypt** algorithm, a memory-hard key derivation function that serves as the default password hashing scheme in modern Linux distributions including Debian 11+, Fedora 35+, and Ubuntu 22.04+. 

Yescrypt is built on SHA-256, HMAC, and PBKDF2 approved primitives, making it NIST-compliant and suitable for high-security applications. The algorithm is designed to be memory-hard, requiring significant memory resources to compute hashes, which makes it highly resistant to GPU-based attacks and specialized hardware.

**Key Features:**
- 🔐 Secure yescrypt password hashing algorithm
- 🎨 Colorized command-line output
- ⚙️ Configurable security parameters (N, r, p, dkLen)
- 🧂 Custom or automatic salt generation
- ⏱️ Performance timing and memory usage reporting
- 🛡️ Memory-hard protection against brute-force attacks

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Install Dependencies

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/yescrypt-cli-hasher.git
   cd yescrypt-cli-hasher
   ```

2. **Install required Python packages:**
   ```bash
   pip install pyescrypt termcolor
   ```

   Or install from requirements file if provided:
   ```bash
   pip install -r requirements.txt
   ```

3. **Make the script executable (Linux/macOS):**
   ```bash
   chmod +x yescrypt_hasher.py
   ```

### System Compatibility
- ✅ Windows
- ✅ macOS  
- ✅ Linux

## Usage

### Basic Syntax

```bash
python3 yescrypt_hasher.py <word> [options]
```

### Arguments

#### Required Arguments
- `word` - The password or plaintext string to hash

#### Optional Arguments
- `--salt` - Custom salt as hexadecimal string (default: random 16 bytes)
- `--n` - CPU/memory cost parameter (default: 16384)
- `--r` - Block size parameter (default: 8)
- `--p` - Parallelism parameter (default: 1)
- `--dklen` - Derived key length in bytes (default: 64)

### Examples

#### Basic Password Hashing
```bash
python3 yescrypt_hasher.py "mypassword123"
```

**Output:**
```
[+] Input       : mypassword123
[+] Salt (hex)  : a1b2c3d4e5f67890abcdef1234567890
[+] Hash        : 7d8e9f0a1b2c3d4e5f6789abcdef0123456789abcdef...
[i] Time taken  : 0.1234 seconds
[i] Memory cost : ~16 MB (approx)
```

#### High-Security Configuration
```bash
python3 yescrypt_hasher.py "sensitive_password" --n 65536 --r 16 --p 2 --dklen 128
```

#### Custom Salt for Testing
```bash
python3 yescrypt_hasher.py "testpassword" --salt "deadbeefcafebabe1234567890abcdef"
```

#### Help Information
```bash
python3 yescrypt_hasher.py --help
```

### Security Parameters Guide

| Parameter | Description | Default | Security Impact |
|-----------|-------------|---------|-----------------|
| `--n` | CPU/memory cost | 16384 | Higher = more secure, slower |
| `--r` | Block size | 8 | Affects memory usage pattern |
| `--p` | Parallelism | 1 | Multi-threading capability |
| `--dklen` | Output length | 64 bytes | Hash output size |

### Memory Requirements

The approximate memory usage is calculated as: `128 * N * r / (1024 * 1024)` MB

| N Value | r Value | Approx. Memory |
|---------|---------|----------------|
| 16384 | 8 | ~16 MB |
| 32768 | 8 | ~32 MB |
| 65536 | 16 | ~128 MB |

## Security Considerations

- **Salt Management**: Always use unique salts for each password in production
- **Parameter Selection**: Higher N values provide better security but require more resources
- **Performance vs Security**: Balance computation time with security requirements
- **Memory-Hard Properties**: The algorithm's memory requirements protect against specialized hardware attacks

## License

This project is open source. Please check the repository for license details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.