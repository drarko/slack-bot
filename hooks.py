import json
import web
from slacker import Slacker

slack = Slacker('<slack-key>')

urls = ('/.*', 'hooks')

app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = web.data()
        print
        print 'DATA RECEIVED:'
        print data
        print
        obj = json.loads(data)
        if obj["action"] == "opened" :
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
                                
                slack.chat.post_message(channel, "Nuevo ISSUE en Github: " + obj["issue"]["title"] + " - " + obj["issue"]["html_url"])
                slack.chat.post_message("bot_errors", "DEBUG - Nuevo ISSUE en Github: " + data)

        return 'OK'

if __name__ == '__main__':
    app.run()


