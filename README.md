## **Secure Artifact Supply Chain with Policy-Driven CI/CD (JFrog Artifactory)**


## Overview

This project demonstrates an end-to-end **secure artifact supply chain** using GitHub Actions and JFrog Artifactory. It simulates how modern enterprises build, verify, publish, scan, and promote software artifacts with **strong auditability and least-privilege access controls**.

The focus is **pipeline security, artifact integrity, and traceability**, not application complexity.
---

## Objective

Design and implement a secure CI/CD pipeline that:

\- Builds and packages application artifacts
\- Publishes artifacts to JFrog Artifactory using **scoped access tokens**
\- Captures build metadata and integrity hashes
\- Performs security scanning using JFrog Xray
\- Promotes trusted builds across repositories
\- Provides audit visibility and traceability across the pipeline

This project simulates **real-world DevSecOps and supply-chain security practices**.
---

## Scope

\- One application (simple Python example)
\- One CI pipeline (GitHub Actions)
\- Secure authentication (scoped access token)
\- Security scanning (Xray build scan)
\- Artifact promotion
\- Audit and documentation
---

## Architecture (Logical Flow)

→ Developer Commit
→ GitHub Actions (Secure Build Pipeline)
→ Versioned \& Hashed Artifact
→ GitHub Actions (Publish Pipeline)
→ JFrog Artifactory (Local Repository)
→ Build Info + Xray Scan
→ Promotion to Release Repository
---

## Application

\- Simple Python application
\- Explicit dependency pinning (`requests==2.32.4`)
\- Version controlled via `version.txt`
\- SSL verification is **not disabled**
\- Graceful handling of SSL inspection failures commonly observed in enterprise networks

This ensures secure defaults and predictable builds.
---

## Security Controls Implemented

Secure Build Practices
\- Versioned artifacts
\- SHA-256 checksum generation
\- Build metadata capture:
  - Application name
  - Version
  - Git commit SHA
  - Build time
  - Build executor

Secure Authentication
\- No username/password authentication
\- No secrets committed to repository
\- JFrog access via **scoped access token**
\- Secrets stored in GitHub Secrets / Variables

CI/CD Pipeline Hardening
\- Separation of build and publish pipelines
\- Publish pipeline triggered only on successful build
\- Least-privilege permissions in workflows

Artifact Governance
\- Build info published to Artifactory
\- Build visible in JFrog Xray
\- Controlled promotion to release repository

Design choice
Security enforcement is performed at the artifact and build level, not within application logic, to align with centralized governance models.
---

## CI/CD Workflows

Secure Build Pipeline (`build.yml`)
**Trigger**: Push to `main`

**Responsibilities**:
\- Checkout source code
\- Read application version
\- Package application artifact
\- Generate build metadata
\- Generate SHA-256 checksum
\- Upload artifacts for downstream jobs

Publish, Scan \& Promote Pipeline (`ci-artifactory.yml`)
**Trigger**: `workflow_run` (only after successful build)

**Responsibilities**:
\- Download build artifacts
\- Configure JFrog CLI securely
\- Verify Artifactory connectivity
\- Upload artifact to Artifactory
\- Publish build info
\- Run Xray build scan
\- Promote build to release repository
---

## Security Scanning (Xray)
\- Xray build scan is executed on published build info
\- Build appears in Xray Build list
\- Pipeline is **policy-ready** for enforcement
\- Blocking policies can be added without changing pipeline structure

**Note**: This project demonstrates scanning and governance readiness rather than enforcing a blocking policy.
---

## Auditability \& Traceability
The pipeline enables:
\- Full traceability from Git commit -> build -> artifact -> promotion
\- Artifact integrity verification via checksums
\- Build-to-artifact mapping via JFrog Build Info
\- Historical audit of promoted releases
---

## Repository Structure
.
├── app/ # Python application
│ ├── main.py
│ ├── requirements.txt
│ └── version.txt
├── build/ # Build artifacts \& metadata
│ ├── secure-artifact-app-'version'.tar.gz
│ ├── secure-artifact-app-'version'.sha256
│ └── build-info.txt
├── .github/workflows/ # CI/CD pipelines
│ ├── build.yml
│ └── ci-artifactory.yml
└── README.md
---

## Key Takeaways
\- Demonstrates **secure software supply-chain fundamentals**
\- Shows real-world JFrog Artifactory \& Xray usage
\- Implements least-privilege CI/CD authentication
\- Provides a strong base for policy enforcement and compliance
\- Designed for **DevSecOps and platform security roles**
---

## Future Enhancements
\- Enforce Xray blocking policies
\- Integrate SBOM generation
\- Use OIDC-based authentication
---

## Author
**Novya** **Sharma**
DevSecOps | CI/CD Security | Software Supply Chain Security
Open to DevSecOps / Platform Security roles