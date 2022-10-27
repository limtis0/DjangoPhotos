### Start

```
python ./manage.py runserver
```

### Tests

```
pytest ./tests/
```

# API

| Path                  | Method | Description                                              |
| --------------------- | ------ | -------------------------------------------------------- |
| /api/                 | GET    | API Overview                                             |
| /api/list/            | GET    | List all saved Photos                                    |
| /api/create/          | POST   | Create new Photo listing                                 |
| /api/update/<int:pk>  | POST   | Update Photo listing with given primary key              |
| /api/delete/<int:pk>  | DELETE | Delete Photo listing with given primary key              |
| /api/import/from_api  | POST   | Import multiple Photos from a third-party API            |
| /api/import/from_file | POST   | Import multiple Photos from a file (multipart/form-data) |       |

# CLI

```
python ./manage.py <COMMAND> <ARGUMENTS>
```

| Command          | Arguments |
| ---------------- | --------- |
| import_from_file | file      |
| import_from_api  | url       |


# Tools used

| Type          | Tool                    |
| ------------- | ----------------------- |
| Framework     | Django + REST Framework |
| DBMS          | SQLite                  |
| Tests         | pytest-django           |
| Image Parsing | Selenium                |

### Why SQLite?
It is easier to store locally.

### Why Selenium?
Third-party API is protected by [Cloudflare's IAUA](https://support.cloudflare.com/hc/en-us/articles/200170076), which blocks all of the traffic from bots.
To bypass this, I used **Selenium** with additional **Selenium-Stealth** module.

To increase efficiency, Selenium Webdriver loads as a Singleton object on it's first call, and closes on app's shutdown. <sub><sup>Not without hacks, huh?</sup></sub>

~~As there is no consistent way to download pictures with Selenium only, it takes screenshot of a first image it founds on the webpage. This adds a little flexibility for a cost of an image quality.~~

Because Selenium can't donwload images, I convert them into Base64 with JavaScript, then into Bytes Array and, lastly, into a PIL Image.
