# Python Poetry Project Template

A template repository for Python projects using Poetry for dependency management, with PyTorch support and structured logging configuration.

## ✨ Features

- 🐍 **Python 3.9+** support
- 📦 **Poetry** for dependency management
- 🧪 **pytest** with coverage reporting
- 📝 **Structured logging** with coloredlogs and colorlog
- 🔥 **PyTorch** and torchvision support
- 📁 **Standard src-layout** project structure
- 🔄 **GitHub Actions** CI/CD workflow

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- Poetry ([installation instructions](https://python-poetry.org/docs/#installation))

### Using This Template

1. **Click "Use this template"** button at the top of this repository
2. **Clone your new repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   cd YOUR_REPO_NAME
   ```

3. **Customize the project**:
   
   Update `pyproject.toml`:
   - Replace `{{PROJECT_NAME}}` with your project name (e.g., `my-awesome-project`)
   - Replace `{{PROJECT_DESCRIPTION}}` with your description
   - Replace `{{AUTHOR_NAME}}` with your name
   - Replace `{{AUTHOR_EMAIL}}` with your email
   - Replace `{{PACKAGE_NAME}}` with your package name (e.g., `my_awesome_project`)
   
   Rename the package directory:
   ```bash
   mv src/package_template src/your_package_name
   ```
   
   Update this README.md with your project information

4. **Install dependencies**:
   ```bash
   poetry install
   ```

### 🎮 PyTorch GPU Support

By default, this template installs PyTorch with CPU support. If you have CUDA-enabled hardware:

```bash
poetry run pip uninstall torch torchvision
poetry run pip install torch torchvision --index-url https://download.pytorch.org/whl/cu129
```

> **Note:** Poetry can take a long time resolving PyTorch dependencies. This template uses CPU version by default for faster installation.

## 📁 Project Structure

```
.
├── .github/
│   └── workflows/
│       └── test.yml           # CI/CD pipeline
├── src/
│   └── package_template/      # Main package (rename this!)
│       ├── __init__.py         # Package initialization with version info
│       ├── __main__.py         # CLI entry point
│       └── logging_config.py   # Structured logging configuration
├── tests/                      # Test directory
│   └── __init__.py
├── .gitignore
├── pyproject.toml             # Project dependencies and configuration
└── README.md
```

## 🧪 Running Tests

Run all tests:
```bash
poetry run pytest
```

Run tests with coverage report:
```bash
poetry run pytest --cov=your_package_name --cov-report=html
```

View coverage report:
```bash
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
```

## 🏃 Running the Package

As a module:
```bash
poetry run python -m your_package_name
```

## 🛠️ Development

Activate the virtual environment:
```bash
poetry shell
```

Install with dev dependencies:
```bash
poetry install --with dev
```

Add a new dependency:
```bash
poetry add package-name
```

Add a dev dependency:
```bash
poetry add --group dev package-name
```

## 📊 Logging

This template includes a comprehensive logging configuration with:
- ✅ Colored console output (using coloredlogs or colorlog)
- ✅ File rotation support
- ✅ Configurable log levels
- ✅ Fallback to basic ANSI colors if dependencies not available

Example usage:
```python
from package_template import get_logger

logger = get_logger(__name__)
logger.info("Hello, world!")
logger.warning("This is a warning")
logger.error("This is an error")
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

Add your license here

## 👤 Author

**{{AUTHOR_NAME}}**
- Email: {{AUTHOR_EMAIL}}

---

Based on [javidaf/quantumify](https://github.com/javidaf/quantumify)