from src.openhand_node.hands import Model_O

if __name__ == '__main__':
    T = Model_O('/dev/ttyUSB0', 4, 1, 2, 3, 'XM', 0.0, 0.36, -0.11, 0.05)
    T.readHand()
    T.readLoads()
    # T.readMotorMins()
    # T.moveMotor()
    T.pinch_close()
    # T.close(0.5)
    # T.reset()
    T.release()
