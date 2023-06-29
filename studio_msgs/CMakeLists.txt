cmake_minimum_required(VERSION 3.16.3)
project(studio_msgs)

find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(sensor_msgs REQUIRED)

set(msg_files
  "msg/BehaviorParameter.msg"
  "msg/BehaviorParameterDescription.msg"
  "msg/MoveItErrorCodes.msg"
  "srv/ExecuteObjective.srv"
)

rosidl_generate_interfaces(${PROJECT_NAME}
    ${msg_files}
  DEPENDENCIES
    builtin_interfaces
    geometry_msgs
    sensor_msgs
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
