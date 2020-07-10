from test_case.test_cases import ExcelExcute
import os
import threading
from log.log import Logger

if __name__ == '__main__':
    cases = []
    th = []
    for path,dir,files in os.walk("../config/"):
        for file in files:
            excel_path = path+file
            s = os.path.splitext(file)[1]
            if s == '.xlsx':
                cases.append(file)
                t = threading.Thread(target=ExcelExcute().excute,args=[excel_path])
                th.append(t)
            else:
                Logger().log().info("该文件不是xlsx后缀文件，文件名为{}".format(file))
    for t in th:
        t.start()