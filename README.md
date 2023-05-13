# URL shortener
![GitHub repo size](https://img.shields.io/github/repo-size/FMularski/url-shortener)
![GitHub last commit](https://img.shields.io/github/last-commit/FMularski/url-shortener?color=yellow)
![GitHub top language](https://img.shields.io/github/languages/top/FMularski/url-shortener?color=purple)

## 🌐 Created with
* Django 4.2
* Django Rest Framework 3.14.0
* drf-yasg 1.21.5
* Postgres
* Nginx
* Docker

## 🌐 About
URL shortener is an API project allowing to substitute long urls with shorter ones. The project itself consists of three docker containers being: the web application, a relational database and a reverse proxy server for serving the static content. The app was created as a recruitment task.

## 🌐 Core features
* shortening URLs
* extending URLs (shortening reversion)
* displaying the list of all shortened URLs

## 🌐 Launching and usage

* Download the project to your local machine
```bash
git clone https://github.com/FMularski/url-shortener.git
```
* Start the project with docker
```bash
docker compose up
```
During the booting up the static content is collected and the database is migrated.
* Open the app in your browser at
```bash
http://localhost:80
```
* Have fun with the project by interacting with the provided open API or use any other client of your choice.

## 🌐 Testing
The code can be tested by executing in the web app container:
```bash
pytest
```
or (if you want some extra coverage info):
```bash
pytest --cov=core/tests/
```
