<ul>

     <li>If you want to add a task to the startup, namely that it is executed every time after the start, then the standard crontab method will not help even if you create a task for root </li>
     <li>The first thing you need to do is open the systemd  file and create your own service: sudo nano  ## /lib/systemd/system/myscript.service ##</li>
     

</ul>