# Hito 1 – Practice Repository and Project Definition

Student: Tim Severein  
Project: TapasMap-Granada

---

## 1. Milestone Goal

- Set up the development environment and repository
- Use Git/GitHub following best practices
- Document all Hito 1 steps
- Define the project (TapasMap)

---

## 2. Git/GitHub Setup

1. **Installed Git**  
   ```bash
   git --version
2. **Configured Git**
   git config --global user.name "Tim Severein"
   git config --global user.email "tim.severein@stud.uni-due.de"
3. **Created SSH key**
   ssh-keygen -t ed25519 -C "tim.severein@stud.uni-due.de"
   ssh-add ~/.ssh/id_ed25519
   - Public key uploaded to GitHub
4. **GitHub Profile Setup**
   - Name, location, university, profile picture, 2FA activated
   - Screenshots saved in docs/images/
## 3. Repository Structure
TapasMap-Granada/
├── README.md
├── LICENSE
├── .gitignore
└── docs/
    ├── hito1.md
    └── images/
## 4. Project Description - TapasMap
- Problem: Users want to quickly find and rate good tapas bars in Granada.
- Solution: Web application with a central server to store bars, manage ratings, and share recommendations.
- Technology: Python backend (e.g., Flask), later deployed in the cloud
- Minimum Viable Product (MVP):
  1. Display list of bars
  2. Add new bar
  3. Add ratings
  4. Simple search function
## 5. Screenshots/Evidence
- GitHub profile screenshot --> docs/images/profile.png
- SSH key screenshot --> docs/images/ssh.png
- 2FA screenshot --> docs/images/2FA.png
## 6. Next Steps
- Subsequent milestones will build on this repository
- Additional features (map, user reviews, cloud deployment) will be added step by step
