"""composite"""
def main():
    """composite"""
    number = int(input())
    result = composite_function(number)
    result2 = compositefunction(number)
    print('%.2f' %result)
    print('%.2f' %result2)

def composite_function(xxx):
    """composite"""
    return fff(ggg(xxx))

def fff(xxx):
    """composite"""
    return 2*xxx

def ggg(xxx):
    """composite"""
    return (xxx/2)+1

def compositefunction(xxx):
    """composite"""
    return ggg(fff(xxx))

def fff2(xxx):
    """composite"""
    return 2*xxx

def ggg2(xxx):
    """composite"""
    return (xxx/2)+1

main()
