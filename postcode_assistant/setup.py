from setuptools import setup

setup(
    name="postcode_assistant",
    packages=["postcode_assistant"],
    tests_require=["pytest==7.1.2"],
    setup_requires=["pytest-runner"],
    test_suite="tests",
    version="0.1",
    description="Simple validator for UK postcodes",
    author="serge",
    license="MIT",
)
