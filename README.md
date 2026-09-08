# AI Security — The Backdoored Model

ZeroDay Reapers × TheXSSRat Cybersecurity Internship — Week 04

This repository documents a controlled AI/ML security lab focused on unsafe Python pickle deserialization and model supply-chain risk.

## Repository Structure

```text
.
├── code/          # Scripts used to create and analyze the lab sample
├── samples/       # Controlled model artifacts / sample metadata
├── analysis/      # Fickling and picklescan analysis outputs
├── screenshots/   # Evidence screenshots with the system clock visible
└── report/        # Final assessment report and supporting documents
```

## Scope

The lab demonstrates how a Python pickle can contain executable reconstruction logic through `__reduce__`, how static security tools can detect the dangerous behavior, and how controlled execution can prove the side effect in an isolated VM.

## Safety

The experiment was performed in a disposable virtual machine using a harmless marker-file side effect. Do not load untrusted pickle files on a normal workstation.

> Public repositories should avoid distributing active or weaponizable payloads unnecessarily. Keep sensitive/executable lab artifacts private or replace them with sanitized representations where appropriate.
