# HW8 — мониторинг ML-сервиса (Prometheus + Grafana + Evidently + DQOps)

## Файлы
- `app.py` — FastAPI с `/health`, `/predict`, `/metrics` (prometheus_client)
- `Dockerfile`, `docker-compose.yml` (prometheus + grafana + ml-service)
- `prometheus.yml` — скрейп ml-сервиса
- `alerts.yml` — алерт `HighLatency` (p95 > 1с)
- `grafana_dashboard.json` — дашборд: p95 latency + RPS
- `metrics_tree.py` + `metrics_tree.png` — дерево метрик (бизнес/приложение/ML/инфра)
- `vpp_architecture.py` + `vpp_architecture.png` — Kappa-схема Virtual Product Placement
- `drift_report.py` — Evidently DataDriftPreset, генерит `drift_report.html`
- `dqops_incident.sql` — SQL что вызывает инцидент data quality
- `HW8_Monitoring_Gorlishchev_Vasily.ipynb` — заполненный ноутбук

## SLO
- p95 latency < 1с
- Error rate < 1%
- Availability > 99%

## Запуск
```bash
docker compose up -d --build
```

- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (admin/admin) → подключить Prometheus как datasource → импортировать `grafana_dashboard.json`
- ML-сервис: http://localhost:8000/metrics

## Алерт
```bash
docker compose run -e SLOW=1 ml-service uvicorn app:app --host 0.0.0.0 --port 8000
# подождать 2 минуты — алерт HighLatency перейдёт в Alerting
```

## Drift report
```bash
pip install evidently pandas scikit-learn
python drift_report.py
open drift_report.html
```

## DQOps
```bash
pip install dqops
python -m dqops --host 0.0.0.0 --port 8080
# подключить MySQL → выполнить dqops_incident.sql → во вкладке Incidents увидеть инцидент
```

## Диаграммы
```bash
pip install diagrams
python metrics_tree.py
python vpp_architecture.py
```
