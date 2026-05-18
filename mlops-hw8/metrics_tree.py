from diagrams import Diagram, Cluster
from diagrams.generic.blank import Blank


with Diagram("Metrics tree", show=False, filename="metrics_tree", direction="TB"):
    root = Blank("ML-сервис")

    with Cluster("Бизнес"):
        b1 = Blank("Выручка")
        b2 = Blank("Конверсия")
        b3 = Blank("Удержание")

    with Cluster("Приложение"):
        a1 = Blank("RPS")
        a2 = Blank("p95 latency")
        a3 = Blank("Error rate")

    with Cluster("ML"):
        m1 = Blank("Accuracy")
        m2 = Blank("Data drift")
        m3 = Blank("Pred drift")

    with Cluster("Инфра"):
        i1 = Blank("CPU")
        i2 = Blank("RAM")
        i3 = Blank("Disk")

    root >> [b1, a1, m1, i1]
