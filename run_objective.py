from pprint import pprint
import roslibpy

client = roslibpy.Ros(host='0.0.0.0', port=3201)
client.run()

execute_objective = roslibpy.Service(client, '/execute_objective', 'moveit_studio_agent_msgs/srv/ExecuteObjective')

request = roslibpy.ServiceRequest({
    "objective_name": "3 Waypoints Pick and Place"
})
response = execute_objective.call(request)

pprint(response)
