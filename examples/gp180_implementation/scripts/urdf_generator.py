# pip install onshape-robotics-toolkit
from onshape_robotics_toolkit.robot import Robot
from onshape_robotics_toolkit.utilities.helpers import save_model_as_json
from onshape_robotics_toolkit.connect import Client
# from onshape_robotics_toolkit.log import LOGGER, LogLevel

# LOGGER.set_file_name("GP180.log")
# LOGGER.set_stream_level(LogLevel.INFO)

client = Client(env=".env")
robot = Robot.from_url(
    name="GP180",
    url="https://cad.onshape.com/documents/e87c92f9a1491476a774460b/w/f25192154fc9e1cfa421a00c/e/33e01fcde29dd373fb7f168b",
    client=client,
    max_depth=0,
    use_user_defined_root=True,
)

save_model_as_json(robot.assembly, "yaskawagp180.json")

robot.show_graph(file_name="yaskawagp180.png")

robot.save()