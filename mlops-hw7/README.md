# HW7 — CI/CD Blue-Green

ml-сервис на fastapi, деплой blue-green через nginx.

Файлы:
- ml_pipeline.py, app.py, Dockerfile, requirements.txt
- docker-compose.blue.yml (v1.0.0, 8001) + docker-compose.green.yml (v1.1.0, 8002)
- nginx.conf — балансер, переключение комментарием строки
- .gitlab-ci.yml, .github/workflows/{ci,deploy}.yml
- doc/architecture/decisions/0001-blue-green.md

Запуск:

```bash
docker compose -f docker-compose.blue.yml up -d --build
docker compose -f docker-compose.green.yml up -d --build
docker run -d --name nginx -p 8080:80 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf:ro nginx:alpine

curl http://localhost:8080/health
curl -X POST http://localhost:8080/predict -d '{"x":[1,2,3]}' -H 'content-type: application/json'
```

Переключение на green: в nginx.conf раскомментировать строку 8002, закомментировать 8001, `docker restart nginx`.
