import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist

state = (0.0, 0.0, 0.0, 0.0)
target_state = (5.0, 5.0, 0.0, 0.0)

def newOdom(msg):

    global state 

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y

    velx = msg.twist.twist.linear.x
    vely = msg.twist.twist.linear.y

    state = (x,y,velx,vely)

    #ADD DELAY TO ODOMETER

    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", x)

#TODO Ask if this required.
rospy.init_node("speed_controller")

sub = rospy.Subscriber("/odom", Odometry, newOdom)  #ADD DELAY TO ODOMETER
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 1)

speed = Twist()

def publish_action(action):
    
    global pub
    global speed

    speed.linear.x = 0.0
    speed.linear.y = 0.0

    if action == 0:
        speed.linear.x=0.5
    elif action==1:
        speed.linear.x=-0.5
    elif action==2:
        speed.linear.y=0.3
    else:
        speed.linear.y = -0.3
    
    pub.publish(speed)



def calc_next_state(): # TO BE EDITED
    return state
