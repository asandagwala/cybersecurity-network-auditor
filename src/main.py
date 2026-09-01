import json

from checks import (run_security_checks, check_firewall, check_authentication, 
                    check_remote_admin_enabled, check_network_encryption, check_unnecessary_services, 
                    check_firmware_status,calculate_overall_risk, prioritise_findings, generate_audit_report)

def load_configuration():
    with open("data/config.json", "r") as file:
        configuration = json.load(file)
        
    return configuration

def main():
    configuration = load_configuration() 
    
    findings = run_security_checks(configuration, [check_firewall,check_authentication, 
    check_remote_admin_enabled, check_network_encryption, check_unnecessary_services,
    check_firmware_status])
    
    prioritised_findings = prioritise_findings(findings)
    
    overall_risk = calculate_overall_risk(findings)
    report = generate_audit_report(configuration, prioritised_findings, overall_risk)
    print(report)
    
  
    
    
    

if __name__ == "__main__":
    main()