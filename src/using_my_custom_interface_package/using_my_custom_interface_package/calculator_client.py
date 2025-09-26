import sys
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from action_msgs.msg import GoalStatus
from msg_interface_example.action import Calculator

class CalculatorActionClient(Node):
    
    def __init__(self):
        super().__init__('calculator_action_client')
        self._action_client = ActionClient(self, Calculator, 'calculator')
        
    def send_goal(self):
        goal_msg = Calculator.Goal()
        goal_msg.num_a = int(sys.argv[1])
        goal_msg.op = str(sys.argv[2])
        goal_msg.num_b = int(sys.argv[3])
        
        self._action_client.wait_for_server()
        
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback)
        self._send_goal_future.add_done_callback(self.goal_response_callback)
        
    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return
        
        self.get_logger().info('Goal accepted :)')
        
        self._get_result_future = goal_handle.get_result_async()        
        self._get_result_future.add_done_callback(self.get_result_callback)
        
    def get_result_callback(self, future):
        action_status = future.result().status
        result = future.result().result
        
        if action_status == GoalStatus.STATUS_SUCCEEDED:
            self.get_logger().info('Action succeed!')
            self.get_logger().info('Result: {0}'.format(result.answer))
            
            rclpy.shutdown()
    
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.loading_count))
        
def main(args = None):
    rclpy.init(args=args)
    
    action_client = CalculatorActionClient()
    action_client.send_goal()
    rclpy.spin(action_client)
    
if __name__ == '__main__':
    main()
        