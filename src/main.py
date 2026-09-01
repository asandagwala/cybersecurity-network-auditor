import json

from checks import (run_security_checks, check_firewall, check_authentication, 
                    check_remote_admin_enabled, check_network_encryption, check_unnecessary_services, 
                    check_firmware_status,calculate_overall_risk)

def load_configuration():
    with open("data/config.json", "r") as file:
        configuration = json.load(file)
        
    return configuration

def main():
    configuration = load_configuration() 
    
    findings = run_security_checks(configuration, [check_firewall,check_authentication, 
    check_remote_admin_enabled, check_network_encryption, check_unnecessary_services,
    check_firmware_status])
    
    overall_risk = calculate_overall_risk(findings)
    
    
    print("Security checks completed.")
    print(f"Findings:{len(findings)}")
    for finding in findings:
        print(finding)
    print(f"Overall Risk:{overall_risk}")
    
    

if __name__ == "__main__":
    main()