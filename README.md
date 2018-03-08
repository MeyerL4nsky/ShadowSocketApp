# ShadowSocketApp

Feel pain for installing ss server&&client across different platforms.

Want a webapp to easily manage ss service.

Feels better if I can manage both CLI and server from installing to daily use within one tool.


ideas:

(1) 1 installation shell, serveral client side dockerfiles and serveral proxy server dockerfiles stored on github

(2) The shell(or powershell) will be run on client machine, install docker on client mechine and on proxy server machine via SSH

(3) The shell let client docker build the image and run from client dockerfiles on github

(4) The shell let server docker build the image and run from proxy server dockerfiles on github
  
(3) The client docker image contains SS CLI, firefox/chrome proxy configuration, manage website(manage both SS CLI and server side daily usage).

(4) The server docker image contains SS server, service monitor/manage website

questions:

(1)all service based on docker, what if manage websites are down, lose control of SS CLI and server service?

    -- Since the manage/monitor website is responsible for manage the others, they should totally be responsible for installing/runing other docker services.
    
    So , it should be :
    
    install shell==> install docker and build/run manage website container ==> build/run SS client/server container via manage website ==> manage daily usage and restart/reinstall via manage website
    
    Futher more, if there is a new released docker service pushed to github, the website will detect the update and let user know there is a new service available to install.
    
    The same goes to service update. Detect new version of the exsiting docker service.
    

