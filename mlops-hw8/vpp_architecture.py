from diagrams import Diagram, Cluster
from diagrams.onprem.queue import Kafka
from diagrams.onprem.compute import Server
from diagrams.onprem.client import User
from diagrams.generic.storage import Storage
from diagrams.generic.blank import Blank


# Kappa-архитектура: один стрим, в нём весь pipeline (без батчевой ветки).
# Подходит для онлайн-замены брендов в видео.
with Diagram("Virtual Product Placement (Kappa)", show=False, filename="vpp_architecture", direction="LR"):
    user = User("Зритель")

    with Cluster("Видео-стрим"):
        ingest = Kafka("Kafka: frames")

    with Cluster("ML pipeline"):
        detect = Server("YOLO\nдетект объектов")
        seg = Server("Сегментация\nбрендов")
        gen = Server("Diffusion\nвставка лого")

    with Cluster("Выход"):
        out_stream = Kafka("Kafka: out frames")
        cdn = Storage("CDN")

    profile = Blank("Профиль\nстраны")

    user >> ingest >> detect >> seg >> gen >> out_stream >> cdn >> user
    profile >> gen
