
# cURL

## Get basic information
```
curl --help
curl --manual
```

## Log options

### Verbose
```
curl --verbose http://localhost:3000/hello
curl -v http://localhost:3000/hello

curl -v http://localhost:3000/hello -o saved.txt

```

### Trace
```
curl --trace dump.txt http://localhost:3000/hello
curl --trace-ascii dump2.txt http://localhost:3000/hello

curl -v --trace-time http://localhost:3000/hello
```
