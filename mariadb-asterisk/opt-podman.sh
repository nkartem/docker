#!/bin/bash
cd /home/lion/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user disable container-mariadb.service
systemctl --user disable container-phpmyadmin.service
systemctl --user disable container-asterisk.service
systemctl --user daemon-reload
rm *.service
ls -l /home/lion/.config/systemd/user/
cd /opt/podman/
podman-compose down
podman-compose down
######################
podman-compose up -d
cd /home/lion/.config/systemd/user/
podman generate systemd --new --name mariadb --files > /home/lion/.config/systemd/user/mariadb.service
podman generate systemd --new --name phpmyadmin --files > /home/lion/.config/systemd/user/phpmyadmin.service
podman generate systemd --new --name asterisk --files > /home/lion/.config/systemd/user/asterisk.service
systemctl --user daemon-reload
systemctl --user enable container-mariadb.service
systemctl --user enable container-phpmyadmin.service
systemctl --user enable container-asterisk.service
