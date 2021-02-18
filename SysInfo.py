import datetime as dt
import platform


def get_system_info():
    print('node:          {0}'.format(platform.node()))
    print('processor:     {0}'.format(platform.processor()))
    print('system:        {0}'.format(platform.system()))
    print('release:       {0}'.format(platform.release()))
    print('version:       {0}'.format(platform.version()))
    print('platform:      {0}'.format(platform.platform()))


current_minute = int(dt.datetime.now().minute)
current_hour = int(dt.datetime.now().hour)

print("Current time: {0}:{1}".format(current_hour, current_minute))

if 12 > current_hour:
    print("Good morning. Here is your system information:")
    get_system_info()
elif 18 > current_hour:
    print("Good afternoon. Here is your system information:")
    get_system_info()
else:
    print("Good evening. Here is your system information:")
    get_system_info()
