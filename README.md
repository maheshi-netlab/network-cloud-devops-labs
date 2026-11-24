# Network, Cloud & DevOps Engineering Labs

A hands-on learning repository for building practical skills in **network engineering, network security, cloud networking, DevOps, and automation**.

The labs use networking and security scenarios to develop skills progressively—from Linux, Git, and Bash to JSON, Python, REST APIs, API-driven security automation, Infrastructure as Code, and cloud automation.

## Learning goals

- Automate network and security tasks with Bash and Python.
- Work with JSON and YAML configuration data.
- Understand and consume REST APIs using curl and Python Requests.
- Analyze firewall policies and validate IP addresses and CIDR networks.
- Generate security reports and application logs.
- Test automation code with Python unit tests.
- Build repeatable infrastructure with Terraform.
- Use Git, GitHub, and GitHub Actions for source control and CI/CD.
- Develop practical AWS and Azure networking and security skills.
- Apply testing, troubleshooting, and DevSecOps practices.

## Learning roadmap

Lab status reflects work completed and verified through **Lab 08**. Future topics are planned learning milestones.

| Lab | Focus | Status |
|---|---|---|
| 01 | Linux and Git fundamentals | Completed |
| 02 | Advanced Git and GitHub: branches, pull requests, reviews, and merge conflicts | Completed |
| 03 | GitHub Actions and CI/CD fundamentals | Completed |
| 04 | Bash automation, ShellCheck, and script quality | Completed |
| 05 | JSON fundamentals and firewall service validation | Completed |
| 06 | Python fundamentals and firewall configuration validation | Completed |
| 07 | REST API fundamentals, HTTP methods, headers, status codes, and authentication concepts | Completed |
| 08 | Python REST API security automation, firewall policy analysis, reporting, logging, unit testing, and CI integration | Completed |
| 09 | Terraform fundamentals and Infrastructure as Code | Next |
| 10 | AWS and Azure cloud networking | Planned |
| 11 | Advanced CI/CD and infrastructure automation | Planned |
| 12 | Docker and Kubernetes | Planned |
| 13 | Ansible automation | Planned |
| 14 | DevSecOps, monitoring, and security validation | Planned |
| 15 | Network and cloud security automation capstone | Planned |

## Lab progress

### Lab 01 — Linux and Git fundamentals

**Topics**
- Linux commands and filesystem navigation.
- Git configuration and repository workflow.
- Bash scripting.
- Network configuration validation.

**Practical work:** Created a Bash script to validate required network configuration values, including DNS resolvers and SSH management settings.

### Lab 02 — Advanced Git and GitHub

**Topics**
- Feature branches and branching workflows.
- Pull requests and code reviews.
- Merge and conflict resolution.
- GitHub Wiki documentation.

**Practical work:** Practiced collaborative firewall configuration changes, resolved a simulated merge conflict while preserving the intended configuration, and documented the resolution.

### Lab 03 — GitHub Actions and CI/CD

**Topics**
- Workflow triggers for pushes and pull requests.
- GitHub-hosted runners.
- Checkout and script execution steps.
- Exit codes and automated validation.
- CI failure analysis and recovery.

**Practical work:** Added a GitHub Actions workflow to run the network configuration validation script. Tested both successful and intentionally failing configurations, then restored a passing configuration.

### Lab 04 — Bash automation and ShellCheck

**Topics**
- Bash scripting and validation logic.
- ShellCheck static analysis.
- Bash syntax checking with `bash -n`.
- Relative path handling.
- Positive and negative testing.

**Practical work:** Improved the network validation script so it locates its configuration file relative to the script rather than depending on the current working directory. Tested it from the repository and from `/tmp`.

### Lab 05 — JSON fundamentals

**Topics**
- JSON objects, arrays, strings, numbers, and Boolean values.
- Reading JSON with Python's `json` module.
- Accessing nested configuration values.
- Validating required firewall services.

**Practical work:** Created a JSON firewall configuration and Python scripts to read configuration data and validate required services such as SSH, HTTPS, and DNS.

### Lab 06 — Python fundamentals

**Topics**
- Python variables and data types.
- Conditional statements and loops.
- Functions and reusable code.
- Exception handling.
- JSON file processing.
- IP address validation with Python's `ipaddress` module.

**Practical work:** Built a firewall configuration validator that checks required fields, management IP addresses, and required services. Tested valid and invalid configurations, missing files, and malformed JSON.

### Lab 07 — REST API fundamentals

**Topics**
- REST API concepts and HTTP request/response flow.
- HTTP methods: GET, POST, PUT, PATCH, and DELETE.
- HTTP status codes, including 200, 201, and 404.
- HTTP headers, including Accept and Content-Type.
- Python Requests basics.
- Bearer token authentication concepts.
- API response parsing and error handling.

**Practical work:** Used curl and Python Requests with the JSONPlaceholder test API to retrieve and inspect JSON responses, send simulated API operations, and handle HTTP status codes.

### Lab 08 — Python REST API automation for network security

**Topics**
- Python Requests and REST API integration.
- Custom HTTP headers and authentication header construction.
- JSON response inspection and validation.
- Firewall policy analysis using local JSON data.
- Management IP and source/destination CIDR validation.
- Detection of enabled Telnet allow rules.
- Security report generation.
- Python logging and exception handling.
- Unit testing with `unittest`.
- GitHub Actions integration.

**Practical work:** Built an integrated security analyzer that checks connectivity to a test API, reads mock firewall policies from JSON, classifies policy findings, and generates reports and logs. Added unit tests and extended the GitHub Actions workflow to run the Python tests.

**Architecture note:** The API connectivity check uses JSONPlaceholder, and firewall policies are read from a local mock JSON file. This lab is not a live Palo Alto firewall API integration. The Bearer token example demonstrates request-header construction; JSONPlaceholder does not enforce token authentication.

**Verification:** Three firewall analyzer unit tests passed locally. The GitHub Actions run for commit `45d4dc0` completed successfully, including the network configuration validation and Python unit tests. The run displayed a Node.js 20 deprecation warning for the action versions in use; it did not fail the workflow.

## Repository layout

The repository currently includes the following lab and automation assets:

```text
network-cloud-devops-labs/
├── .github/
│   └── workflows/
│       └── network-security-validation.yml
├── config/
│   └── network.conf
├── scripts/
│   └── validate_network_config.sh
├── labs/
│   ├── 02-advanced-git/
│   │   ├── README.md
│   │   ├── network-security.conf
│   │   └── docs/
│   │       └── merge-conflict-resolution.md
│   ├── 05-json-fundamentals/
│   ├── 06-python-fundamentals/
│   └── 08-python-rest-api-automation/
│       ├── data/
│       │   └── firewall_policies.json
│       ├── reports/
│       │   ├── firewall_security_report.txt
│       │   ├── integrated_security_report.txt
│       │   └── security_automation.log
│       ├── api_authentication.py
│       ├── api_custom_headers.py
│       ├── api_data_validator.py
│       ├── api_error_handling.py
│       ├── api_get_request.py
│       ├── api_response_headers.py
│       ├── firewall_analyzer.py
│       ├── firewall_api_client.py
│       ├── firewall_report.py
│       ├── inspect_api_response.py
│       ├── integrated_api_client.py
│       ├── integrated_security_analyzer.py
│       ├── logging_demo.py
│       ├── requirements.txt
│       ├── test_firewall_analyzer.py
│       └── validate_firewall_networks.py
└── README.md
```

## Technology areas

| Area | Tools and concepts |
|---|---|
| Operating systems | Linux, openSUSE, Windows |
| Scripting and programming | Bash, Python |
| Data formats | JSON, YAML |
| Version control | Git, GitHub |
| CI/CD | GitHub Actions |
| API tooling | curl, Python Requests, REST APIs, Postman concepts |
| Network validation | IP addresses, CIDR networks, firewall policy checks |
| Testing and quality | ShellCheck, bash syntax checks, Python unittest |
| Reporting and observability | Python logging, text reports |
| Infrastructure as Code | Terraform |
| Cloud | AWS, Microsoft Azure |
| Containers and orchestration | Docker, Kubernetes |
| Configuration management | Ansible |
| Security | Network security, cloud security, DevSecOps |

## How each lab is practiced

Each exercise follows a repeatable learning cycle:

1. Understand the concept.
2. Perform one hands-on task.
3. Validate the result.
4. Troubleshoot errors and understand the cause.
5. Document the outcome.
6. Commit and push completed work to GitHub.
7. Verify automated checks when a CI workflow applies.

**Practice environments**
- Windows with Visual Studio Code.
- Linux using KodeKloud sandbox environments.
- GitHub repository and GitHub Actions.

The learning pace is intentionally incremental: one concept and exercise at a time, with validation before moving forward.

## Next milestone — Lab 09: Terraform fundamentals

The next stage introduces Infrastructure as Code and builds on the Linux, Git, JSON, Python, and API skills developed in the completed labs.

Planned topics include:

- Terraform purpose and workflow.
- HCL syntax and configuration blocks.
- Providers, resources, and data sources.
- Input variables and outputs.
- Terraform plan and apply.
- State fundamentals.
- A practical cloud networking example.

## Capstone direction

**Cloud Network Security Automation and Troubleshooting Assistant**

The planned capstone will bring together Python, JSON, REST APIs, Bash, cloud networking, and security automation. Possible capabilities include:

- Parsing network and security diagnostic outputs.
- Validating DNS and connectivity configuration.
- Organizing routing, firewall, and VPN troubleshooting evidence.
- Integrating with supported cloud and security platform APIs.
- Producing structured troubleshooting reports.
- Running automated checks through CI/CD pipelines.

## Repository

[GitHub — maheshi-netlab/network-cloud-devops-labs](https://github.com/maheshi-netlab/network-cloud-devops-labs)

[Lab 08 — Python REST API Automation](https://github.com/maheshi-netlab/network-cloud-devops-labs/tree/main/labs/08-python-rest-api-automation)

---

*Learning by building, testing, troubleshooting, documenting, and continuously improving practical engineering skills.*
