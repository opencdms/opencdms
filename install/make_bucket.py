from minio import Minio
from minio.notificationconfig import (NotificationConfig, PrefixFilterRule,
                                      QueueConfig)

client = Minio("opencdms-bucket:9000",
               access_key="opencdms",
               secret_key="insecure-change-me",
               secure=False)

client.make_bucket('incoming')

config = NotificationConfig(
    queue_config_list=[
        QueueConfig(
            "arn:minio:sqs::OPENCDMS:mqtt",
            ["s3:ObjectCreated:*"],
            config_id="2",
            prefix_filter_rule=PrefixFilterRule("CA_")
        )
    ],
)

client.set_bucket_notification("incoming", config)