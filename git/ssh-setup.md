# Git Notes - Day 1

## Objective

Understand the difference between Git configuration, authentication, remotes, and why a `403 Permission Denied` error occurs.

---

# Problem Faced

While pushing my first commit, I encountered:

```text
remote: Permission to Vishnu473/learn-build-repeat.git denied to otherAccount-data.
fatal: unable to access 'https://github.com/Vishnu473/learn-build-repeat.git/': The requested URL returned error: 403
```

---

# Root Cause

The repository belonged to **Vishnu473**, but Git was authenticating using cached HTTPS credentials for another GitHub account.

The remote URL was correct.

The authentication identity was wrong.

---

# Important Learning

There are **three independent identities** in Git.

## 1. Commit Identity

This determines who appears as the author of a commit.

```bash
git config user.name
git config user.email
```

Example:

```bash
git config user.name "Vishnu"
git config user.email "my-email@example.com"
```

Changing these does **not** change the GitHub account used to push.

---

## 2. Remote

The remote determines **where** the code is pushed.

Check:

```bash
git remote -v
```

HTTPS example:

```text
https://github.com/Vishnu473/learn-build-repeat.git
```

SSH example:

```text
git@github:Vishnu473/learn-build-repeat.git
```

---

## 3. Authentication

Authentication determines **who is allowed to push**.

Examples:

- HTTPS + Windows Credential Manager
- GitHub CLI
- SSH Keys

In my case, HTTPS credentials were cached for another account, causing the 403 error.

---

# Why SSH?

SSH authenticates using a private/public key pair instead of a username and password.

Advantages:

- No repeated logins
- No Personal Access Token required
- Works well with multiple repositories
- Preferred by many developers

---

# SSH Setup

## Generate a key (if required)

```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

---

## SSH Config

Location:

```text
C:\Users\<username>\.ssh\config
```

Configuration:

```text
Host github
    HostName github.com
    User git
    IdentityFile C:\Users\<username>\.ssh\id_ed25519_vishnu
    IdentitiesOnly yes
```

---

## Test SSH Connection

```bash
ssh -T git@github
```

Successful output:

```text
Hi Vishnu473! You've successfully authenticated, but GitHub does not provide shell access.
```

This confirms:

- SSH key is valid
- GitHub recognizes the account
- Authentication is working

---

# Convert Repository from HTTPS to SSH

Check current remote:

```bash
git remote -v
```

Update remote:

```bash
git remote set-url origin git@github:Vishnu473/learn-build-repeat.git
```

Verify:

```bash
git remote -v
```

Expected:

```text
origin  git@github:Vishnu473/learn-build-repeat.git (fetch)
origin  git@github:Vishnu473/learn-build-repeat.git (push)
```

---

# Useful Commands

## Check local Git configuration

```bash
git config --local --list
```

## Check global configuration

```bash
git config --global --list
```

## Show current remote

```bash
git remote -v
```

## Change remote

```bash
git remote set-url origin <new-url>
```

## Check SSH keys

```bash
dir %USERPROFILE%\.ssh
```

## Test GitHub authentication

```bash
ssh -T git@github
```

---

# Biggest Takeaway

A Git push depends on three separate things:

1. **Commit Identity** → Who wrote the commit.
2. **Remote** → Where the commit is sent.
3. **Authentication** → Whether GitHub allows the push.

These are independent of each other.

---

# Today's Lesson

Today's goal was to learn Python, but I also learned an important Git concept:

> A 403 error doesn't necessarily mean the repository or code is wrong. It often means Git is authenticating as the wrong user.

Understanding the difference between **author**, **remote**, and **authentication** makes Git much easier to troubleshoot.

---

# Why SSH in This Setup?

This repository uses SSH instead of HTTPS to support working with multiple GitHub identities on the same computer.

For example:

- Another developer (or another GitHub account) may already be signed in using GitHub Desktop, Git Credential Manager, or a browser.
- This repository can still authenticate silently using its own SSH key.
- No logout or account switching is required.
- Existing GitHub sessions remain unaffected.

This is especially useful when:

- Collaborating with different GitHub accounts.
- Using separate accounts for work and personal projects.
- Sharing the same computer with another developer.
- Avoiding conflicts caused by cached HTTPS credentials.

The SSH key specified in `~/.ssh/config` determines **which GitHub account is used for this repository**, independent of who is currently signed in elsewhere.

Example:

```text
HTTPS
-------
Browser Login  ─────► GitHub Account A

SSH
----
Repository ─► SSH Key ─► GitHub Account B
```

This means one user can remain signed in normally, while another repository pushes to a different GitHub account without affecting the current login session.