import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))  # 建立连接
channel = connection.channel()  # 声明一个管道

# 声明queue
channel.queue_declare(queue='hello queue2', durable=True)  # durable 持久化队列

channel.basic_publish(
    exchange='',
    routing_key='hello queue2',  # queue名字
    body='Hello World!',  # 消息内容
    properties=pika.BasicProperties(
        delivery_mode=2  # 使队列中的消息持久化
    )
)
print("[x] Sent 'Hello World!'")
connection.close()
