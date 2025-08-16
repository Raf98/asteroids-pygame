# Asteroids Pygame clone from BootDev

## Prerequisites
- Python 3.10+ installed
- uv project and package manager
- Access to a unix-like shell (e.g. zsh or bash)

## Virtual Environment (venv) setup

1. Create a new uv project on your computer.
    ```shell
        uv init your-project-name
        cd your-project-name
    ```

2. Create a virtual environment at the top level of your project directory:
    ```shell
        uv venv
    ```

3. Activate the virtual environment:
    ```shell
        source .venv/bin/activate
    ```

4. In a Linux bash terminal, for example, you should see (asteroids) at the beginning of your terminal prompt after activating the virtual environment:

    ```shell
        (asteroids) user@machine-name:~$
    ```

5. Add the pygame library as a project dependency:
    ```shell
        uv add pygame==2.6.1
    ```

6. Make sure pygame is installed:
    ```shell
        uv run -m pygame
    ```

This will result in an error (the test expects an exit code of 1), but the output will show that pygame is installed.

7. Run Asteroids clone game:
    ```shell
        uv run main.py
    ```
