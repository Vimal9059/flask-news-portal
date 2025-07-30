#!/bin/bash

IP=$(curl -s ifconfig.me)
curl -s "https://dynupdate.no-ip.com/nic/update?hostname=topglobalnews.zapto.org&myip=$IP" \
  -H "Authorization: Basic bG9ob3hlNTQ1NkAwdGlyZXMuY29tOlZpbWFsQDEyMw==" \
  -H "User-Agent: topglobalnews (by Vimal)"
