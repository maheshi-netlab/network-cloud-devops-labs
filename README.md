# Network, Cloud & DevOps Engineering Labs

A hands-on learning repository for building practical skills in **network engineering, network security, cloud networking, DevOps, and automation**.

The labs use networking and security scenarios to develop skills progressively—from Linux, Git, and Bash to JSON, Python, REST APIs, Infrastructure as Code, and cloud automation.

## Learning goals

- Automate network and security tasks with Bash and Python.
- Work with JSON and YAML configuration data.
- Understand and consume REST APIs using Postman and Python.
- Build repeatable infrastructure with Terraform.
- Use Git, GitHub, and GitHub Actions for source control and CI/CD.
- Develop practical AWS and Azure networking and security skills.
- Apply testing, troubleshooting, and DevSecOps practices.

## Learning roadmap

The roadmap is organized as a progression. Lab status reflects work completed in this repository; future topics are planned learning milestones.

| Phase | Focus | Status |
|---|---|---|
| 1 | Linux, Git, GitHub, and Bash fundamentals | Completed |
| 2 | Advanced Git: branches, pull requests, reviews, and merge conflicts | Completed |
| 3 | GitHub Actions and CI/CD fundamentals | Completed |
| 4 | Bash quality, ShellCheck, JSON, and Python fundamentals | In progress |
| 5 | Python for network automation | Planned |
| 6 | REST APIs and Postman | Planned |
| 7 | Python API integration and automation | Planned |
| 8 | Terraform and Infrastructure as Code | Planned |
| 9 | AWS and Azure cloud networking | Planned |
| 10 | Advanced CI/CD with GitHub Actions | Planned |
| 11 | Docker and Kubernetes | Planned |
| 12 | Ansible automation | Planned |
| 13 | DevSecOps, monitoring, and security validation | Planned |
| 14 | Network and cloud security automation capstone | Planned |

## Lab progress

### Lab 01 — Linux and Git fundamentals

**Topics**
- Linux commands and filesystem navigation
- Git configuration and repository workflow
- Bash scripting
- Network configuration validation

**Practical work:** Created a Bash script to validate required network configuration values, including DNS resolvers and SSH management settings.

### Lab 02 — Advanced Git and GitHub

**Topics**
- Feature branches and branching workflows
- Pull requests and code reviews
- Merge and conflict resolution
- GitHub Wiki documentation

**Practical work:** Practiced collaborative firewall configuration changes, resolved a simulated merge conflict, and documented the resolution.

### Lab 03 — GitHub Actions and CI/CD

**Topics**
- Workflow triggers for pushes and pull requests
- GitHub-hosted runners
- Checkout and script execution steps
- Exit codes and automated validation
- CI failure analysis and recovery

**Practical work:** Added a GitHub Actions workflow to run the network configuration validation script. Tested both successful and intentionally failing configurations, then restored a passing configuration.

### Lab 04 — Bash quality, JSON, and Python

**Topics and progress**
- Installed and ran ShellCheck against the Bash validation script.
- Used `bash -n` for syntax validation.
- Improved the script to locate its configuration file relative to the script itself.
- Tested the script from the repository directory and from `/tmp`.
- Next: learn JSON fundamentals and begin Python using network configuration examples.

**Latest completed change:** Made the validation script independent of the current working directory.

## Repository layout

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
│   └── 02-advanced-git/
│       ├── README.md
│       ├── network-security.conf
│       └── docs/
│           └── merge-conflict-resolution.md
└── README.md
```

Additional lab folders and exercises will be added as the roadmap progresses.

## Technology areas

| Area | Tools and concepts |
|---|---|
| Operating systems | Linux, openSUSE, Windows |
| Scripting and programming | Bash, Python |
| Data formats | JSON, YAML |
| Version control | Git, GitHub |
| CI/CD | GitHub Actions |
| API tooling | Postman, REST APIs |
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

**Practice environments**
- Windows with Visual Studio Code.
- Linux using KodeKloud sandbox environments.

The learning pace is intentionally incremental: one concept and exercise at a time, with validation before moving forward.

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

---

*Learning by building, testing, troubleshooting, documenting, and continuously improving practical engineering skills.*
