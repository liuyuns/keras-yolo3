@call python convert.py C:\dev\Phoenix\0___model\web\tiny-model\od_net.cfg  C:\dev\Phoenix\0___model\web\tiny-model\od_net_best.weights anet-tiny\anet.h5

REM @call xcopy anet-tiny\anet.h? ..\POC\service\anet-tiny\ /y /i
@call xcopy C:\dev\Phoenix\0___model\web\tiny-model\od_net.names anet-tiny\classes.txt /y /i

