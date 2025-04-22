    print("🪄 The coin is spinning", end="")
    for _ in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print()