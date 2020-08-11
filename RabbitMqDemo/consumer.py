import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.108'))

channel = connection.channel()

channel.queue_declare(queue='hello queue')


def callback(ch, method, properties, body):
    print('ch', ch)  # 管道的内存对象地址
    print('me', method)
    print('pro', properties)
    print('body', body)  # 消息内容
    print("[x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # 向生产者发送确认消息


channel.basic_qos(prefetch_count=1)  # 处理完当前这条信息再发送下一条消息，公平消息机制，这样就不会因为某些处理速度慢的机器一直收到消息而处理不完
channel.basic_consume(  # 消费信息
    callback,  # 如果收到消息，就调用CALLBACK函数来处理消息
    queue='hello queue',
    no_ack=True)
print('[*] Waiting for message. to exit press CTRL+C')

# 开始收消息
channel.start_consuming()