from enum import Enum


class Mode(Enum):
    '''
    对比方式,可根据自己的需要进行补充
    equle：字符串相等
    contain：字符串包含
    bool:bool值
    '''
    Equal = "equle"
    Contain = "contain"
    Bool = 'bool'
