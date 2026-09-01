# Cybersecurity Network Auditor

A Python-based security auditing tool that evaluates network and device configurations, identifies common security weaknesses, assesses their severity, and provides recommendations for improving the security posture of the environment.

## Overview

Network devices and services can introduce security risks when they are incorrectly configured, unnecessarily exposed, or not maintained securely.

The Cybersecurity Network Auditor is designed to help identify these risks through a set of automated security checks. The tool evaluates a configuration against defined security criteria and produces an audit report highlighting areas that require attention.

The project is being developed as a practical exploration of cybersecurity concepts, with an emphasis on understanding how security principles can be translated into software.

## Objectives

The project aims to:

* Identify common security weaknesses in network and device configurations.
* Apply fundamental cybersecurity principles to a practical software project.
* Classify security findings according to their severity.
* Provide clear, actionable recommendations for identified risks.
* Produce an understandable security audit report.
* Demonstrate software development practices including testing, validation, documentation, and version control.

## How It Works

The auditor follows a simple assessment process:

```text
Configuration
      │
      ▼
Security Checks
      │
      ▼
Findings
      │
      ▼
Risk Assessment
      │
      ▼
Recommendations
      │
      ▼
Audit Report
```

A configuration is evaluated against a collection of security checks. Each check determines whether a particular security requirement has been satisfied and records a finding when a potential weakness is identified.

The findings are then assessed according to their severity, allowing the tool to provide an overall view of the security posture and prioritise areas that require attention.

### Configuration

The auditor uses a JSON configuration file as its input. The configuration represents the security settings of a network device, such as a router.

The configuration currently includes information about:

- Firewall status
- Default credentials
- Remote administration
- Network encryption
- Firmware status
- Enabled services

## Planned Security Checks

The initial version of the auditor will focus on common configuration and network security concerns, including:

* Firewall configuration
* Authentication and default credentials
* Network encryption
* Remote administration
* Unnecessary services
* Software and firmware updates
* Other configuration weaknesses identified during development

The checks will evolve as the project develops and as additional cybersecurity concepts are explored.

## Technology

**Language**

* Python

**Testing**

* Pytest

**Development Tools**

* Git
* GitLab

Additional technologies will be introduced where they provide a clear benefit to the project.

## Project Structure

The project will follow a modular structure so that individual security checks, risk assessment logic, and reporting functionality can be developed and tested independently.

```text
cybersecurity-network-auditor/
│
├── src/
│   ├── checks/
│   ├── models/
│   ├── reporting/
│   └── ...
│
├── tests/
│
├── data/
│
├── docs/
│
├── README.md
└── requirements.txt
```

The structure will evolve as the application grows.

## Example

A completed audit could produce findings such as:

```text
Security Audit
--------------

Firewall                 PASS
Authentication           PASS
Network Encryption       PASS
Remote Administration    WARNING
Firmware Status          CRITICAL

Overall Risk: HIGH

Recommendations:
- Disable remote administration where it is not required.
- Update the device firmware to a supported version.
```

## Development

The project is developed iteratively, with functionality introduced, tested, and refined as the application evolves. Security checks and design decisions are informed by cybersecurity concepts and practical experimentation.

## Learning

This project is being developed alongside cybersecurity coursework and independent learning. Concepts from the Cisco Introduction to Cybersecurity course and additional practical cybersecurity training will be applied where relevant.

The project provides an opportunity to explore how concepts such as security controls, risk assessment, authentication, network security, and threat mitigation can be implemented in software.

## Future Improvements

Potential future improvements include:

* Expanded security checks
* Configurable security rules
* Improved risk scoring
* More detailed audit reports
* Additional input formats
* Logging
* Automated testing
* Command-line options
* Improved reporting and visualisation

## Project Status

**In development**

The project is currently in the early development stage. Features, architecture, and security checks will continue to evolve as development progresses.
