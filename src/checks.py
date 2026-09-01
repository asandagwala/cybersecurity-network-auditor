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
        "message": "Firewall is disabled."
    }
    
    
def check_authentication(configuration):
    if not configuration["default_credentials"]:
        return None
    
    return {
        "check":"Authentication",
        "severity": "CRITICAL",
        "message" : "Default credentials are still in use."
    }

def check_remote_admin_enabled(configuration):
    if not configuration["remote_admin_enabled"]:
        return None
    
    return {
        "check" : "Remote Admin",
        "severity" : "High",
        "message" : "Remote Admin is enabled"
    }