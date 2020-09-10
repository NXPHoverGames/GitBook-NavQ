import rospy
import time
from smbus import SMBus
from sensor_msgs.msg import BatteryState
from mavros_msgs.msg import State

addr = 0x29
bus = SMBus(1)
batt_voltage = 0
current_state = State

def state_cb(msg):
    global batt_voltage
    batt_voltage = msg.voltage

def status_cb(msg):
    global current_state
    current_state = msg

def main():
    rospy.init_node("batt_node", anonymous=True)

    state_sub = rospy.Subscriber("mavros/battery", BatteryState, state_cb)
    status_sub = rospy.Subscriber("mavros/state", State, status_cb)
    rate = rospy.Rate(1)

    while((not rospy.is_shutdown()) and (not current_state.connected)):
        rate.sleep()

    while(not rospy.is_shutdown()):
        print(batt_voltage)
        percent = int(((batt_voltage - 11.1) / 1.5) * 255)
        print(percent)
        bus.write_byte(addr, percent)
        rate.sleep()
       
if __name__ == '__main__':
    main()
