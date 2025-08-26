# 🤝 Contributing to Word Finder

Thank you for your interest in contributing to Word Finder! This document provides guidelines and information for contributors.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Pull Request Process](#pull-request-process)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Questions or Need Help?](#questions-or-need-help)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

**Be respectful and inclusive of everyone.**

## 🚀 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include details about your configuration and environment**

### 💡 Suggesting Features

We love feature requests! If you have a suggestion for a new feature:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested functionality**
- **Provide specific examples to demonstrate the use case**
- **Describe the current behavior and explain which behavior you expected to see instead**

### 🔧 Pull Requests

- Fork the repo and create your branch from `main`
- If you've added code that should be tested, add tests
- If you've changed APIs, update the documentation
- Ensure the test suite passes
- Make sure your code follows the existing code style
- Issue that pull request!

## 🛠️ Development Setup

### Prerequisites

- Python 3.8 or higher
- Git
- A code editor (VS Code, PyCharm, etc.)

### Local Development

1. **Fork the repository**
   ```bash
   # Clone your fork
   git clone https://github.com/YOUR_USERNAME/Word-Finder.git
   cd Word-Finder
   
   # Add the original repository as upstream
   git remote add upstream https://github.com/ORIGINAL_OWNER/Word-Finder.git
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r Requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

### Development Workflow

1. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes**
   - Write your code
   - Add tests if applicable
   - Update documentation

3. **Test your changes**
   ```bash
   python main.py
   # Run any additional tests
   ```

4. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Fill out the PR template

## 📝 Code Style Guidelines

### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines
- Use type hints for all function parameters and return values
- Keep functions focused and single-purpose
- Use descriptive variable and function names

### Example of Good Code Style

```python
from typing import List, Optional
from PyQt5.QtWidgets import QMainWindow

class ModernPdfReader(QMainWindow):
    """Modern PDF reader with advanced search capabilities."""
    
    def __init__(self) -> None:
        """Initialize the PDF reader application."""
        super().__init__()
        self._setup_ui()
        self._setup_connections()
    
    def search_text(self, query: str) -> List[SearchResult]:
        """
        Search for text in the current PDF document.
        
        Args:
            query: The text to search for
            
        Returns:
            List of search results with page numbers and positions
        """
        if not query.strip():
            return []
        
        results = []
        for page_num in range(self.engine.page_count):
            page_results = self.engine.search_in_page(page_num, query)
            if page_results:
                results.extend(page_results)
        
        return results
```

### UI Code Style

- Use descriptive names for UI elements
- Group related UI elements together
- Use consistent spacing and layout
- Follow the existing naming conventions

### Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/) for commit messages:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

**Types:**
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

**Examples:**
```
feat: add dark mode toggle
fix: resolve PDF rendering crash on Windows
docs: update installation instructions
style: format code according to PEP 8
```

## 🔄 Pull Request Process

### Before Submitting

1. **Ensure your code follows the style guidelines**
2. **Test your changes thoroughly**
3. **Update documentation if needed**
4. **Check that all tests pass**

### Pull Request Template

When creating a PR, please use this template:

```markdown
## Description
Brief description of what this PR accomplishes.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] I have tested this change locally
- [ ] I have added tests for this change
- [ ] All existing tests pass

## Screenshots (if applicable)
Add screenshots to help explain your changes.

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
```

### Review Process

1. **Automated checks** will run on your PR
2. **Maintainers** will review your code
3. **Feedback** will be provided if changes are needed
4. **Approval** will be given once all concerns are addressed

## 🐛 Reporting Bugs

### Bug Report Template

```markdown
## Bug Description
Clear and concise description of what the bug is.

## Steps to Reproduce
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OS: [e.g. Windows 10, macOS 12.0, Ubuntu 20.04]
- Python Version: [e.g. 3.9.7]
- PyQt5 Version: [e.g. 5.15.9]
- PyMuPDF Version: [e.g. 1.26.4]

## Additional Context
Add any other context about the problem here.
```

## 💡 Suggesting Features

### Feature Request Template

```markdown
## Feature Description
Clear and concise description of the feature you'd like to see.

## Problem Statement
A clear and concise description of what problem this feature would solve.

## Proposed Solution
A clear and concise description of what you want to happen.

## Alternative Solutions
A clear and concise description of any alternative solutions you've considered.

## Additional Context
Add any other context or screenshots about the feature request here.
```

## ❓ Questions or Need Help?

- **GitHub Issues**: Use the issue tracker for bugs and feature requests
- **Discussions**: Use GitHub Discussions for questions and general help
- **Documentation**: Check the README and code comments first

## 🙏 Recognition

Contributors will be recognized in:
- The project README
- Release notes
- GitHub contributors list

## 📄 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

**Thank you for contributing to Word Finder! 🚀**

Your contributions help make this project better for everyone in the community.
