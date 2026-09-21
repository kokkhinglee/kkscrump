# Project Documentation

## Overview
This project is designed to demonstrate the use of GitHub Actions for continuous integration. It includes a workflow that automatically runs unit tests whenever changes are pushed to the main branch or when pull requests are created.

## GitHub Actions
The project utilizes a GitHub Actions workflow defined in `.github/workflows/tests.yml`. This workflow:
- Is triggered on pushes to the `main` branch and on pull requests.
- Sets up Python 3.13.
- Executes unit tests using the command `python -m unittest discover`.

## Running Tests Locally
To run the tests locally, ensure you have Python 3.13 installed and execute the following command in your terminal:
```
python -m unittest discover
```

## Contributing
Contributions to this project are welcome. Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.