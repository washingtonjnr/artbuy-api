[FLASK__BADGE]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[POSTGRES_BADGE]: https://img.shields.io/badge/PostgreSQL-000?style=for-the-badge&logo=postgresql

<h1 align="center" style="font-weight: bold;">[ARTBUY]</h1>

![flask][FLASK__BADGE]
![postgres][POSTGRES_BADGE]

<p align="center">
    <img src="./.github/logo.svg" alt="ArtBuy logo" width="300px">
</p>

<h2 id="started">📌 About</h2>
API built on Flask, made for managing users, works of art, financial transactions and auctions, providing a safe and reliable experience for buyers and sellers.

<h2 id="started">🚀 Getting started</h2>
Here you describe how to run your project locally

<h3>Prerequisites</h3>
Here you list all prerequisites necessary for running your project. For example:

- [Python](https://www.python.org/downloads/) (used: 3.9.7)
- [Pip](https://pypi.org/project/pip/) (used: 21.2.2)


<h3>Running</h3>
- Create Env: `pyenv virtualenv 3.9.7 artbuy-api`

- Active Env: `pyenv activate artbuy-api`

- Install Dependencies: `pip install -r requirement.txt`

- Config database on [api/ext/database.py]

- Run Project: `flask run`

<h3>Response</h3>

- Success: { paylaod: {}, success: true }
- Error: { errors: {}, success: false }
