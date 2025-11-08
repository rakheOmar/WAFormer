# Contributing

Thanks for your interest in contributing! We appreciate all contributions, big or small.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Python** (v3.11 or higher) - [Download here](https://www.python.org/)
- **uv** (latest version) - [Installation guide](https://docs.astral.sh/uv/getting-started/installation/)
- **Git** (v2.50.1 or higher) - [Download here](https://git-scm.com/)

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/WAFormer.git`
3. Navigate to the directory: `cd WAFormer`
4. Sync dependencies: `uv sync`
5. Create a branch: `git checkout -b feature/your-feature-name`

## Development

Start the development environment:

```bash
uv run main.py
```

Install development dependencies:

```bash
uv sync --group dev
```

## Code Quality

We use Ruff for linting and formatting. Before committing:

**Linting:**

```bash
uv run ruff check .
```

**Formatting:**

```bash
uv run ruff format .
```

## Making Changes

1. Make your changes in your feature branch
2. Test your changes thoroughly
3. Run `uv run ruff check .` and `uv run ruff format .` to ensure code quality
4. Commit with a clear message following our commit conventions (see below)
5. Push to your fork
6. Open a pull request

## Commit Message Conventions

We follow the Conventional Commits specification for clear and consistent commit messages:

**Format:**

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, missing semicolons, etc.)
- `refactor`: Code refactoring without changing functionality
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `chore`: Maintenance tasks (dependencies, build config, etc.)
- `ci`: CI/CD changes

**Example:**

```
feat(logger): add JSON output support

- Implement structured logging for production environments
- Add optional JSON formatter to logger configuration
- Maintain backward compatibility with existing console output

Fixes #42
```

**Scope** (optional): The area of the codebase affected (e.g., `logger`, `exceptions`, `models`, `api`)

**Breaking Changes:**
Add `!` after the type/scope or include `BREAKING CHANGE:` in the footer:

```
feat(api)!: change response format
```

## Pull Request Guidelines

- Keep PRs focused on a single feature or fix
- Write clear descriptions of what your PR does
- Reference any related issues
- Ensure all checks pass
- Be responsive to feedback

## Code Style

- Use Python best practices and PEP 8
- Write clear, descriptive variable and function names
- Add docstrings for functions and classes
- Add comments for complex logic
- Keep functions small and focused

## Project Structure

```
WAFormer/
├── WAFormer/
│   ├── utils/
│   │   ├── logger.py       — Logging configuration
│   │   └── exceptions.py   — Custom exception classes
│   └── __init__.py
├── main.py                 — Application entry point
├── pyproject.toml          — Project configuration
└── README.md               — Project documentation
```

## Need Help?

Feel free to open an issue if you have questions or need clarification on anything.

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.
