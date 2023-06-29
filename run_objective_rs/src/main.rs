roslibrust_codegen_macro::find_and_generate_ros_messages!(
    "/opt/ros/humble/share/std_msgs",
    "/opt/ros/humble/share/geometry_msgs",
    "/opt/ros/humble/share/sensor_msgs",
    "../studio_msgs",
);

roslibrust_codegen_macro::find_and_generate_ros_messages!();

#[tokio::main]
async fn main() -> Result<(), roslibrust::RosLibRustError> {
    let client = roslibrust::ClientHandle::new("ws://0.0.0.0:3201").await?;

    let request = studio_msgs::ExecuteObjectiveRequest {
        objective_name: "3 Waypoints Pick and Place".to_string(),
        parameter_overrides: vec![],
    };
    let response = client
        .call_service::<studio_msgs::ExecuteObjectiveRequest, studio_msgs::ExecuteObjectiveResponse>(
            "/execute_objective",
            request,
        )
        .await?;

    dbg!(response);

    Ok(())
}
