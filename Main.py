import getdata  # 数据初步处理
import getcount1  # 网格划分
import juanji  # 卷积运算
import getcount3  # 统计经过卷积处理后网格中点的个数
import show3  # 展示结果

# 1.数据初步处理，删除其中速度为0的点和偏移比较大的点，参数为速度阈值
# getdata.getData(0.2, 2)
#
# # 2.划分网格，参数为网格的大小
# getcount1.grid(360, 360)
#
# # 3.卷积运算
# juanji.juanji()

# 4.统计卷积后网格中的数据,参数为删除点的阈值
getcount3.Datapreprocessing(10)

# 5.结果展示
show3.shoures()
