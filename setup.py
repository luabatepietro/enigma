from setuptools import setup, find_packages

setup(
    name="codificacao_algebra_linear",  # Nome do pacote
    version="0.1.0",  # Versão do pacote
    packages=find_packages(),  # Encontrar automaticamente todos os pacotes
    install_requires=[  # Dependências
        'setuptools',
        'numpy'
    ],
    entry_points={
        "console_scripts": [
            "demo_codificacao=demo:demo",  # Apontando para a função demo no arquivo demo.py
        ],
    },
    author="Lucas Abatepietro",  # Seu nome
    author_email="luabatepietro@hotmail.com",  # Seu email
    description="Sistema de Codificação e Decodificação utilizando Álgebra Linear",
    long_description=open("README.md").read(),  # Descrição longa (usualmente do README)
    long_description_content_type="text/markdown",
    url="https://github.com/luabatepietro/codificacao_algebra_linear.git",  # URL do seu repositório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Versão mínima do Python
)
