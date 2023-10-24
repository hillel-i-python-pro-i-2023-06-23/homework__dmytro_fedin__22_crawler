# Django application

---
![Main workflow](https://github.com/hillel-i-python-pro-i-2023-06-23/homework__dmytro_fedin__22_crawler/actions/workflows/main-workflow.yml/badge.svg)

## 🏠 Homework

The simple console application to collect urls from pages.
Run it with only two arguments --link_list [url] and --link_depth [depth] and get urls in logs/urls.csv file.




### ▶️ Run

Make all actions needed for run homework from zero. Including configuration.

```shell
make d-homework-i-run
```

### 🚮 Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
```

---

## 🛠️ Dev

### Initialize dev

Install dependencies and register pre-commit.

```shell
make init-dev
```

### ⚙️ Configure

Configure homework.

```shell
make init-configs
```

---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just run

```shell
make d-run
```

### ⏹️Stop

Stop services

```shell
make d-stop
```

### 🚮 Purge

Purge all data related with services

```shell
make d-purge
```
