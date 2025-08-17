# GitHub Actions CI/CD Setup Guide

This guide explains how to set up the automated CI/CD pipeline for your web-and-db application.

## What This Workflow Does

1. **Triggers**: Runs on every push to the `main` branch when changes are made to:
   - `app-web/` directory
   - `db-web/` directory
   - `.github/workflows/ci-cd.yml` file

2. **Builds**: Creates Docker images for both your web app and database

3. **Pushes**: Uploads images to Docker Hub with:
   - A unique timestamp-based tag (e.g., `20250115-143022-a1b2c3d`)
   - The `latest` tag

4. **Updates**: Automatically updates your Helm `values.yaml` with the new image tags

5. **Deploys**: ArgoCD automatically detects the Git changes and deploys the new images to your EKS cluster

## Prerequisites

1. **Docker Hub Account**: You need a Docker Hub account
2. **Docker Hub Access Token**: Create an access token (not your password)
3. **GitHub Repository Access**: Admin access to this repository

## Setup Steps

### Step 1: Create Docker Hub Access Token

1. Go to [Docker Hub](https://hub.docker.com/)
2. Sign in to your account
3. Go to Account Settings → Security
4. Click "New Access Token"
5. Give it a name (e.g., "GitHub Actions")
6. Copy the token (you won't see it again!)

### Step 2: Add GitHub Secrets

1. Go to your GitHub repository: `https://github.com/yagen1111/helm-web-db`
2. Click on "Settings" tab
3. Click on "Secrets and variables" → "Actions"
4. Click "New repository secret"
5. Add these two secrets:

   **Secret Name**: `DOCKERHUB_USERNAME`
   **Secret Value**: Your Docker Hub username (e.g., `yagen1111`)

   **Secret Name**: `DOCKERHUB_TOKEN`
   **Secret Value**: The access token you created in Step 1

### Step 3: Verify Workflow File

Make sure the `.github/workflows/ci-cd.yml` file exists in your repository.

## How It Works

1. **Push Code**: When you push changes to `app-web/` or `db-web/` directories
2. **Workflow Triggers**: GitHub Actions automatically starts the workflow
3. **Build Images**: Creates new Docker images with unique tags
4. **Push to Docker Hub**: Uploads images to your Docker Hub account
5. **Update Helm Values**: Modifies `values.yaml` with new image tags
6. **Commit & Push**: Commits the changes back to your repository
7. **ArgoCD Sync**: ArgoCD detects the changes and deploys new images

## Image Naming Convention

- **Web App**: `yagen1111/web_and_db-web:YYYYMMDD-HHMMSS-commit`
- **Database**: `yagen1111/web_and_db-db:YYYYMMDD-HHMMSS-commit`
- **Latest Tags**: Both images also get `:latest` tags

## Example Workflow Run

```
✅ Build completed successfully!
📦 Web App Image: docker.io/yagen1111/web_and_db-web:20250115-143022-a1b2c3d
📦 DB Image: docker.io/yagen1111/web_and_db-db:20250115-143022-a1b2c3d
🏷️  Tag: 20250115-143022-a1b2c3d
🔗 ArgoCD will automatically detect the changes and deploy the new images
```

## Troubleshooting

### Common Issues

1. **Docker Hub Authentication Failed**
   - Check your `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN` secrets
   - Ensure the token has the correct permissions

2. **Workflow Not Triggering**
   - Make sure you're pushing to the `main` branch
   - Check that you're modifying files in `app-web/` or `db-web/` directories

3. **Build Failures**
   - Check your Dockerfile syntax
   - Ensure all required files are present in the build context

### Viewing Logs

1. Go to your GitHub repository
2. Click on "Actions" tab
3. Click on the workflow run you want to inspect
4. Click on the job to see detailed logs

## Security Notes

- The workflow uses `[skip ci]` in commit messages to prevent infinite loops
- Docker Hub credentials are stored as encrypted secrets
- The workflow only runs on pushes to the main branch

## Next Steps

After setting up the secrets:

1. Make a small change to a file in `app-web/` or `db-web/`
2. Push to the main branch
3. Watch the workflow run in the Actions tab
4. Check Docker Hub for your new images
5. Monitor ArgoCD for automatic deployment

Your CI/CD pipeline is now fully automated! 🚀
