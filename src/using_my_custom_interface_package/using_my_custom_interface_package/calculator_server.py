import time
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from msg_interface_example.action import Calculator

class CalculatorActionServer(Node):
    
    def __init__(self):
        super().__init__('calculator_action_server')
        self._action_server = ActionServer(
            self,
            Calculator,
            'calculator',
            self.execute_callback)
        
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        
        feedback_msg = Calculator.Feedback()
        
        # 피드백 보내기
        for i in range(1, 10):
            feedback_msg.loading_count = i
            self.get_logger().info('Loading Count : {0}'.format(feedback_msg.loading_count))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)
            
        
        
        # 연산 진행
        result = Calculator.Result()
        if goal_handle.request.op == '+':
            result.answer = float(goal_handle.request.num_a + goal_handle.request.num_b)
        elif goal_handle.request.op == '-':
            result.answer = float(goal_handle.request.num_a - goal_handle.request.num_b)
        elif goal_handle.request.op == '*':
            result.answer = float(goal_handle.request.num_a * goal_handle.request.num_b)
        elif goal_handle.request.op == '/':
            result.answer = float(goal_handle.request.num_a / goal_handle.request.num_b)
        else:
            self.get_logger().info('You have entered an incorrect operator. It can be +, -, *, or /.')
            
        goal_handle.succeed()        
        return result
    
def main(args = None):
    rclpy.init(args=args)
    caculator_action_server = CalculatorActionServer()
    rclpy.spin(caculator_action_server)
    
if __name__ == '__main__':
    main()