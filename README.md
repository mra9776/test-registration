## happy path:
```
$ curl -v -X POST localhost:8080/api/v1/users/signup --json '{"social_number": "1234567893", "full_name": "user1", "mobile": "09190001112233"}'

< HTTP/1.1 200 OK
< Server: nginx/1.29.0
< Date: Thu, 24 Jul 2025 17:46:20 GMT
< Content-Type: application/json
< Content-Length: 45
< Connection: keep-alive
<
{"id":"78f435cc-4d3f-4137-8c12-10dcedfec00a"}
```

## user already exists:
```
$ curl -v -X POST localhost:8080/api/v1/users/signup --json '{"social_number": "1234567892", "full_name": "user1", "mobile": "09190001112233"}'

< HTTP/1.1 409 Conflict
< Server: nginx/1.29.0
< Date: Thu, 24 Jul 2025 17:45:03 GMT
< Content-Type: application/json
< Content-Length: 28
< Connection: keep-alive
<
{"detail":"social number already used"}
```

## bad input

```
curl -v -X POST localhost:8080/api/v1/users/signup --json '{"social_number": "21234567892", "full_name": "user1", "mobile": "09190001112233"}'

< HTTP/1.1 422 Unprocessable Entity
< Server: nginx/1.29.0
< Date: Thu, 24 Jul 2025 17:45:08 GMT
< Content-Type: application/json
< Content-Length: 165
< Connection: keep-alive
<
{"detail":[{"type":"string_too_long","loc":["body","social_number"],"msg":"String should have at most 10 characters","input":"21234567892","ctx":{"max_length":10}}]}*

```