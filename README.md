# ros_study
my first ros study 

-2022년 9월 27일
- topic_tutorial 패키지
- publsiher.cpp subscriber.cpp 노드생성 
- 빌드
- 실행  

-2022년 9월 28일
- topic_tutorial 패키지
- publsiher.cpp subscriber.cpp  python노드생성 
- 빌드
- 실행

### rosrun
-노드를 실행한다 
-rosrun 패키지이름 노드이름 

### catkin_create_pkg
- 현재 위치한 작업 공간에 패키지를 생성한다.
- catkin_create_pkg 패키지이름 의존성 
'''bash
    catkin_create_pkg <패키지이름> <의존성1> <의존성2> ...
'''

'''bash
    catkin_create_pkg topic_tutorial roscpp 
    rospy std_msgs
'''
catkin_create_pkg topic_second roscpp rospy std_msgs
