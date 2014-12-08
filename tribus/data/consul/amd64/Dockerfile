FROM franj/debian-amd64:jessie

# Proxy de paquetes porque ya estoy cansado de descargar paquetes
# Para probar fuera de la oficina, comente esta linea
RUN echo 'Acquire::http { Proxy "http://10.16.106.152:3142"; };' > /etc/apt/apt.conf.d/02proxy

RUN apt-get update && apt-get install unzip nano python-pip nmap

# Add consul binary
ADD https://dl.bintray.com/mitchellh/consul/0.3.1_linux_amd64.zip /tmp/consul.zip
RUN cd /bin && unzip /tmp/consul.zip && chmod +x /bin/consul && rm /tmp/consul.zip

# Add consul UI
ADD https://dl.bintray.com/mitchellh/consul/0.3.1_web_ui.zip /tmp/webui.zip
RUN cd /tmp && unzip /tmp/webui.zip && mv dist /ui && rm /tmp/webui.zip

# Add consul config
ADD ./config /config/

# ONBUILD will make sure that any additional service configuration file is added to docker conatiner as well.
ONBUILD ADD ./config /config/

# Add startup file
ADD ./consul-server /bin/consul-server
RUN chmod +x /bin/consul-server

# Expose consul ports
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 53/udp

#Create a mount point
VOLUME ["/data"]

# Entry point of container
ENTRYPOINT ["/bin/consul-server"]