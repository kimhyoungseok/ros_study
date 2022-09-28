#include "ros/ros.h"
#include "std_msgs/Int32.h" 
//int32 4byte 1byte-8bit 

int main(int argc, char** argv)
{
    ros::init(argc, argv, "second_pub");
    ros::NodeHandle nh;

    ros:: Publisher pub = nh.advertise<std_msgs::Int32> ("my_count", 100);

    ros::Rate loop_rate(2);

    std_msgs::Int32 msg;
    msg.data = 0;

    while(ros::ok())
    {
        pub.publish(msg); //보내는거
        loop_rate.sleep(); //주기에 맞게 멈추는거 
        msg.data++;
    }

    return 0;
}