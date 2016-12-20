from setuptools import setup, find_packages

setup (
    name                    = "todobackend",
    version                 = "0.1.0",
    description             = "Docker with Ansible Learn Class. Rest services.",
    packages                = find_packages(),
    include_package_data    = True,
    scripts                 = ["manage.py"],
    install_requires       = [
        "Django==1.10.4",
        "django-cors-headers==1.3.1",
        "djangorestframework==3.5.3",
        "MySQL-python==1.2.5"
    ],
    extras = {
        "test": [
            "colorama==0.3.7",
            "coverage==4.2",
            "django-nose==1.4.4",
            "nose==1.3.7",
            "pinocchio==0.4.2"
        ]
    }
)
