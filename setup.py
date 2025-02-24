import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Loan_Approval_App_With_Mlflow"
AUTHOR_USER_NAME = "shubh-2291"
AUTHOR_EMAIL = "iamshubhamsharma375@gmail.com"
setuptools.setup(
    name=REPO_NAME,
    version= __version__,
    author= AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/shubh-2291/shubh-2291-Loan_Approval_App_With_Mlflow",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)