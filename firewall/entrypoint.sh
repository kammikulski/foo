#!/bin/bash

ufw default deny incoming
ufw default allow outgoing

ufw allow 22/tcp
ufw allow 443
ufw allow 8080

ufw deny 3001/tcp
ufw deny 3002/tcp
ufw deny 3003/tcp
rsyslogd
ufw enable
