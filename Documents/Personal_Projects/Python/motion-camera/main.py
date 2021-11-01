from monitor_class import monitor

monitorCamera = monitor(False)

def main():
  print('Welcome to the free motion security detection camera')

  while(True):
    monitorCamera.monitor_camera()
    print("Goodbye!")


if __name__ == "__main__":
  main()