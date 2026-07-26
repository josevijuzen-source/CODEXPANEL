# ðŸ› ï¸ CodexPanel

Web Hosting Control Panel powered by OpenLiteSpeed, designed to simplify hosting management.

---

## ðŸ”§ Features & Services

- ðŸ” **Different User Access Levels** (via ACLs).
- ðŸŒŒ **Auto SSL** for secure websites.
- ðŸ’» **FTP Server** for file transfers.
- ðŸ•’ **Light-weight DNS Server** (PowerDNS).
- ðŸ” **phpMyAdmin** to manage databases (MariaDB).
- ðŸ“§ **Email Support** (SnappyMail).
- ðŸ•Œ **File Manager** for quick file access.
- ðŸŒ **PHP Management** made easy.
- ðŸ”’ **Firewall** (FirewallD & ConfigServer Firewall Integration).
- ðŸ“€ **One-click Backups and Restores**.
- ðŸ³ **Docker Management** with command execution capabilities.
- ðŸ¤– **AI-Powered Security Scanner** for enhanced protection.
- ðŸ“Š **Monthly Bandwidth Reset** - Automatic bandwidth usage reset (Fixed in latest version).

---

## ðŸ“– **Documentation & Guides**

CodexPanel comes with comprehensive documentation and step-by-step guides:

- ðŸ“š **[Complete Guides Index](guides/INDEX.md)** - All available documentation in one place
- ðŸ³ **[Docker Command Execution](guides/Docker_Command_Execution_Guide.md)** - Execute commands in Docker containers
- ðŸ¤– **[AI Scanner Setup](guides/AIScannerDocs.md)** - Configure AI-powered security scanning
- ðŸ“§ **[Mautic Installation](guides/MAUTIC_INSTALLATION_GUIDE.md)** - Email marketing platform setup

---

## ðŸ”¢ Supported PHP Versions

CodexPanel supports a wide range of PHP versions across different operating systems:

### â˜‘ï¸ **Currently Supported PHP Versions**

- **PHP 8.5** - Latest stable version (EOL: Dec 2028)
- **PHP 8.4** - Stable version (EOL: Dec 2027)
- **PHP 8.3** - Stable version (EOL: Dec 2027)
- **PHP 8.2** - Stable version (EOL: Dec 2026)
- **PHP 8.1** - Stable version (EOL: Dec 2025)
- **PHP 8.0** - Legacy support (EOL: Nov 2023)
- **PHP 7.4** - Legacy support (EOL: Nov 2022)

### ðŸ”§ **Third-Party PHP Add-ons**

For additional PHP versions or specific requirements, you can install third-party packages:

#### **Ubuntu/Debian**

- **Ondrej's PPA**: Provides PHP 5.6 to 8.5
- **Sury's PPA**: Alternative repository with latest PHP versions

#### **RHEL-based Systems** (AlmaLinux, RockyLinux, CentOS, RHEL)

- **Remi Repository**: Comprehensive PHP package collection
- **EPEL Repository**: Additional packages for enterprise Linux

#### **CloudLinux**

- **CloudLinux PHP Selector**: Built-in tool for managing multiple PHP versions
- **Remi Repository**: Additional PHP versions and extensions

> **Note**: Third-party repositories may provide additional PHP versions beyond what's available in default repositories. Always verify compatibility with your specific use case.

---

## ðŸŒ Supported Operating Systems

CodexPanel runs on x86_64 architecture and supports the following operating systems:

### **âœ… Currently Supported**

- **Ubuntu 24.04.3** - Supported until April 2029 â­ **NEW!**
- **Ubuntu 22.04** - Supported until April 2027
- **Ubuntu 20.04** - Supported until April 2025
- **AlmaLinux 10** - Supported until May 2030 â­ **NEW!**
- **AlmaLinux 9** - Supported until May 2032
- **AlmaLinux 8** - Supported until May 2029
- **RockyLinux 9** - Supported until May 2032
- **RockyLinux 8** - Supported until May 2029
- **RHEL 9** - Supported until May 2032
- **RHEL 8** - Supported until May 2029
- **CloudLinux 8** - Supported until May 2029
- **CentOS 9** - Supported until May 2027

### **ðŸ”§ Third-Party OS Support**

Additional operating systems may be supported through third-party repositories or community efforts:

- **Debian** - May work with Ubuntu-compatible packages
- **openEuler** - Community-supported with limited testing
- **Other RHEL derivatives** - May work with AlmaLinux/RockyLinux packages

> **Note**: For unsupported operating systems, compatibility is not guaranteed. Always test in a non-production environment first.

---

## âš™ï¸ Installation Instructions

Install CodexPanel easily with the following command:

```bash
sh <(curl https://codexpanel.net/install.sh || wget -O - https://codexpanel.net/install.sh)
```


---

## ðŸ“Š Upgrading CodexPanel

Upgrade your CodexPanel installation using:

```bash
sh <(curl https://raw.githubusercontent.com/usmannasir/CodexPanel/stable/preUpgrade.sh || wget -O - https://raw.githubusercontent.com/usmannasir/CodexPanel/stable/preUpgrade.sh)
```

---

## ðŸ†• Recent Updates & Fixes

### **Bandwidth Reset Issue Fixed** (January 2025)
- **Issue**: Monthly bandwidth usage was not resetting, causing cumulative values to grow indefinitely
- **Solution**: Implemented automatic monthly bandwidth reset for all websites and child domains
- **Affected OS**: All supported operating systems (Ubuntu, AlmaLinux, RockyLinux, RHEL, CloudLinux, CentOS)
- **Manual Reset**: Use `/usr/local/CodexCP/scripts/reset_bandwidth.sh` for immediate reset
- **Documentation**: See [Bandwidth Reset Fix Guide](to-do/CodexPanel-bandwidth-reset-fix.md)

### **New Operating System Support Added** (January 2025)
- **Ubuntu 24.04.3**: Full compatibility with latest Ubuntu LTS
- **AlmaLinux 10**: Full compatibility with latest AlmaLinux release
- **Long-term Support**: Both supported until 2029-2030

---

## ðŸ“š Resources

- ðŸŒ [Official Site](https://codexpanel.net)
- âœï¸ [Docs (New)](https://codexpanel.net/KnowledgeBase/)
- ðŸŽ“ [Docs (Old)](https://community.codexpanel.net/docs)
- ðŸ“– [Additional Guides](guides/INDEX.md) - Detailed guides for Docker, AI Scanner, Mautic, and more
- ðŸ“š [Local Documentation](guides/) - All guides available in this repository
- ðŸ¤ [Contributing Guide](CONTRIBUTING.md) - How to contribute to CodexPanel development
- âœ… [Changelog](https://codexpanel.net/KnowledgeBase/home/change-logs/)
- ðŸ’¬ [Forums](https://community.codexpanel.net)
- ðŸ“¢ [Discord](https://discord.gg/g8k8Db3)
- ðŸ“µ [Facebook Group](https://www.facebook.com/groups/CodexPanel)
- ðŸŽ¥ [YouTube Channel](https://www.youtube.com/@Cyber-Panel)

### ðŸ“– **Quick Start Guides**

- ðŸ³ [Docker Command Execution](guides/Docker_Command_Execution_Guide.md) - Execute commands in Docker containers
- ðŸ¤– [AI Scanner Setup](guides/AIScannerDocs.md) - Configure AI-powered security scanning
- ðŸ“§ [Mautic Installation](guides/MAUTIC_INSTALLATION_GUIDE.md) - Email marketing platform setup
- ðŸ“š [All Guides Index](guides/INDEX.md) - Complete documentation hub

### ðŸ”— **Direct Guide Links**

| Feature     | Guide                                                      | Description                    |
| ----------- | ---------------------------------------------------------- | ------------------------------ |
| ðŸ³ Docker   | [Command Execution](guides/Docker_Command_Execution_Guide.md) | Execute commands in containers |
| ðŸ¤– Security | [AI Scanner](guides/AIScannerDocs.md)                         | AI-powered security scanning   |
| ðŸ“§ Email    | [Mautic Setup](guides/MAUTIC_INSTALLATION_GUIDE.md)           | Email marketing platform       |
| ðŸ“Š Bandwidth | [Reset Fix Guide](to-do/CodexPanel-bandwidth-reset-fix.md)    | Fix bandwidth reset issues     |
| ðŸ“š All      | [Complete Index](guides/INDEX.md)                             | Browse all available guides    |

---

## ðŸ§ª Testing

CodexPanel includes an OLS feature test suite with 128 tests covering all custom OpenLiteSpeed features.

### Running Tests

```bash
# On the target server, set up test data (once):
bash tests/ols_test_setup.sh

# Run the full 128-test suite:
bash tests/ols_feature_tests.sh
```

### Test Coverage

| Phase | Tests | Coverage |
|-------|-------|----------|
| Phase 1: Live Environment | 56 | Binary integrity, CodexPanel module, Auto-SSL, LE certificates, SSL listener auto-mapping, cert serving, HTTPS/HTTP, .htaccess processing, VHost config, origin headers, PHP config |
| Phase 2: ReadApacheConf | 72 | Include/IncludeOptional, global tuning, listener creation, ProxyPass, IfModule, VHost creation, SSL dedup, Directory/Location blocks, PHP version detection, ScriptAlias, HTTP/HTTPS, process health, graceful restart |

---

## ðŸ”§ Troubleshooting

### **Common Issues & Solutions**

#### **Bandwidth Not Resetting Monthly**
- **Issue**: Bandwidth usage shows cumulative values instead of monthly usage
- **Solution**: Run the bandwidth reset script: `/usr/local/CodexCP/scripts/reset_bandwidth.sh`
- **Prevention**: Ensure monthly cron job is running: `0 0 1 * * /usr/local/CodexCP/bin/python /usr/local/CodexCP/postfixSenderPolicy/client.py monthlyCleanup`


#### **General Support**
- Check logs: `/usr/local/lscp/logs/error.log`
- Verify cron jobs: `crontab -l`
- Test manual reset: Use provided scripts in `/usr/local/CodexCP/scripts/`
