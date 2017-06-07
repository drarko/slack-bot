import json
import web
import sqlite3
import os.path
from slacker import Slacker

slack = Slacker('<slack-key>')

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

if os.path.isfile("slack") == False:
    print "DB NO CREADA"
    conn = sqlite3.connect('slack', check_same_thread=False)
    c = conn.cursor()
    c.execute('create table slack (slack_id integer primary key, slack_thread_ts TEXT, issue_id int)');

conn = sqlite3.connect('slack', check_same_thread=False)
c = conn.cursor()


class hooks:
    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print

        obj = json.loads(data)



        if obj["action"] == "opened" or obj["action"] == "created" :
                if obj["repository"]["full_name"] == "TodoPago/SDK-PHP":
                        channel = "#todopago-sdk-php"
                if obj["repository"]["full_name"] == "TodoPago/SDK-Python":
                        channel = "#todopago-sdk-python"
                if obj["repository"]["full_name"] == "TodoPago/SDK-Java":
                        channel = "#todopago-sdk-java"
                if obj["repository"]["full_name"] == "TodoPago/SDK-Node.js":
                        channel = "#todopago-sdk-nodejs"
                if obj["repository"]["full_name"] == "TodoPago/SDK-Ruby":
                        channel = "#todopago-sdk-ruby"
                if obj["repository"]["full_name"] == "TodoPago/SDK-.NET":
                        channel = "#todopago-sdk-net"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-Drupal-Commerce":
                        channel = "#todopago-plg-drupal"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-VirtueMart":
                        channel = "#todopago-plg-virtue"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-ZenCart":
                        channel = "#todopago-plg-zencart"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-Magento":
                        channel = "#todopago-plg-magento"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-OpenCart":
                        channel = "#todopago-plg-open1"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-PrestaShop":
                        channel = "#todopago-plg-presta"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-WooCommerce":
                        channel = "#todopago-plg-woo"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-OsCommerce":
                        channel = "#todopago-plg-oscom"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-opencart2":
                        channel = "#todopago-plg-open2"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-Magento2":
                        channel = "#todopago-plg-magento2"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-NopCommerce":
                        channel = "#todopago-plg-nop"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-WPeCommerce":
                        channel = "#todopago-plg-wpecom"
                if obj["repository"]["full_name"] == "TodoPago/Plugin-Jigoshop":
                        channel = "#todopago-plg-jigo"
                if obj["repository"]["full_name"] == "decidir/sdk-php":
                        channel = "#decidir-sdk-php"
                if obj["repository"]["full_name"] == "decidir/sdk-java":
                        channel = "#decidir-sdk-java"
                if obj["repository"]["full_name"] == "decidir/sdk-net":
                        channel = "#decidir-sdk-net"
                if obj["repository"]["full_name"] == "decidir/magento-plugin":
                        channel = "#decidir-plg-magento"
                if obj["repository"]["full_name"] == "decidir/magento2-plugin":
                        channel = "#decidir-plg-magento2"
                if obj["repository"]["full_name"] == "decidir/prestashop-plugin":
                        channel = "#decidir-plg-presta"


                if obj["action"] == "opened":                                
                    response = slack.chat.post_message(channel, "Nuevo ISSUE en Github: " + obj["issue"]["title"] + " - " + obj["issue"]["html_url"])
                    slack.chat.post_message("bot_errors", "DEBUG - Nuevo ISSUE en Github: " + data)

                    slackResponseJson=json.loads(json.dumps(response.body))
                    c.execute("INSERT INTO slack (slack_thread_ts, issue_id) VALUES (?, ?)", (slackResponseJson["ts"], obj["issue"]["id"],))
                    conn.commit()

                elif obj["action"] == "created" :
                    c.execute("SELECT slack_id, slack_thread_ts, issue_id, COUNT(*) AS q FROM slack WHERE issue_id = ?", (int(obj["issue"]["id"]),))
                    result = c.fetchone()

                    response = slack.chat.post_message(channel, "Comentario Github - " + obj["comment"]["body"] + " " + obj["comment"]["html_url"], None, None, None, None, None, None, None, None, None, result[1])
                    slack.chat.post_message("bot_errors", "Comentario Github - " + obj["comment"]["body"] + " " + obj["comment"]["html_url"], None, None, None, None, None, None, None, None, None, result[1])

                    if result[3] == 0:
                        slackResponseJson=json.loads(json.dumps(response.body))
                        c.execute("INSERT INTO slack (slack_thread_ts, issue_id) VALUES (?, ?)", (slackResponseJson["ts"], obj["issue"]["id"],))
                        conn.commit()
        return 'OK'

if __name__ == '__main__':
    app.run()


