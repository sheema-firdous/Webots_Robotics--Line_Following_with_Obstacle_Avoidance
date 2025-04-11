from controller import Robot, DistanceSensor, Motor

# time in [ms] of a simulation step
TIME_STEP = 64
MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# Initialize Distance Sensors for obstacle detection
ps = []
psNames = [
    'ps0', 'ps1', 'ps2', 'ps3',
    'ps4', 'ps5', 'ps6', 'ps7'
]
for i in range(8):
    ps.append(robot.getDevice(psNames[i]))
    ps[i].enable(TIME_STEP)

# Initialize Ground Sensors for line following
gs_left = robot.getDevice('gs0')
gs_left.enable(TIME_STEP)
gs_right = robot.getDevice('gs2')
gs_right.enable(TIME_STEP)

# Initialize Motors
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)

# State Variables
avoiding_obstacle = False
avoidance_step = 0
step_counter = 0

# Main loop:
while robot.step(TIME_STEP) != -1:
    # Read obstacle sensors
    psValues = []
    for i in range(8):
        psValues.append(ps[i].getValue())
    
    # Obstacle detection conditions
    front_obstacle = psValues[0] > 80.0 or psValues[1] > 80.0 or psValues[2] > 80.0

    # Read ground sensors for line following
    left_value = gs_left.getValue()
    right_value = gs_right.getValue()
    left_color = "white" if left_value > 500 else "black"
    right_color = "white" if right_value > 500 else "black"
    
    # Obstacle Avoidance Logic
    if front_obstacle or avoiding_obstacle:
        avoiding_obstacle = True
        
        # Step 1: Diagonal Right
        if avoidance_step == 0:
            leftSpeed = 0.2 * MAX_SPEED
            rightSpeed = 0.5 * MAX_SPEED
            print('Step 1: Moving Diagonally Right')
            step_counter += 1
            if step_counter > 10:  # Tune this value to adjust turning duration
                avoidance_step = 1
                step_counter = 0
        
        # Step 2: Move Forward
        elif avoidance_step == 1:
            leftSpeed = 0.5 * MAX_SPEED
            rightSpeed = 0.5 * MAX_SPEED
            print('Step 2: Moving Forward')
            step_counter += 1
            if step_counter > 15:  # Tune this value to adjust forward duration
                avoidance_step = 2
                step_counter = 0
        
        # Step 3: Diagonal Left
        elif avoidance_step == 2:
            leftSpeed = 0.5 * MAX_SPEED
            rightSpeed = 0.2 * MAX_SPEED
            print('Step 3: Moving Diagonally Left')
            step_counter += 1
            if step_counter > 30:  # Tune this value to adjust turning duration
                avoidance_step = 0
                avoiding_obstacle = False
                step_counter = 0
                print('Obstacle cleared, resuming line following')

    # Line Following Logic (only if NOT avoiding obstacle)
    elif not avoiding_obstacle:
        avoidance_step = 0
        step_counter=0
        if left_color == "black" and right_color == "black":
            # Go straight
            leftSpeed = 0.5 * MAX_SPEED
            rightSpeed = 0.5 * MAX_SPEED
            print('Both sensors on black, going straight')
        elif left_color == "white" and right_color == "black":
            # Turn right
            leftSpeed = 0.5 * MAX_SPEED
            rightSpeed = -0.5 * MAX_SPEED
            print('Left white, right black: turning right')
        elif left_color == "black" and right_color == "white":
            # Turn left
            leftSpeed = -0.5 * MAX_SPEED
            rightSpeed = 0.5 * MAX_SPEED
            print('Left black, right white: turning left')
        else:
            # Both white: keep moving slowly to find the line again
            leftSpeed = 0.3 * MAX_SPEED
            rightSpeed = 0.3 * MAX_SPEED
            print('Both sensors on white, searching for line')




    # Set motor speeds
    leftMotor.setVelocity(leftSpeed)
    rightMotor.setVelocity(rightSpeed)
