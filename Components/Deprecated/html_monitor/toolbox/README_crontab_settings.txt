#example for run every reboot at once: 
# @reboot /usr/bin/python /folder/pyscript.py
crontab -e :
@reboot /usr/bin/python /root/Operator/operator.py
@hourly /usr/bin/python /root/Operator/toolbox/syncsys.py
alternatively to directly python exe, use /folder/file.sh
with file.sh as python program launcher