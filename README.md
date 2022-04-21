# Test API exercise

Test framework for automated api testing Annalise.ai image tagging system.

Manual local test run is supported.
## Getting Started

Run the application [Tagged Image Manager Challenge](https://github.com/belkalite/tagged-image-manager-challenge-main-test#run-locally-fake-s3--no-cognitoauth-required)
 locally.


Python 3.8.6 or greater is required.

Create your virtualenv, activate and install dependencies:

```shell
python3 -m pip install -r requirements.txt
````

Run tests locally:

```shell
python3 -m pytest tests
```

Run smoke tests locally:

```shell
python3 -m pytest tests -m smoke
```

## Limitations

- Trigger test run by commit to image tagging system repository are planned to be implemented. 
- Cleanup data, logging and reporting are planned to be added.
- More tests and more detailed assertions are planned to be added.
