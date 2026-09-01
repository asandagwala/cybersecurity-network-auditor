
"""
The run_security_checks function runs the security checks against a
network device configuration and collects any security findings.

It takes the device configuration and a list of security checks,
executes each check, and stores the findings that are returned.

The collected findings are returned so they can later be used for
risk assessment and reporting.
"""

def run_security_checks(configuration,checks):
    findings = []
    
    for check in checks:
        finding = check(configuration)
        
        if finding:
            findings.append(finding)
        
    return findings


def check_firewall(configuration):
    if configuration["firewall_enabled"]:
        return None
    
    return{
        "check": "Firewall",
        "severity": "HIGH",
        "message": "Firewall is disabled, removing an important layer of network protection.",
         "recommendation": "Enable the firewall to provide an important layer of network protection."
    }
    
    
def check_authentication(configuration):
    if not configuration["default_credentials"]:
        return None
    
    return {
        "check":"Authentication",
        "severity": "CRITICAL",
        "message" : "Default credentials are still in use.",
         "recommendation": "Change the default credentials to strong, unique credentials."
    }

def check_remote_admin_enabled(configuration):
    if not configuration["remote_admin_enabled"]:
        return None
    
    return {
        "check" : "Remote Admin",
        "severity" : "HIGH",
        "message" : "Remote administration is enabled, increasing the device's attack surface.",
        "recommendation": "Disable remote administration if it is not required."
       
    }
    
def check_network_encryption(configuration):
    if configuration["encryption"] == "WPA3" or configuration["encryption"]== "WPA2":
        return None
    
    return {
        "check": "Network Encryption",
        "severity": "HIGH",
        "message": "The network is using an insecure encryption protocol.",
        "recommendation": "Use WPA2 or WPA3 encryption to protect network communications."
        
    }
    
def check_unnecessary_services(configuration):
    if "ftp" in configuration["services"]:
        return {
        "check": "Services",
        "severity": "HIGH",
        "message":"FTP is enabled and does not encrypt credentials or data.",
        "recommendation": "Disable FTP and use a secure alternative such as SFTP when file transfer is required."
    }
    return None
    
def check_firmware_status(configuration):
    if configuration["firmware_status"] != "outdated":
        return None
    
    return {
        "check": "Firmware Status",
        "severity" : "MEDIUM",
        "message": "Device firmware is outdated and may contain known vulnerabilities.",
        "recommendation": "Update the device firmware to the latest supported version."
    }
    
def calculate_overall_risk(findings):
    severities = [finding["severity"] for finding in findings]
    
    if "CRITICAL" in severities:
        return "Critical"
    
    if "HIGH" in severities:
        return "HIGH"
    
    if "MEDIUM" in severities:
        return "MEDIUM"
    
    else:
        return "LOW"
    
def prioritise_findings(findings):
    severity_priority = {
        "CRITICAL": 1,
        "HIGH": 2,
        "MEDIUM": 3,
        "LOW": 4
    }
    
    return sorted(findings, key=lambda finding: severity_priority[finding["severity"]])

def generate_audit_report(configuration, findings, overall_risk):
    report = []
    
    report.append("=============================================")
    report.append("       CYBERSECURITY AUDIT REPORT    ")
    report.append("=============================================") 
    report.append("")
    
    report.append(f"Device: {configuration['device']}")
    report.append(f"Overall Risk: {overall_risk}")
    report.append(f"Total Findings: {len(findings)}")
    report.append("")
    
    report.append("------------------------------------------------")
    report.append("FINDINGS")
    report.append("-------------------------------------------------")
    report.append("")
    
    for finding in findings:
        report.append(f"[{finding['severity']}] {finding['check']}")
        report.append(f"Issue: {finding['message']}")
        report.append(f"Recommendation: {finding['recommendation']}")
        report.append("")
        
        report.append("================================================") 
        
    return "\n".join(report)                          