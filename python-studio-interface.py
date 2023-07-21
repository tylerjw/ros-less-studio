import elsie
from elsie.ext import unordered_list

slides = elsie.SlideDeck()


def init_slide(slide, header_text: str):
    # Create a header with some background color
    header = slide.box(width="fill", height="10%").rect(bg_color="#23363A")

    # Put some text into the header
    header.box(x=10, padding=10).text(
        header_text, style=elsie.TextStyle(size=30, bold=True, color="#FFFFFF")
    )

    # Return the remaining content of the slide
    return slide.fbox()


@slides.slide()
def slide1(slide):
    content = init_slide(slide, "Install roslibpy")
    content.box().code("bash", "pip install roslibpy")


@slides.slide()
def slide2(slide):
    content = init_slide(slide, "Run a Studio objective from Python")
    content.box().code(
        "python",
        """
import roslibpy

# Connect to rosbridge
client = roslibpy.Ros(host='0.0.0.0', port=3201)

# Create a service client
execute_objective = roslibpy.Service(
    client,
    '/execute_objective',
    'moveit_studio_agent_msgs/srv/ExecuteObjective'
)

# Request running an objective
request = roslibpy.ServiceRequest({
    "objective_name": "3 Waypoints Pick and Place"
})
response = execute_objective.call(request)
""",
    )


@slides.slide()
def slide3(slide):
    content = init_slide(slide, "How it Works")
    content.box().image("Studio_Websockets.drawio.svg", scale=1.2)


@slides.slide()
def slide4(slide):
    content = init_slide(slide, "So What Would I Do With This?")
    content.box().text("Anything you could do with ROS")
    content.box().text("Without the complexity of ROS or Docker", style=elsie.TextStyle(bold=True))

@slides.slide()
def slide5(slide):
    content = init_slide(slide, "Like What?")
    lst = unordered_list(content.box())
    lst.item().text("Trigger Objectives as part of your software")
    lst.item().text("Publish sensor data used by Studio")
    lst.item().text("Integrate your hardware and command it with Studio")
    lst.item().text("Create a service to run inference on images")
    lst.item().text("Bridge your logging system")
    lst.item().text("Benchmark the objectives you write")


def page_numbering(slides):
    for i, slide in enumerate(slides):
        slide.box(x="90%", y="90%", width=70, height=45).rect(
            bg_color="#23363A", rx=5, ry=5
        ).text(f"{i + 1}/{len(slides)}", style=elsie.TextStyle(color="white"))


slides.render("python-studio-interface.pdf", slide_postprocessing=page_numbering)
