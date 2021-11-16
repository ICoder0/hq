# hq
HTML parser using Xpath expression then dump as json,
it's better piping action before jq stdin.

## installation

```shell
python3 setup install
```

## best practice
- step1: fetch by [cURL](https://github.com/curl/curl)
- step2: extract vars from `html/xml` via xpath and dumps as json
- step3: permutate-combine json via [jq](https://github.com/stedolan/jq)

```shell
curl http://testapi.cn | 
hq -x 'title=//xxxx' -x 'link=//xxxxx' |
jq '[.title,.link] | transpose | map({title:.[0],link:.[1]})' > test.json
```

## usage

### without special key
input
`hq -x '/html/body/text()' '<html><body>123</body></html>'`

output 
`{"_0": "123"}`

### with special key
input
`hq -x 'test=/html/body/text()' '<html><body>123</body></html>'`

output
`{"test":"123"}`

### with special file
input
`hq -x 'test=/html/body/text()' -f asd.html`

output
`{"test":"123"}`

### with piping stdin
input
`cat asd.html | hq -x 'test=/html/body/text()'`

output
`{"test":"123"}`
