* If you want to add a task to the startup, namely that it is executed every<br/> time after the start, then the standard crontab method will not help even if you create a task for root 
* The first thing you need to do is open the systemd  file and create your own service:<br/> 
<b> sudo nano  /lib/systemd/system/myscript.service </b>
* You should write this <br/>:
           ![alt text](https://i.ibb.co/VNY10J3/Screenshot-from-2022-07-19-22-33-01.png)
     
<br>
<pre> <b>         multi-user.target</b>: We want to apply this rule to everyone without exception</pre><br/>
<pre><b>         Type = idle</b> : Just run and forget about it</pre><br/>
<pre>   <b>      ExecStart</b> : PATH to execute script </pre>

* Then you should to change rules for this service:<br/>
<b>sudo chmod 644 /lib/systemd/system/myscript.service</b>
* Then you need to restart systemctl: <br/> <b>sudo systemctl daemon-reload </b>
*<b> sudo  systemctl enable myscript.service </b>
