# Publishing Guide for Docker MCP

This guide explains how to publish the Docker MCP server to various platforms.

## Prerequisites

1. **GitHub Repository**
   - Create a repository on GitHub
   - Update all URLs in `pyproject.toml` with your actual GitHub username/organization

2. **PyPI Account**
   - Register at [pypi.org](https://pypi.org)
   - Create an API token for authentication
   - Optional: Test on [test.pypi.org](https://test.pypi.org) first

## Step 1: Prepare Your Code

1. Update author information in `pyproject.toml`:
   ```toml
   authors = [
       { name = "Kerim Incedayi", email = "k@kerim.me" }
   ]
   ```

2. Ensure all tests pass:
   ```bash
   pytest tests/ -v
   ```

3. Update version number in `pyproject.toml` if needed

## Step 2: Initialize Git Repository

```bash
# Initialize git repo
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Docker MCP server implementation"

# Add remote origin
git remote add origin https://github.com/cevatkerim/docker-mcp.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Publishing to PyPI

### Manual Publishing

1. **Build the package:**
   ```bash
   pip install build twine
   python -m build
   ```

2. **Check the package:**
   ```bash
   twine check dist/*
   ```

3. **Upload to Test PyPI (optional):**
   ```bash
   twine upload --repository testpypi dist/*
   ```

4. **Upload to PyPI:**
   ```bash
   twine upload dist/*
   ```

### Automated Publishing via GitHub Actions

The repository includes GitHub Actions workflows for automated publishing:

1. **Test on every push/PR:** `.github/workflows/ci.yml` runs tests automatically

2. **Publish on release:**
   - Go to GitHub repository → Releases → Create new release
   - Tag version (e.g., `v0.1.0`)
   - The workflow will automatically publish to PyPI

3. **Manual publish to Test PyPI:**
   - Go to Actions → Publish to PyPI workflow
   - Click "Run workflow"
   - This publishes to test.pypi.org for testing

## Step 4: MCP Registry (Optional)

Submit your server to the official MCP registry:

1. Visit [MCP Registry](https://github.com/modelcontextprotocol/servers)
2. Fork the repository
3. Add your server to the registry
4. Submit a pull request

## Step 5: Installation Testing

After publishing, test installation:

```bash
# From PyPI
pip install docker-mcp

# From Test PyPI
pip install -i https://test.pypi.org/simple/ docker-mcp

# From GitHub
pip install git+https://github.com/cevatkerim/docker-mcp.git
```

## Step 6: Configure MCP Clients

Add to Claude Desktop or other MCP clients:

```json
{
  "mcpServers": {
    "docker": {
      "command": "python",
      "args": ["-m", "docker_mcp"]
    }
  }
}
```

Or using the installed script:

```json
{
  "mcpServers": {
    "docker": {
      "command": "docker-mcp"
    }
  }
}
```

## Version Management

1. **Semantic Versioning:** Use MAJOR.MINOR.PATCH format
   - MAJOR: Breaking changes
   - MINOR: New features (backward compatible)
   - PATCH: Bug fixes

2. **Update version in:**
   - `pyproject.toml`
   - Create git tag: `git tag v0.1.0`
   - Push tag: `git push origin v0.1.0`

## Security Considerations

1. **Never commit secrets:** API keys, tokens, passwords
2. **Use GitHub Secrets:** For CI/CD authentication
3. **Enable 2FA:** On PyPI and GitHub accounts
4. **Review dependencies:** Regularly update and audit

## Troubleshooting

### Build Issues
- Ensure `setuptools` and `wheel` are updated
- Check Python version compatibility

### Upload Issues
- Verify PyPI credentials
- Check package name availability
- Ensure version number is incremented

### GitHub Actions Issues
- Check workflow permissions
- Verify secrets are configured
- Review action logs for errors

## Support

For issues or questions:
- Open an issue on GitHub
- Check existing issues and discussions
- Review MCP documentation