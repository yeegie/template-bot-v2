from setuptools import setup, find_packages

with open('requirements.txt') as f:
	required = f.read().splitlines()

setup(
    name="bot",
    version="0.1.0",
    description="Template Aiogram bot",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Egor Berdovskiy",
    author_email="lotus9200@gmail.com",
    url="https://github.com/yeegie/template-bot-v2",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=required,
	entry_points={
        'console_scripts': [
            'start_bot = bin.bot.main:main',
        ],
    },
)
