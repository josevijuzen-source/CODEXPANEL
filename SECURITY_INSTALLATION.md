# CodexPanel Secure Installation Guide

## Overview

This document describes the secure installation process for CodexPanel that eliminates hardcoded passwords and implements environment-based configuration.

## Security Improvements

### âœ… **Fixed Security Vulnerabilities**

1. **Hardcoded Database Passwords** - Now generated securely during installation
2. **Hardcoded Django Secret Key** - Now generated using cryptographically secure random generation
3. **Environment Variables** - All sensitive configuration moved to `.env` file
4. **File Permissions** - `.env` file set to 600 (owner read/write only)

### ðŸ” **Security Features**

- **Cryptographically Secure Passwords**: Uses Python's `secrets` module for password generation
- **Environment-based Configuration**: Sensitive data stored in `.env` file, not in code
- **Secure File Permissions**: Environment files protected with 600 permissions
- **Credential Backup**: Automatic backup of credentials for recovery
- **Fallback Security**: Maintains backward compatibility with fallback method

## Installation Process

### 1. **Automatic Secure Installation**

The installation script now automatically:

1. Generates secure random passwords for:
   - MySQL root user
   - CodexPanel database user
   - Django secret key

2. Creates `.env` file with secure configuration:
   ```bash
   # Generated during installation
   SECRET_KEY=your_64_character_secure_key
   DB_PASSWORD=your_24_character_secure_password
   ROOT_DB_PASSWORD=your_24_character_secure_password
   ```

3. Creates `.env.backup` file for credential recovery
4. Sets secure file permissions (600) on all environment files

### 2. **Manual Installation** (if needed)

If you need to manually generate environment configuration:

```bash
cd /usr/local/CodexCP
python install/env_generator.py /usr/local/CodexCP
```

## File Structure

```
/usr/local/CodexCP/
â”œâ”€â”€ .env                    # Main environment configuration (600 permissions)
â”œâ”€â”€ .env.backup            # Credential backup (600 permissions)
â”œâ”€â”€ .env.template          # Template for manual configuration
â”œâ”€â”€ .gitignore             # Prevents .env files from being committed
â””â”€â”€ CodexCP/
    â””â”€â”€ settings.py        # Updated to use environment variables
```

## Security Best Practices

### âœ… **Do's**

- Keep `.env` and `.env.backup` files secure
- Record credentials from `.env.backup` and delete the file after installation
- Use strong, unique passwords for production deployments
- Regularly rotate database passwords
- Monitor access to environment files

### âŒ **Don'ts**

- Never commit `.env` files to version control
- Don't share `.env` files via insecure channels
- Don't use default passwords in production
- Don't leave `.env.backup` files on the system after recording credentials

## Recovery

### **Lost Credentials**

If you lose your database credentials:

1. Check if `.env.backup` file exists:
   ```bash
   sudo cat /usr/local/CodexCP/.env.backup
   ```

2. If backup doesn't exist, you'll need to reset MySQL passwords using MySQL recovery procedures

### **Regenerate Environment**

To regenerate environment configuration:

```bash
cd /usr/local/CodexCP
sudo python install/env_generator.py /usr/local/CodexCP
```

## Configuration Options

### **Environment Variables**

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Generated (64 chars) |
| `DB_PASSWORD` | CodexPanel DB password | Generated (24 chars) |
| `ROOT_DB_PASSWORD` | MySQL root password | Generated (24 chars) |
| `DEBUG` | Debug mode | False |
| `ALLOWED_HOSTS` | Allowed hosts | localhost,127.0.0.1,hostname |

### **Custom Configuration**

To use custom passwords during installation:

```bash
python install/env_generator.py /usr/local/CodexCP "your_root_password" "your_db_password"
```

## Troubleshooting

### **Installation Fails**

If the new secure installation fails:

1. Check installation logs for error messages
2. The system will automatically fallback to the original installation method
3. Verify Python dependencies are installed:
   ```bash
   pip install python-dotenv
   ```

### **Environment Loading Issues**

If Django can't load environment variables:

1. Ensure `.env` file exists and has correct permissions:
   ```bash
   ls -la /usr/local/CodexCP/.env
   # Should show: -rw------- 1 root root
   ```

2. Install python-dotenv if missing:
   ```bash
   pip install python-dotenv
   ```

## Migration from Old Installation

### **Existing Installations**

For existing CodexPanel installations with hardcoded passwords:

1. **Backup current configuration**:
   ```bash
   cp /usr/local/CodexCP/CodexCP/settings.py /usr/local/CodexCP/CodexCP/settings.py.backup
   ```

2. **Generate new environment configuration**:
   ```bash
   cd /usr/local/CodexCP
   python install/env_generator.py /usr/local/CodexCP
   ```

3. **Update settings.py** (already done in new installations):
   - The settings.py file now supports environment variables
   - It will fallback to hardcoded values if .env is not available

4. **Test the configuration**:
   ```bash
   cd /usr/local/CodexCP
   python manage.py check
   ```

## Support

For issues with the secure installation:

1. Check the installation logs
2. Verify file permissions
3. Ensure all dependencies are installed
4. Review the fallback installation method if needed

---

**Security Notice**: This installation method significantly improves security by eliminating hardcoded credentials. Always ensure proper file permissions and secure handling of environment files.

