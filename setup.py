from setuptools import setup, find_packages

setup(
    name="codegraph",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "astroid",  # For Python AST parsing
        "esprima",  # For JavaScript parsing
        "networkx",  # For graph data structures
        "matplotlib",  # For basic visualization
        "pygraphviz",  # For advanced graph visualization
    ],
    author="Shaurya Dwivedi",
    author_email="shauryadwivediwork@gmail.com",
    description="A tool for analyzing code dependencies and generating call graphs",
    keywords="code, analysis, dependency, graph",
    python_requires=">=3.8",
)
