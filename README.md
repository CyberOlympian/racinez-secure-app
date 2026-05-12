# Secure App - Advanced DevSecOps Pipeline

This repository demonstrates a GitHub-native DevSecOps CI pipeline.

## Features

- Flask application
- Docker containerization
- Semgrep SAST scanning
- Safety dependency scanning
- Gitleaks secret scanning
- Trivy container scanning
- SBOM generation
- Trusted artifact promotion

## Pipeline Stages

1. Security scanning
2. Docker image build
3. Container vulnerability scan
4. SBOM generation
5. Artifact upload
6. Trusted build promotion

## Security Artifacts

The pipeline generates:

- semgrep-results.json
- safety-results.json
- trivy-results.json
- sbom.cyclonedx.json
- vulnerability-summary.txt
- image-metadata.txt

## Security Practices

- Non-root Docker container
- Minimal base image
- Pinned dependencies
- SHA-based image tagging
- Multi-stage pipeline validation
