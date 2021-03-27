# Smoke server examples

- Targeting JSON files from local folder:
```
smoke
```

If we want to run JSON files from specific folder (`json_data`):
```
smoke json_data
```

## Syntax for running jSON files

`get_cars#audi.json`

- get = GET request
- cars = subfolder structure
- hashtag audi is EndPoint

```
get_cats#example.json
http://localhost:3000/cats/example

get_api#helloWorld.json
http://localhost:3000/api/helloWorld

get_cars#audi.json
http://localhost:3000/cars/audi
```