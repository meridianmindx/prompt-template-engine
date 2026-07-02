"""Release automation for prompt-template-engine."""
import subprocess
import sys


def create_release(version):
    """Create a new release on GitHub."""
    tag = f"v{version}"
    print(f"Creating release v{version}")

    # Build the package
    subprocess.run([sys.executable, "setup.py", "sdist", "bdist_wheel"], check=True)

    # Git tag
    subprocess.run(["git", "tag", "-a", tag, "-m", f"Release v{version}"], check=True)
    subprocess.run(["git", "push", "origin", tag], check=True)

    print(f"Release v{version} created: {tag}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        create_release(sys.argv[1])
    else:
        print("Usage: release.py <version>")
