import fastf1 as ff1
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.join(dir_path, 'cache', 'ff1')
print(dir_path)

ff1.Cache.enable_cache(dir_path)

race = ff1.get_session(2021, 22, 'R').results
for count, driver in enumerate(race, start=1):
    print(f"{count} - {driver['Driver']['code']}")