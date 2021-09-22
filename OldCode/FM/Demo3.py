def creat_scripts(*args):
    a = args
    b= ''
    for i in range(len(args)):
        b = b + ' ' + a[i]
    scripts = "adb shell monky " + str(b) + " 1000"
    print(scripts)

creat_scripts('-v','-v')