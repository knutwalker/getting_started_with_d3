import json
import xmltodict

d = xmltodict.parse(open('Performance_MTABUS.xml'))

x = []
y = []
c = []

pull = {
    u'Mean Distance Between Failures - MTA Bus': x,
    u'Collisions with Injury Rate - MTA Bus': y,
    u'Customer Accident Injury Rate - MTA Bus': c
}

push = (
    "dist_between_fail",
    "collision_with_injury",
    "customer_accident_rate"
)

for indicator in d['PERFORMANCE']['INDICATOR']:
    name = indicator['INDICATOR_NAME']
    actual = indicator.get('MONTHLY_ACTUAL')
    actual = float(''.join((actual or '0').split(',')))

    pull.get(name, []).append(actual or None)

out = []
for z in zip(x, y, c):
    if not all(z):
        continue

    out.append({
        "dist_between_fail": z[0],
        "collision_with_injury": z[1],
        "customer_accident_rate": z[2]
    })

json.dump(out, open("../visualisations/data/bus_perf.json",'w'))
