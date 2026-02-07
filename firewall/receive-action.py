import json
import pika
import subprocess
import time
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', stream=sys.stdout)

def ban_ip(ip):
    command = f"iptables -A INPUT -s {ip} -j DROP"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"{e}")

def unban_ip(ip):
    command = f"iptables -D INPUT -s {ip} -j DROP"
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"{e}")

def connect_to_rabbit():
    while True:
        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            return connection
        except pika.exceptions.AMQPConnectionError as e:
            logging.error(f"connection to rabbitMQ error {e}")
            time.sleep(5)

def main():
    connection = connect_to_rabbit()
    channel = connection.channel()
    channel.queue_declare(queue='fail2ban')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        message = json.loads(body)
        action = message.get('action')
        ip = message.get('ip')

        if action == 'ban':
            ban_ip(ip)
        elif action == 'unban':
            unban_ip(ip)
        else:
            print("unkown action")

    channel.basic_consume(queue='fail2ban', on_message_callback=callback, auto_ack=True)
   #waiting
    channel.start_consuming()

    
if __name__ == '__main__':
    main()
