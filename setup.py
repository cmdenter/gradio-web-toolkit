from setuptools import setup, find_packages

setup(
    name='gradio-web-toolkit',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'gradio',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A toolkit for creating Gradio apps with SEO and accessibility features',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/gradio-web-toolkit',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
